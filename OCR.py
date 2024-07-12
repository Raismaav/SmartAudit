from pdf2image import convert_from_path
import pytesseract
import os

class OCR:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = None
        self.images = None
        # Verifica si el archivo es un PDF
        if self.file_path.endswith('.pdf'):
            self.images = self.pdf_to_img(self.file_path)
        else:
            # Si no es un PDF, asume que es una imagen y la almacena en una lista
            self.images = [self.file_path]

    def pdf_to_img(self, pdf_file):
        """Convierte un archivo PDF a imágenes."""
        return convert_from_path(pdf_file)

    def ocr_core(self, images):
        """Realiza OCR en las imágenes y extrae el texto."""
        text = ""
        for img in images:
            text += pytesseract.image_to_string(img)
        return text

    def read_text(self):
        """Lee el texto del archivo PDF o imagen."""
        if not self.images:
            print("No hay imágenes para procesar.")
            return None
        self.text = self.ocr_core(self.images)
        return self.text.upper()

    def is_readable(self):
        """Verifica si fue posible extraer texto."""
        return bool(self.text)