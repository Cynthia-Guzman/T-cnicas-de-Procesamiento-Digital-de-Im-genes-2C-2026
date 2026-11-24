# AGENTS.md — Restauración de fotografías de perros

## Contexto y objetivo
Trabajo Integrador N.º 2, IFTS 24, 2026. La aplicación ayuda a Nati, voluntaria de un refugio, a mejorar fotografías para adopción y búsqueda de perros extraviados. Priorizar la conservación de rasgos identificatorios sobre la mejora estética.

## Stack tecnológico
- Python 3.12, uv, Google Colab con GPU NVIDIA T4.
- Gradio para la interfaz.
- PyTorch, Diffusers, Accelerate y Transformers.
- Stable Diffusion x4 Upscaler (`stabilityai/stable-diffusion-x4-upscaler`).
- SigLIP (`google/siglip-base-patch16-224`).
- Pillow, NumPy, OpenCV, Matplotlib y scikit-image para procesamiento y evaluación.

## Archivos y comandos
- El notebook `TP2_RestauracionyMejorade_imagenesconModelosdeDifusion.ipynb` contiene el desarrollo y la interfaz final.
- Mantener `pyproject.toml`, `uv.lock` y `.python-version` sincronizados.
- Usar `uv sync` para preparar el entorno y `uv add <paquete>` cuando sea necesario agregar dependencias.
- Verificar CUDA con `uv run python -c "import torch; print(torch.cuda.is_available())"`.
- En Colab, activar GPU, ejecutar las celdas en orden, ajustar la ruta de datos y ejecutar el paso 3.6. La interfaz usa `demo.queue(default_concurrency_limit=1)` y `demo.launch(share=True)`.
- No afirmar que la ejecución local independiente está validada sin probarla.

## Reglas del pipeline
1. Conservar la imagen original y trabajar en RGB.
2. Advertir si el lado más corto es inferior a 112 píxeles, sin bloquear el procesamiento. Es un umbral experimental, no una garantía.
3. Comparar original, ampliación bicúbica y resultado final de Stable Diffusion x4 con reducción de ruido mediante OpenCV.
4. En la interfaz final, calcular el mapa de diferencias entre la bicúbica y el resultado final; calcular la similitud SigLIP entre el original y el resultado final.
5. Permitir descargar únicamente el resultado final en PNG.
6. No presentar detalles generados como información original recuperada. SigLIP, PSNR y SSIM no certifican la identidad del animal. Mantener las advertencias y la revisión humana.

## Reglas para agentes de programación
- Proponer un plan antes de modificar el código y realizar cambios pequeños y revisables.
- No cambiar modelos, umbrales ni funcionalidades sin justificarlo y solicitar aprobación.
- Mantener mensajes claros en español y una interfaz accesible para personas sin conocimientos técnicos.
- No incluir credenciales, tokens, cachés de modelos ni entornos virtuales en Git.
- Documentar los cambios, sus motivos y las limitaciones; no inventar pruebas ni resultados.
- Usar commits descriptivos y mantener el README coherente con el código.

## Verificaciones mínimas propuestas
- Probar una fotografía de ejemplo y verificar las dimensiones de salida x4.
- Comprobar la advertencia con una imagen inferior a 112 píxeles y otra que alcance el umbral.
- Verificar que una entrada vacía produzca un mensaje claro.
- Comprobar la comparación visual, el mapa de diferencias, el informe SigLIP y la descarga PNG.
- Revisar visualmente ojos, hocico, orejas y pelaje; informar posibles alteraciones.
- Registrar qué pruebas se ejecutaron realmente y cuáles quedaron pendientes.
