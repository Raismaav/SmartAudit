# SmartAudit

SmartAudit es un sistema de auditorías moderno y automatizado diseñado para optimizar los procesos de auditoría interna en GONTOR. Este sistema reemplaza el sistema actual, que es lento y antiguo, con una solución más rápida, escalable y eficiente, mejorando significativamente el flujo de trabajo de los auditores. La funcionalidad principal incluye la automatización de tareas mecánicas como la comparación de documentos y la eliminación de tiempos de carga prolongados.

## Para comenzar

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Prerrequisitos

Qué cosas necesitas para instalar el software y cómo instalarlas:

```
python >= 3.6
Pytesseract
Opencv-python
PyPDF2
Tkinter
```

### Instalación

Instala las dependencias del proyecto:

```
pip install pytesseract opencv-python PyPDF2
```

Nota: Tkinter generalmente viene preinstalado con Python. Si no es así, consulta cómo instalarlo para tu sistema operativo.

## Uso

Para ejecutar el programa, navega al directorio del proyecto y ejecuta:

```
python main.py
```

### Configuración

**Configuración del servicio OCR:**

- Asegúrate de tener instalado Tesseract OCR en tu sistema. Puedes descargarlo e instalarlo desde [aquí](https://github.com/tesseract-ocr/tesseract).

**Variables de entorno:**

- Define la variable de entorno `TESSDATA_PREFIX` para apuntar al directorio donde está instalado Tesseract.

Ejemplo en Windows:

```
setx TESSDATA_PREFIX "C:\Program Files\Tesseract-OCR\tessdata"
```

## Estructura del Proyecto

Breve descripción de la estructura de carpetas y archivos principales del proyecto:

- `main.py`: Punto de entrada del programa.
- `Controller.py`: Contiene la lógica principal de control de flujo del programa.
- `DebugAudit.py`: Define la lógica para la auditoría de depuración.
- `DataReader.py`: Encargado de leer y procesar los datos de entrada.
- `/files`: Directorio para almacenar archivos de entrada, como PDFs.

## Construido con

* [Python](https://www.python.org/) - El lenguaje de programación usado.
* [Pytesseract](https://pypi.org/project/pytesseract/) - OCR para convertir imágenes en texto.
* [Opencv-python](https://pypi.org/project/opencv-python/) - Biblioteca de visión por computadora y machine learning.
* [PyPDF2](https://pypi.org/project/PyPDF2/) - Biblioteca para trabajar con archivos PDF.
* [Tkinter](https://docs.python.org/3/library/tk.html) - Biblioteca para la creación de interfaces gráficas.

## Autores

* **Rafael Isaí Magaña Avila** - *Desarrollador BackEnd y Diseñador* - [raismaav.2510@gmail.com](mailto:raismaav.2510@gmail.com)
* **Laisha Melina Riestra Martinez** - *Desarrolladora FrontEnd y Diseñadora* - [laishamelina@gmail.com](mailto:laishamelina@gmail.com)


