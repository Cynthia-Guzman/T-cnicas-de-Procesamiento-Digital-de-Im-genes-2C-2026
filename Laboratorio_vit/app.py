import gradio as gr
import torch
from transformers import ViTForImageClassification, ViTImageProcessor


# 1. Carga del modelo: se realiza una sola vez al iniciar la aplicación.
modelo_id = "google/vit-base-patch16-224"
processor = ViTImageProcessor.from_pretrained(modelo_id)
model = ViTForImageClassification.from_pretrained(modelo_id)
model.eval()


# 2. Función de clasificación: prepara la imagen y obtiene las cinco predicciones.
def clasificar_imagen(imagen):
    if imagen is None:
        raise gr.Error("Cargá una imagen antes de clasificar.")

    imagen = imagen.convert("RGB")
    inputs = processor(images=imagen, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probabilidades = torch.softmax(logits, dim=-1)
    valores, indices = torch.topk(probabilidades, 5)

    return {
        model.config.id2label[indice.item()]: valor.item()
        for valor, indice in zip(valores[0], indices[0])
    }


# 3. Interfaz Gradio: recibe una imagen y muestra las probabilidades.
interfaz = gr.Interface(
    fn=clasificar_imagen,
    inputs=gr.Image(type="pil", label="Imagen para clasificar"),
    outputs=gr.Label(num_top_classes=5, label="Cinco predicciones principales"),
    title="Clasificador de imágenes con ViT",
    description=(
        "Cargá una imagen para consultar las cinco categorías más probables "
        "según el modelo google/vit-base-patch16-224."
    ),
)

if __name__ == "__main__":
    interfaz.launch()
