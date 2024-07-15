from PDFReader import PDFReader
from OCR import OCR

archivo = 'files/test_image.png'
# Reemplaza 'ruta/a/tu/archivo.pdf' con la ruta real a tu archivo PDF
pdf_reader = PDFReader(archivo)
texto = pdf_reader.read_pdf()
if pdf_reader.is_readable:
    print("El PDF es legible. Aquí está el texto:")
    print(texto)
else:
    # Crea una instancia de OCR pasando la ruta del archivo
    lector_ocr = OCR(archivo)

    # Llama al método read_text para extraer el texto del archivo
    texto = lector_ocr.read_text()

    if lector_ocr.is_readable():
        print("El archivo es legible. Aquí está el texto extraído:")
        print(texto)
    else:
        print("El archivo no es legible o no se pudo extraer texto.")