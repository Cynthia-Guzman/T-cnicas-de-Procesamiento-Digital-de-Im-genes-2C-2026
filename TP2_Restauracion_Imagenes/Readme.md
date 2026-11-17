
# Restauración de Fotografías

> Aplicación de inteligencia artificial que utiliza modelos de difusión para mejorar la resolución de fotografías de perros rescatados, 
compara los resultados con métodos tradicionales y analiza posibles alteraciones visuales para facilitar su uso responsable en publicaciones 
de adopción y búsqueda.

## 1. Descripción

Las fotografías de perros rescatados suelen presentar problemas de baja resolución, desenfoque o pérdida de detalles, lo que puede 
dificultar su utilización en publicaciones de adopción o búsqueda de animales extraviados. Este proyecto propone una aplicación 
de restauración y superresolución de imágenes mediante inteligencia artificial, orientada a mejorar su calidad visual y facilitar 
la preparación de estas publicaciones.

La aplicación está diseñada para personas que colaboran con refugios y organizaciones de rescate animal, representadas por Nati, 
una voluntaria que necesita mejorar fotografías sin contar con conocimientos técnicos de edición. Para ello, 
utiliza **Stable Diffusion x4 Upscaler**, un modelo de difusión que permite aumentar la resolución de las imágenes, y **SigLIP**, 
un modelo de análisis visual utilizado para evaluar la similitud entre la fotografía original y la versión procesada. Además, 
incorpora la interpolación bicúbica como método tradicional de comparación.

A diferencia de una herramienta que únicamente mejora la apariencia de una fotografía, este sistema busca promover un uso responsable 
de la inteligencia artificial. Permite comparar los resultados, visualizar las diferencias y consultar un informe de similitud visual, 
advirtiendo que los modelos generativos pueden modificar o inventar características del animal. De esta manera, la persona usuaria
puede evaluar si la imagen restaurada resulta adecuada para su publicación, especialmente cuando es importante preservar los rasgos 
que permiten identificar al perro.

## 2. Persona Usuaria
**Nombre:** Nati

**Contexto:Nati es voluntaria de un refugio de animales y colabora en la difusión de fotografías de perros rescatados para promover su 
adopción y ayudar en la búsqueda de animales extraviados. No cuenta con conocimientos avanzados de edición de imágenes y necesita 
una herramienta sencilla que facilite esta tarea.

**Problema:** Muchas de las fotografías que recibe tienen baja resolución, desenfoque o pérdida de detalles. Esto dificulta la 
preparación de publicaciones claras y de buena calidad. 

**Solución:** La aplicación permite a Nati cargar una fotografía, mejorar su resolución mediante Stable Diffusion x4 Upscaler y comparar 
el resultado con la imagen original y una ampliación bicúbica. También incorpora un análisis de similitud visual con SigLIP y un mapa 
de diferencias para ayudarla a identificar posibles alteraciones. De esta manera, puede revisar el resultado antes de decidir si es 
adecuado para una publicación.

## 3. Demo
### Capturas de la aplicación
La aplicación permite cargar una fotografía de un perro y verifica si cumple con el umbral mínimo recomendado de 112 píxeles en su lado más corto. También informa que cumplir este criterio no garantiza una restauración fiel.
![Captura de la aplicación](Capturas/Captura%20de%20pantalla%202026-11-16%20170959.png)
### Comparación de resultados
Se presentan tres imágenes: la fotografía original, la ampliación mediante interpolación bicúbica y el resultado final obtenido con Stable Diffusion x4 Upscaler y reducción de ruido mediante OpenCV. Esta comparación permite evaluar visualmente los cambios producidos
![Comparación de resultados](Capturas/Captura%20de%20pantalla%202026-11-16%20171101.png)


### 3.3. Análisis visual y descarga
La aplicación incorpora un mapa de diferencias y un informe de similitud visual generado con SigLIP. También muestra advertencias sobre posibles alteraciones de los rasgos del perro y permite descargar la fotografía final en formato PNG.
![Análisis visual y descarga](Capturas/Captura%20de%20pantalla%202026-11-16%20171403.png)

### Video demostrativo


## 4. Qué es real y qué es inventado

### Funcionamiento de la restauración

La aplicación utiliza **Stable Diffusion x4 Upscaler** para aumentar cuatro veces la resolución de una fotografía mediante inteligencia 
artificial generativa. A diferencia de la interpolación bicúbica, que calcula nuevos píxeles a partir de los existentes, el modelo de 
difusión genera detalles visuales a partir de patrones aprendidos durante su entrenamiento.

Esto permite obtener imágenes aparentemente más nítidas, pero no significa que se haya recuperado la información original que se perdió en la 
fotografía. Algunos detalles pueden ser reconstrucciones estimadas por el modelo.

### Detalles generados por IA

Durante la restauración, el modelo puede modificar características del perro, como la forma de los ojos, el hocico, las orejas o las marcas 
del pelaje. Estas modificaciones pueden resultar visualmente creíbles, aunque no correspondan exactamente al animal fotografiado.

En publicaciones de adopción o búsqueda de perros extraviados, preservar estos rasgos es especialmente importante porque pueden utilizarse 
para identificar al animal.

### Advertencias para la persona usuaria

La aplicación incorpora una advertencia cuando la fotografía tiene menos de **112 píxeles en su lado más corto**, un umbral orientativo 
establecido a partir de las pruebas realizadas durante el proyecto.

También permite comparar la imagen original con la ampliación bicúbica y la restauración generativa, además de consultar un mapa de 
diferencias y un informe de similitud visual elaborado con SigLIP.

Estas herramientas ayudan a revisar el resultado, pero no garantizan que todos los rasgos originales se hayan conservado.

### Ejemplo de fallo

Durante las pruebas de honestidad realizadas en el apartado 2.8.2 del notebook, se redujo una fotografía de referencia de 512 × 512 píxeles a una resolución de 64 × 64 píxeles para evaluar el comportamiento de Stable Diffusion x4 Upscaler.

Se compararon tres resultados: la fotografía original de referencia, la ampliación mediante interpolación bicúbica y la restauración generativa.

La interpolación bicúbica produjo una imagen borrosa, pero mantuvo aproximadamente la estructura del animal. En cambio, Stable Diffusion x4 generó detalles visuales artificiales y alteró considerablemente la forma de la cabeza, el pelaje y las extremidades del perro.
![Ejemplo de fallo de Stable Diffusion x4 Upscaler](Capturas/Captura%20de%20pantalla%202026-11-16%20233249.png)
Este experimento demuestra que una imagen generada mediante superresolución puede parecer más definida sin representar fielmente al animal original. Por este motivo, la aplicación incorpora advertencias y herramientas de comparación, manteniendo la revisión humana como parte fundamental del proceso.


### Verificación de resultados

Para evaluar la restauración, la persona usuaria puede comparar visualmente la fotografía original, la versión bicúbica y la imagen generada por inteligencia artificial.

El mapa de diferencias permite localizar cambios visuales, mientras que SigLIP proporciona una medida de similitud global entre las imágenes. 
Sin embargo, una similitud elevada no garantiza que se hayan conservado todos los detalles importantes.

Por este motivo, la revisión humana sigue siendo fundamental. Cuando la fotografía se utiliza para identificar a un animal, se recomienda contrastar el resultado 
con otras imágenes originales disponibles y evitar publicar como auténticos detalles que no puedan verificarse.

## 5. Características

La aplicación integra herramientas de restauración, comparación y análisis visual para facilitar la evaluación de fotografías de perros rescatados.

- **Carga de fotografías:** permite seleccionar una imagen desde el dispositivo para iniciar el proceso de restauración.

- **Superresolución mediante inteligencia artificial:** utiliza Stable Diffusion x4 Upscaler para aumentar cuatro veces la resolución de la fotografía y generar una versión con mayor nivel de detalle visual.

- **Ampliación bicúbica:** incorpora un método tradicional de interpolación para comparar sus resultados con los obtenidos mediante inteligencia artificial.

- **Comparación de imágenes:** presenta tres fotografías en una misma fila: original, interpolación bicúbica y resultado final de Stable Diffusion x4 + OpenCV.

- **Análisis visual con SigLIP:** calcula la similitud global entre la imagen original y la restaurada y presenta un informe en lenguaje natural para facilitar su interpretación.

- **Mapa de diferencias:** genera una representación visual de los cambios entre la ampliación bicúbica y la imagen procesada mediante difusión.

- **Advertencia de baja resolución:** informa cuando la fotografía tiene menos de 112 píxeles en su lado más corto, debido al mayor riesgo de generar detalles poco fiables.

- **Reducción de ruido:** incorpora un procesamiento mediante OpenCV sobre la imagen generada por Stable Diffusion x4, para obtener el resultado final de la restauración.

- **Interfaz interactiva con Gradio:** reúne las funciones de carga, procesamiento, visualización y análisis en una interfaz sencilla, sin necesidad de que la persona usuaria programe.

- **Descarga de resultados:** permite descargar únicamente la fotografía final procesada mediante Stable Diffusion x4 y OpenCV, en formato PNG.



## 6. Tecnologías Utilizadas

### Entorno de desarrollo

El proyecto se desarrolló en Python, utilizando Google Colab como entorno principal de experimentación y ejecución de los modelos de inteligencia artificial.

Para gestionar las dependencias y organizar el proyecto se utilizó `uv`, mediante los archivos `pyproject.toml` y `uv.lock`.

- **Lenguaje:** Python 3.12.16
- **Entorno de ejecución:** Google Colab
- **Gestor de dependencias:** uv
- **Control de versiones:** Git y GitHub
- **GPU utilizada:** NVIDIA Tesla T4

### Interfaz web

Se utilizó **Gradio** para desarrollar una interfaz interactiva que permite cargar fotografías, ejecutar la restauración, comparar resultados y consultar el análisis visual.

- **Framework:** Gradio
- **Versión utilizada:** 6.32.0

### Modelos de inteligencia artificial

**Stable Diffusion x4 Upscaler**

- **Repositorio:** `stabilityai/stable-diffusion-x4-upscaler`
- **Biblioteca:** Hugging Face Diffusers
- **Versión de Diffusers utilizada:** 0.43.0
- **Función:** aumentar cuatro veces la resolución de fotografías mediante difusión generativa.
- **Licencia del modelo:** CreativeML Open RAIL++-M.
- **Referencia:** https://huggingface.co/stabilityai/stable-diffusion-x4-upscaler

**SigLIP**

- **Repositorio:** `google/siglip-base-patch16-224`
- **Biblioteca:** Hugging Face Transformers
- **Versión de Transformers utilizada:** 5.23.0
- **Función:** evaluar la similitud visual global entre la fotografía original y la restaurada.
- **Licencia del modelo:** Apache 2.0.
- **Referencia:** https://huggingface.co/google/siglip-base-patch16-224

### Procesamiento de imágenes

- **Pillow (PIL):** carga, conversión, redimensionamiento y manipulación de imágenes.
- **NumPy:** operaciones numéricas sobre matrices de píxeles.
- **OpenCV:** procesamiento de imágenes y reducción de ruido aplicada al resultado final.
- **Matplotlib:** visualización de resultados y mapas de diferencias.
- **scikit-image:** cálculo de métricas PSNR y SSIM.

### Consideraciones sobre las licencias

Los modelos preentrenados utilizados en el proyecto mantienen sus respectivas licencias y condiciones de uso, que deben respetarse al utilizarlos o distribuir resultados generados con ellos.


## 7. Arquitectura del Sistema

### Descripción de la arquitectura

La aplicación utiliza una arquitectura de procesamiento de imágenes basada en Python, que integra una interfaz web interactiva, técnicas tradicionales de procesamiento digital y modelos de inteligencia artificial.

La interfaz está desarrollada con **Gradio** y permite que la persona usuaria cargue una fotografía de un perro, ejecute su restauración y compare los resultados.

El procesamiento se organiza en tres componentes principales:

1. **Preparación y restauración:** se carga la fotografía mediante Pillow, se verifica su resolución y se generan dos versiones ampliadas: una mediante interpolación bicúbica y otra utilizando Stable Diffusion x4 Upscaler. Posteriormente, se aplica una reducción de ruido mediante OpenCV sobre la imagen generada por difusión para obtener el resultado final.

2. **Análisis y comparación:** se genera un mapa de diferencias entre la ampliación bicúbica y la restauración obtenida mediante Stable Diffusion x4. Además, SigLIP analiza la similitud visual global entre la fotografía original y la imagen restaurada mediante difusión.

3. **Presentación de resultados:** Gradio muestra tres fotografías en una misma fila: original, interpolación bicúbica y resultado final de Stable Diffusion x4 + OpenCV. Debajo se presentan el mapa de diferencias, el informe de SigLIP y las advertencias sobre posibles alteraciones visuales.

### Flujo de funcionamiento

```text
PERSONA USUARIA: NATI
        |
        v
INTERFAZ WEB - GRADIO
        |
        |-- Carga de fotografía
        |-- Verificación de resolución (112 px)
        |-- Advertencia de baja resolución
        |
        v
PREPARACIÓN DE LA IMAGEN
        |
        v
PROCESAMIENTO
        |
        +----------------------------+
        |                            |
        v                            v
INTERPOLACIÓN BICÚBICA       STABLE DIFFUSION x4
        |                            |
        |                            +----> OpenCV
        |                            |      Reducción de ruido
        |                            |            |
        |                            |            v
        |                            |      RESULTADO FINAL
        |                            |
        +-------------+--------------+
                      |
                      v
              ANÁLISIS VISUAL
                      |
              +-------+-------+
              |               |
              v               v
       MAPA DE DIFERENCIAS   SIGLIP
              |               |
              |               v
              |        SIMILITUD GLOBAL
              |               |
              +-------+-------+
                      |
                      v
              RESULTADOS EN GRADIO
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
       ORIGINAL    BICÚBICA     FINAL
                               SD x4 + OpenCV
                      |
                      v
            REVISIÓN HUMANA
                      |
                      v
          DESCARGA DEL RESULTADO FINAL
                   (PNG)
```

### Transparencia y revisión humana

La aplicación no considera que una fotografía visualmente mejorada sea necesariamente más fiel al animal original.

El mapa de diferencias y SigLIP se calculan utilizando la imagen restaurada mediante Stable Diffusion x4, antes de aplicar la reducción de ruido con OpenCV.

Estas herramientas permiten observar cambios y evaluar la similitud visual global, pero no garantizan que todos los rasgos identificatorios del perro se hayan conservado.

Por este motivo, la persona usuaria mantiene el control sobre la decisión de utilizar o descartar la fotografía restaurada.

La aplicación permite descargar únicamente el resultado final procesado mediante Stable Diffusion x4 y OpenCV, en formato PNG.
```




## 8. Instalación y Ejecución

### 8.1. Requisitos

El proyecto fue desarrollado y probado principalmente en Google Colab, utilizando aceleración por GPU para ejecutar Stable Diffusion x4 Upscaler.

**Requisitos:**

- Python 3.12.
- Gestor de dependencias `uv`.
- Conexión a Internet para descargar los modelos de Hugging Face.
- GPU NVIDIA compatible con CUDA, recomendada para ejecutar el modelo de difusión.
- Espacio de almacenamiento para los pesos de los modelos y las fotografías.

**Entorno utilizado durante las pruebas:**

- Plataforma: Google Colab.
- GPU: NVIDIA Tesla T4.
- Modelo de difusión: `stabilityai/stable-diffusion-x4-upscaler`.
- Modelo de análisis visual: `google/siglip-base-patch16-224`.

La ejecución del modelo de difusión en CPU no fue validada como alternativa práctica para este proyecto.

### 8.2. Ejecución en Google Colab

Google Colab es el entorno principal de ejecución de la aplicación.

**Paso 1. Abrir el notebook**

Abrir el archivo `.ipynb` del proyecto en Google Colab.

**Paso 2. Activar la GPU**

En Google Colab:

1. Seleccionar `Entorno de ejecución`.
2. Ingresar en `Cambiar tipo de entorno de ejecución`.
3. Seleccionar `T4 GPU` si está disponible.
4. Guardar la configuración.

La disponibilidad de GPU depende de los recursos asignados por Google Colab.

**Paso 3. Preparar el entorno**

Ejecutar las celdas de preparación del notebook, donde se instala `uv`, se configura Python 3.12 y se crean las dependencias del proyecto.

El notebook incluye la creación del proyecto con:

```bash
uv init tpi2-restauracion --python 3.12
```

Y la incorporación de dependencias mediante `uv add`.

Si el proyecto ya está creado y contiene `pyproject.toml` y `uv.lock`, se pueden instalar las dependencias registradas con:

```bash
uv sync
```

**Paso 4. Preparar las fotografías**

El notebook original utiliza Google Drive para acceder a las fotografías de prueba.

La ruta configurada durante el desarrollo fue:

```python
DATOS = Path("/content/drive/MyDrive/Restauracion_refugio/Datos")
```

Si se utiliza otra carpeta, es necesario actualizar esta ruta y los nombres de las fotografías de prueba.

**Paso 5. Ejecutar los modelos**

Ejecutar las celdas del notebook correspondientes a:

- Carga de Stable Diffusion x4 Upscaler.
- Restauración y ampliación bicúbica.
- Análisis visual mediante SigLIP.
- Procesamiento y reducción de ruido con OpenCV.
- Funciones de comparación y evaluación.

La primera ejecución puede demorar debido a la descarga de los modelos.

**Paso 6. Iniciar Gradio**

Ejecutar la celda `PASO 3.6 - INTERFAZ FINAL DE GRADIO`.

La aplicación utiliza:

```python
demo.queue(default_concurrency_limit=1)
demo.launch(share=True)
```

Gradio genera un enlace temporal que permite abrir la interfaz web mientras la sesión de Colab permanezca activa.

### 8.3. Preparación del entorno local con uv

El proyecto también permite preparar sus dependencias en una computadora mediante los archivos:

- `pyproject.toml`
- `uv.lock`
- `.python-version`

Una vez publicado el repositorio en GitHub, se podrá descargar mediante:

```bash
git clone URL_DEL_REPOSITORIO
cd NOMBRE_DE_LA_CARPETA
```

Para instalar las dependencias registradas:

```bash
uv sync
```

Para verificar la disponibilidad de CUDA:

```bash
uv run python -c "import torch; print(torch.cuda.is_available())"
```

La instalación de dependencias no garantiza por sí sola que los modelos funcionen correctamente.

También se requieren controladores NVIDIA compatibles, una instalación de PyTorch con soporte CUDA y suficiente memoria de GPU.

**Estado de validación:** la aplicación fue ejecutada en Google Colab. La ejecución local independiente mediante un único comando todavía no fue verificada.

### 8.4. Consideraciones sobre la ejecución

- La restauración mediante Stable Diffusion x4 requiere más recursos que la interpolación bicúbica.
- Las imágenes grandes pueden provocar errores por falta de memoria.
- La primera ejecución puede demorar por la descarga y carga de los modelos.
- Las sesiones de Google Colab son temporales.
- El enlace público generado por Gradio deja de funcionar cuando finaliza la sesión correspondiente.
- Los resultados pueden variar según la fotografía de entrada y la configuración del modelo.


El proyecto

## 9. Uso de la Aplicación

La aplicación cuenta con una interfaz web desarrollada con **Gradio**, diseñada para que voluntarios de refugios puedan restaurar fotografías de perros y evaluar los resultados antes de utilizarlos en publicaciones de adopción o búsqueda de animales extraviados.

### Paso 1. Acceder a la aplicación

Ejecutar el notebook en Google Colab y abrir el enlace temporal generado por Gradio para acceder a la interfaz web.

La aplicación permanece disponible mientras la sesión de Google Colab esté activa.

### Paso 2. Cargar una fotografía

Seleccionar una fotografía de un perro desde el dispositivo.

La aplicación verifica sus dimensiones y muestra una advertencia cuando el lado más corto tiene menos de **112 píxeles**, debido al mayor riesgo de generar detalles visuales poco fiables.

Esta advertencia no impide continuar con el procesamiento. El umbral es orientativo y no garantiza la fidelidad de la restauración.

### Paso 3. Ejecutar la restauración

Presionar el botón **Restaurar** para iniciar el procesamiento.

El sistema aplica los siguientes procedimientos:

1. **Interpolación bicúbica:** amplía la fotografía mediante un método tradicional.
2. **Stable Diffusion x4 Upscaler:** utiliza inteligencia artificial generativa para aumentar la resolución y producir detalles visuales.
3. **OpenCV:** aplica una reducción suave de ruido sobre la restauración generativa para obtener la fotografía final.

### Paso 4. Comparar los resultados

La aplicación presenta tres fotografías en una misma fila:

- **Fotografía original:** imagen cargada por la persona usuaria.
- **Interpolación bicúbica:** ampliación tradicional utilizada como referencia de comparación.
- **Resultado final — Stable Diffusion x4 + OpenCV:** fotografía restaurada mediante inteligencia artificial y procesada posteriormente para reducir el ruido.

Esta comparación permite observar diferencias en la nitidez, las texturas y las características del animal.

Se recomienda prestar especial atención a los ojos, el hocico, las orejas y las marcas del pelaje.

### Paso 5. Consultar el análisis visual

Debajo de las tres fotografías, la aplicación presenta dos herramientas de análisis:

- **Mapa de diferencias:** permite visualizar los cambios entre la ampliación bicúbica y la restauración generada mediante Stable Diffusion x4.
- **Informe de SigLIP:** presenta una medida de similitud visual global entre la fotografía original y la restauración generativa, acompañada de una interpretación en lenguaje natural.

Ambos análisis se realizan utilizando la restauración de Stable Diffusion x4 antes de aplicar la reducción de ruido mediante OpenCV.

Estos resultados son orientativos y no garantizan que todos los rasgos originales del perro se hayan conservado.

### Paso 6. Revisar y descargar la fotografía

La persona usuaria debe revisar las fotografías y el informe antes de decidir si el resultado es adecuado para su publicación.

Si detecta modificaciones importantes en las características del perro, se recomienda utilizar la fotografía original o contrastar el resultado con otras imágenes del mismo animal.

La aplicación permite descargar **únicamente la fotografía final procesada mediante Stable Diffusion x4 y OpenCV**, en formato PNG.

La decisión de utilizar o descartar la imagen restaurada permanece bajo responsabilidad de la persona usuaria.




## 10. Decisiones de Diseño

### Por qué Gradio

Se eligió **Gradio** porque permite desarrollar una interfaz web interactiva para utilizar modelos de inteligencia artificial sin necesidad de construir una aplicación web desde cero.

Su integración con Python y Google Colab facilita la ejecución de los modelos y la presentación de los resultados en un mismo entorno.

Desde la perspectiva de Human-AI Interaction, Gradio permite diseñar una experiencia sencilla para Nati, quien no necesita conocimientos de programación ni de edición avanzada de imágenes. La interfaz reúne la carga de fotografías, la restauración y las herramientas de comparación, evitando que la persona usuaria deba utilizar diferentes programas.

### Por qué Stable Diffusion x4 Upscaler

Se seleccionó **Stable Diffusion x4 Upscaler** porque es un modelo de difusión especializado en superresolución, capaz de aumentar cuatro veces las dimensiones de una imagen y generar detalles visuales.

A diferencia de la interpolación bicúbica, que calcula nuevos píxeles a partir de la información existente, el modelo de difusión puede generar texturas y detalles mediante patrones aprendidos durante su entrenamiento.

Esta capacidad resulta útil para mejorar fotografías de baja resolución, pero también representa un riesgo: el modelo puede modificar características del animal.

Por este motivo, se decidió incorporar la interpolación bicúbica como referencia de comparación y mostrar advertencias sobre las limitaciones de la restauración generativa.

### Por qué SigLIP

Se eligió **SigLIP** como modelo complementario de análisis visual para evaluar la similitud global entre la fotografía original y la imagen restaurada.

Su utilización permite incorporar una segunda perspectiva al proceso: además de observar si la imagen presenta mayor nitidez, se analiza si ambas fotografías mantienen una representación visual similar.

En la aplicación, SigLIP se utiliza para obtener representaciones de las imágenes y calcular su similitud, presentando el resultado mediante un informe en lenguaje natural.

Es importante señalar que este análisis no identifica automáticamente todos los detalles modificados ni garantiza que la identidad visual del perro se haya preservado. Por ello, funciona como una herramienta de apoyo a la revisión humana.

### Principios de Human-AI Interaction

**Transparencia:**

La aplicación permite visualizar la fotografía original junto con las versiones procesadas mediante interpolación bicúbica y Stable Diffusion x4 Upscaler. De esta manera, la persona usuaria puede reconocer qué resultado corresponde a cada procedimiento y comparar los cambios producidos.

**Control:**

La persona usuaria selecciona la fotografía que desea procesar, inicia la restauración y decide si utiliza o descarta el resultado. Las advertencias de resolución no bloquean automáticamente el procesamiento, sino que proporcionan información para tomar una decisión.

**Explicabilidad:**

El sistema incorpora un mapa de diferencias y un informe de similitud visual elaborado con SigLIP. Estas herramientas aportan información para interpretar los cambios entre las imágenes, aunque no explican completamente las decisiones internas del modelo generativo.

**Honestidad sobre lo generado:**

La aplicación advierte que una fotografía restaurada puede contener detalles generados por inteligencia artificial que no estaban presentes o no podían distinguirse en la imagen original.

También se estableció un umbral orientativo de 112 píxeles en el lado más corto, a partir de las pruebas realizadas, para advertir sobre imágenes con mayor riesgo de alteraciones visuales. Este valor no garantiza la fidelidad del resultado.

**Manejo de errores:**

La aplicación contempla la validación de la carga de imágenes y la comunicación de advertencias cuando la resolución es demasiado baja.

El diseño busca que los mensajes sean comprensibles para personas sin conocimientos técnicos, diferenciando las advertencias que permiten continuar del procesamiento de los errores que impiden completar una operación.

La gestión de errores durante la ejecución de los modelos deberá verificarse en las pruebas finales de la interfaz.



## 11. Conceptos de Procesamiento Digital Aplicados

### Interpolación bicúbica

La interpolación bicúbica es una técnica de redimensionamiento que calcula nuevos valores de píxeles a partir de los píxeles vecinos, utilizando una interpolación cúbica.

En el proyecto se utiliza para ampliar las fotografías mediante un método tradicional, sin recurrir a inteligencia artificial generativa. Su resultado funciona como referencia para comparar la superresolución obtenida con Stable Diffusion x4 Upscaler.

Esta comparación permite observar las diferencias entre aumentar las dimensiones de una imagen mediante cálculos matemáticos y generar nuevos detalles visuales mediante un modelo de difusión.

### Espacios de color

Las imágenes digitales pueden representarse mediante diferentes espacios de color, que determinan cómo se organiza e interpreta la información cromática.

En la aplicación se utiliza principalmente el espacio **RGB**, que representa cada píxel mediante tres canales: rojo, verde y azul.

La biblioteca Pillow permite convertir las fotografías a este formato para mantener una representación consistente durante el procesamiento y preparar las imágenes para los modelos utilizados.

### Restauración y superresolución

La superresolución busca generar una imagen de mayor resolución a partir de otra de menor resolución.

En este proyecto se aplica **Stable Diffusion x4 Upscaler**, que aumenta cuatro veces el ancho y el alto de la fotografía mediante un modelo de difusión generativa.

A diferencia de los métodos tradicionales, el modelo puede producir detalles y texturas visuales que no se distinguen en la imagen original.

Por este motivo, la restauración no se considera una recuperación exacta de información perdida, sino una reconstrucción estimada que debe ser evaluada antes de su utilización.

### Filtrado y reducción de ruido

El filtrado espacial permite modificar los valores de los píxeles para reducir ruido, suavizar regiones o resaltar determinadas características de una imagen.

La aplicación contempla una etapa opcional de reducción de ruido mediante **OpenCV**, destinada a suavizar pequeñas irregularidades de la fotografía procesada.

Este procedimiento puede mejorar la apariencia visual, aunque un filtrado excesivo también puede eliminar detalles importantes, como la textura del pelaje.

Por ello, se considera un procesamiento complementario y no un mecanismo para garantizar la fidelidad de la restauración.

### Métricas de evaluación

Para analizar los resultados se utilizan herramientas cuantitativas y visuales:

- **PSNR (Peak Signal-to-Noise Ratio):** mide la diferencia entre dos imágenes a partir del error cuadrático medio. Un valor mayor indica menor error respecto de la imagen de referencia.
- **SSIM (Structural Similarity Index):** evalúa la similitud estructural considerando aspectos como luminancia, contraste y estructura.
- **Mapa de diferencias:** permite visualizar las regiones donde existen cambios entre la ampliación bicúbica y la imagen generada por difusión.
- **Similitud visual con SigLIP:** compara representaciones visuales de la fotografía original y la restaurada para obtener una medida de similitud global.

Estas herramientas aportan información complementaria, pero ninguna permite determinar por sí sola si los detalles generados corresponden exactamente al perro original.

La evaluación combina los resultados técnicos con la inspección visual humana, especialmente de los rasgos relevantes para identificar al animal.




## 12. Uso de Agentes de IA

### Herramientas utilizadas

Para el desarrollo del proyecto se contempla el uso de **Codex (OpenAI)** como agente de programación, siguiendo el enfoque de *Vibe Engineering* propuesto por Simon Willison y trabajado durante la cursada.

Este enfoque plantea que la inteligencia artificial puede colaborar en la construcción de software, pero que las decisiones técnicas, la supervisión del código y la validación de los resultados deben permanecer bajo responsabilidad de quien desarrolla el proyecto.

### Decisiones propias

Se definieron el problema a resolver, la persona usuaria y las funcionalidades principales de la aplicación.

Las principales decisiones fueron:

- Seleccionar la restauración de fotografías de perros rescatados para publicaciones de adopción y búsqueda.
- Definir a Nati, voluntaria de un refugio, como persona usuaria.
- Utilizar **Stable Diffusion x4 Upscaler** para la superresolución.
- Incorporar **SigLIP** para el análisis de similitud visual.
- Utilizar la interpolación bicúbica como referencia de comparación.
- Desarrollar una interfaz sencilla mediante **Gradio**.
- Establecer un umbral orientativo de 112 píxeles en el lado más corto de la fotografía.
- Priorizar la conservación de los rasgos identificatorios del animal por encima de la mejora estética.

### Propuestas de agentes y revisión

Siguiendo el enfoque de *Vibe Engineering*, se plantea el uso de Codex mediante instrucciones que describen el problema, las funcionalidades esperadas, las restricciones técnicas y los criterios de validación.

**Ejemplo de prompt para Codex:**

> Necesito desarrollar una aplicación web en Python destinada a voluntarios de refugios de animales que necesitan mejorar fotografías de perros rescatados para publicaciones de adopción o búsqueda.
>
> La aplicación debe utilizar **Stable Diffusion x4 Upscaler** para aumentar la resolución de las fotografías y **SigLIP** para analizar la similitud visual entre la imagen original y la restaurada. La interfaz debe desarrollarse con **Gradio** y ejecutarse principalmente en Google Colab con GPU.
>
> **Funcionalidades que necesito:**
>
> - Permitir cargar una fotografía desde el dispositivo.




## 13. Limitaciones Conocidas

### Limitaciones del modelo

El modelo **Stable Diffusion x4 Upscaler** permite aumentar la resolución de una fotografía mediante técnicas de difusión generativa. Sin embargo, no recupera necesariamente los detalles originales que se perdieron durante la captura o la compresión de la imagen.

El modelo genera información visual a partir de patrones aprendidos durante su entrenamiento. Por este motivo, una fotografía restaurada puede presentar mayor nitidez y, al mismo tiempo, contener detalles que no estaban presentes en la imagen original.

Por su parte, **SigLIP** permite analizar la similitud visual global entre imágenes, pero no puede garantizar que todos los rasgos del animal se hayan conservado correctamente.

En consecuencia, los resultados de ambos modelos deben interpretarse como herramientas de asistencia y no como una reconstrucción exacta o una verificación automática de autenticidad.

### Resolución mínima recomendada

La calidad de la restauración depende, en parte, de la información visual disponible en la fotografía original.

Durante las pruebas del proyecto se adoptó un umbral orientativo de **112 píxeles en el lado más corto de la imagen**. Cuando una fotografía se encuentra por debajo de ese valor, la aplicación debe mostrar una advertencia sobre el mayor riesgo de generar detalles poco confiables.

Este umbral constituye un criterio práctico definido para el proyecto y no una resolución mínima oficial del modelo ni una garantía de fidelidad.

Las fotografías que no alcancen ese tamaño podrán procesarse, pero sus resultados requerirán una revisión especialmente cuidadosa.

### Alteraciones de características originales

Una de las principales limitaciones de la restauración generativa es la posibilidad de modificar características que permiten identificar a un perro.

Entre las alteraciones posibles se encuentran:

- Cambios en la forma o expresión de los ojos.
- Modificaciones en el hocico, la nariz o las orejas.
- Variaciones en el color, la textura o las manchas del pelaje.
- Aparición de detalles que no pueden verificarse en la fotografía original.
- Suavizado o modificación de marcas particulares del animal.

Estas alteraciones son especialmente relevantes cuando las fotografías se utilizan para buscar animales extraviados o promover adopciones, porque pueden generar una representación que no coincide completamente con su apariencia real.

Para reducir este riesgo, la aplicación incorpora la comparación entre la fotografía original, la ampliación bicúbica y la restauración generativa, junto con un mapa de diferencias y un análisis de similitud mediante SigLIP.

Sin embargo, estas herramientas no reemplazan la **revisión humana**, que sigue siendo necesaria antes de publicar una imagen restaurada.

### Recursos y tiempos de procesamiento

La ejecución de Stable Diffusion x4 Upscaler requiere recursos computacionales considerables, especialmente memoria de GPU, debido a la arquitectura del modelo y al proceso iterativo de generación.

Por este motivo, el entorno principal de ejecución del proyecto es **Google Colab con aceleración por GPU**, evitando depender de una computadora personal con hardware especializado.

Entre las limitaciones operativas se encuentran:

- **Disponibilidad de GPU:** Google Colab puede limitar el acceso a los aceleradores según la disponibilidad y el tipo de cuenta.
- **Consumo de memoria:** las fotografías de mayor tamaño pueden provocar errores por falta de memoria.
- **Tiempo de procesamiento:** la restauración generativa suele requerir más tiempo que la interpolación bicúbica convencional.
- **Carga de modelos:** la primera ejecución puede demorar más debido a la descarga e inicialización de los modelos.
- **Sesiones temporales:** las desconexiones o reinicios de Colab pueden requerir volver a preparar el entorno y cargar los modelos.

El tiempo de ejecución depende del tamaño de la fotografía, la configuración del modelo y los recursos disponibles en cada sesión.

Por lo tanto, no se establece un tiempo fijo de procesamiento ni se garantiza el funcionamiento continuo de la aplicación fuera de una sesión activa de Google Colab.



## 14. Métricas de Calidad (Opcional)

### PSNR

Se utilizó **PSNR (Peak Signal-to-Noise Ratio)** para cuantificar las diferencias entre imágenes mediante el error cuadrático medio de sus píxeles.

Esta métrica se expresa en decibelios (dB). Un valor más alto indica una menor diferencia respecto de la imagen utilizada como referencia.

En el proyecto, PSNR se incorporó al análisis cuantitativo de los resultados de restauración, como complemento de la comparación visual entre los métodos de procesamiento.

Es importante señalar que un valor elevado de PSNR no garantiza que la imagen restaurada conserve todos los detalles originales del animal.

### SSIM

Se utilizó **SSIM (Structural Similarity Index Measure)** para evaluar la similitud estructural entre imágenes, considerando aspectos como la luminancia, el contraste y la organización de sus estructuras visuales.

Esta métrica complementó el análisis realizado mediante PSNR, aportando una perspectiva diferente sobre las semejanzas y diferencias entre las imágenes procesadas.

Un valor de SSIM cercano a 1 indica una mayor similitud estructural entre las imágenes comparadas.

Sin embargo, una similitud estructural elevada no garantiza que características particulares del perro, como los ojos, el hocico o las manchas del pelaje, se hayan conservado correctamente.

### Interpretación de resultados

En el proyecto se combinaron métricas cuantitativas y herramientas de análisis visual para evaluar las fotografías restauradas.

Se utilizaron **PSNR y SSIM** para analizar diferencias y similitudes entre imágenes, junto con **SigLIP** para evaluar la similitud visual global y un mapa de diferencias para identificar regiones modificadas.

Los resultados se interpretaron considerando que la restauración mediante modelos de difusión puede generar detalles que no estaban presentes en la fotografía original.

Por este motivo, las métricas no se consideraron pruebas definitivas de fidelidad. Cuando no se dispone de una imagen de alta resolución como referencia, los valores obtenidos permiten describir diferencias entre las imágenes comparadas, pero no demostrar que se hayan recuperado los detalles reales del animal.

La evaluación se complementó con la inspección visual de los resultados, prestando especial atención a posibles modificaciones en los rasgos identificatorios del perro.

De esta manera, el análisis priorizó la conservación de la identidad visual del animal y no solamente el aumento de resolución o la mejora estética de la fotografía.



## 15. Trabajo Futuro

- **Incorporar un sistema de detección de posibles alteraciones en los rasgos del animal.** Ampliar el análisis visual para identificar cambios específicos en características como los ojos, el hocico, las orejas y las manchas del pelaje. Actualmente, SigLIP permite evaluar la similitud visual 
global, pero no determina qué detalles fueron modificados o generados artificialmente. Esta mejora permitiría señalar regiones que requieren una revisión más cuidadosa, sin reemplazar la evaluación humana.

- [ ] **Optimizar el procesamiento y facilitar el acceso a la aplicación.** Reducir el consumo de memoria y los tiempos de ejecución del modelo de difusión, evaluando técnicas de optimización compatibles con el hardware disponible. Como evolución del proyecto, estudiar la posibilidad de publicar 
la aplicación en una plataforma como Hugging Face Spaces, para que los voluntarios de refugios puedan utilizarla sin necesidad de configurar manualmente un entorno de Google Colab.



## 16. Reflexiones y Aprendizajes

### Aprendizajes principales

El desarrollo de este proyecto permitió comprender que la restauración de imágenes mediante inteligencia artificial no consiste simplemente en aumentar su resolución, sino en generar una nueva representación visual a partir de la información disponible.

Uno de los principales aprendizajes fue reconocer las diferencias entre los métodos tradicionales de procesamiento digital de imágenes, como la interpolación bicúbica, y los modelos generativos de difusión. Mientras que la interpolación calcula nuevos píxeles a partir de los existentes, 
Stable Diffusion x4 Upscaler puede generar detalles adicionales basándose en patrones aprendidos durante su entrenamiento.

También se profundizó en el uso de herramientas de evaluación como PSNR, SSIM, SigLIP y los mapas de diferencias, comprendiendo tanto su utilidad como sus limitaciones.

La integración de estos componentes en una interfaz desarrollada con Gradio permitió relacionar los conocimientos de procesamiento digital de imágenes con el desarrollo de una aplicación orientada a resolver un problema concreto.

### Desafíos técnicos

Uno de los principales desafíos fue integrar diferentes modelos y técnicas de procesamiento dentro de un mismo flujo de trabajo, desde la carga de la fotografía hasta la visualización y evaluación de los resultados.

La ejecución de Stable Diffusion x4 Upscaler también implicó considerar las restricciones de memoria, la disponibilidad de GPU y los tiempos de procesamiento en Google Colab.

Otro desafío importante fue establecer criterios para interpretar los resultados. Durante las pruebas se observaron casos en los que las imágenes restauradas presentaban una apariencia más nítida, pero también modificaciones en determinadas características del perro.

Esta situación llevó a incorporar comparaciones con interpolación bicúbica, métricas cuantitativas y herramientas de análisis visual, evitando evaluar la restauración únicamente por su apariencia estética.

Además, fue necesario diseñar una interfaz que presentara información técnica de manera comprensible para una persona usuaria sin conocimientos especializados.

### Reflexión sobre restauración con IA

La principal reflexión del proyecto es que **una imagen visualmente mejorada no necesariamente es una imagen más fiel a la realidad**.

Los modelos de difusión pueden producir resultados convincentes, pero parte de los detalles generados pueden ser estimaciones del modelo y no información recuperada de la fotografía original.

Esta diferencia adquiere especial importancia cuando se trabaja con imágenes de animales rescatados o extraviados. Una modificación en los ojos, el hocico o las marcas del pelaje puede afectar el reconocimiento del perro, incluso cuando la fotografía restaurada parece de mejor calidad.

Por este motivo, el proyecto no plantea la inteligencia artificial como una herramienta capaz de reconstruir fotografías con exactitud, sino como un recurso de asistencia cuyos resultados deben analizarse críticamente.

La experiencia permitió comprender la importancia de combinar el desarrollo técnico con criterios de responsabilidad, transparencia y supervisión humana.

En definitiva, **el objetivo no es obtener la fotografía más nítida posible, sino mejorar su utilidad sin perder de vista la identidad del animal que representa**.




## 17. Recursos y Referencias

### Modelos de Hugging Face

**Stable Diffusion x4 Upscaler — Stability AI**

Modelo de difusión utilizado para aumentar la resolución de las fotografías mediante superresolución generativa.

- Repositorio del modelo: https://huggingface.co/stabilityai/stable-diffusion-x4-upscaler

**SigLIP Base Patch16-224 — Google**

Modelo de visión y lenguaje utilizado para el análisis de similitud visual entre las fotografías originales y las imágenes restauradas.

- Repositorio del modelo: https://huggingface.co/google/siglip-base-patch16-224

### Documentación técnica

**Hugging Face Diffusers**

Biblioteca utilizada para ejecutar el modelo de difusión y gestionar el proceso de restauración.

- https://huggingface.co/docs/diffusers

**Hugging Face Transformers**

Biblioteca que proporciona herramientas para cargar y utilizar modelos preentrenados, incluido SigLIP.

- https://huggingface.co/docs/transformers

**Gradio**

Herramienta utilizada para desarrollar la interfaz web interactiva de la aplicación.

- https://www.gradio.app/docs

**PyTorch**

Framework de aprendizaje profundo utilizado para la ejecución de los modelos de inteligencia artificial.

- https://pytorch.org/docs/stable/index.html

**OpenCV**

Biblioteca de procesamiento digital de imágenes utilizada para operaciones de mejora y análisis visual.

- https://docs.opencv.org/

**scikit-image**

Biblioteca utilizada para el cálculo de métricas de calidad de imagen, como PSNR y SSIM.

- https://scikit-image.org/docs/stable/

**Pillow**

Biblioteca utilizada para la carga, manipulación y conversión de imágenes.

- https://pillow.readthedocs.io/

**uv — Astral**

Gestor de proyectos y dependencias de Python utilizado para organizar el entorno de desarrollo y facilitar su reproducción.

- https://docs.astral.sh/uv/

**Google Colab**

Entorno de ejecución principal del proyecto, utilizado para trabajar con modelos de aprendizaje profundo mediante aceleración por GPU.

- https://colab.research.google.com/

### Otros recursos

**Simon Willison — Vibe Engineering (2025)**

Artículo de referencia sobre el desarrollo de software asistido por agentes de inteligencia artificial, con énfasis en la supervisión humana, la revisión del código y la responsabilidad sobre las decisiones técnicas.

- https://simonwillison.net/2025/Oct/7/vibe-engineering/

**Simon Willison — Blog**

Publicaciones sobre agentes de programación, modelos de lenguaje y prácticas de desarrollo de software asistido por inteligencia artificial.

- https://simonwillison.net/

**Material de la cátedra — Procesamiento Digital de Imágenes**

Barreto, M. (2026). Materiales de la asignatura Procesamiento Digital de Imágenes. Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial, Instituto de Formación Técnica Superior N.º 24.

Se utilizaron los materiales de clase sobre modelos de difusión, superresolución, análisis visual, evaluación de resultados y desarrollo de aplicaciones con inteligencia artificial.





## 18. Autor
**Nombre:** CYNTHIA GUZMAN
**Institución:** IFTS N.º 24  
**Carrera:** Tecnicatura Superior en Ciencias de Datos e IA  
**Materia:** Procesamiento Digital de Imágenes e Introducción a Visión por Computadora  
**Año:** 2026  
**GitHub:** https://github.com/Cynthia-Guzman/T-cnicas-de-Procesamiento-Digital-de-Im-genes-2C-2026/blob/main/TP2_Restauracion_Imagenes/TP2_RestauracionyMejorade_imagenesconModelosdeDifusion.ipynb




## 19. Licencia

Los modelos de inteligencia artificial utilizados, **Stable Diffusion x4 Upscaler** y **SigLIP**, mantienen sus respectivas licencias y condiciones de uso, que deben respetarse de manera independiente.

Para consultar las condiciones de cada modelo:

- Stable Diffusion x4 Upscaler: https://huggingface.co/stabilityai/stable-diffusion-x4-upscaler
- SigLIP: https://huggingface.co/google/siglip-base-patch16-224

---

**Trabajo Integrador N.º 2 - IFTS 24 - 2026**
