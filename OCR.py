from pdf2image import convert_from_path
import pytesseract
import os


class OCR:
    def __init__(self, file_path):
        """
        Initializes the OCR object with a file path.
        If the file is a PDF, it converts it to images.
        Otherwise, it assumes the file is an image and stores it in a list.

        :param file_path: Path to the file to be processed.
        """
        self.file_path = file_path
        self.text = None
        self.__images = None
        if self.file_path.endswith('.pdf'):
            try:
                self.images = self.pdf_to_img(self.file_path)
            except Exception as e:
                print(f"Error converting PDF to images: {e}")
                self.images = []
        else:
            self.images = [self.file_path]

    def pdf_to_img(self, pdf_file):
        """
        Converts a PDF file to images.

        :param pdf_file: Path to the PDF file.
        :return: A list of images.
        """
        try:
            return convert_from_path(pdf_file, dpi=200)  # Increase resolution to improve OCR quality
        except Exception as e:
            print(f"Error during PDF to image conversion: {e}")
            return []

    def ocr_core(self, images):
        """
        Performs OCR on the images and extracts text.

        :param images: A list of images to process.
        :return: Extracted text as a string.
        """
        text = ""
        for img in images:
            try:
                text += pytesseract.image_to_string(img)
            except Exception as e:
                print(f"Error during OCR: {e}")
        return text

    def read_text(self):
        """
        Reads text from the PDF or image file.

        :return: The extracted text in uppercase.
        """
        if not self.images:
            print("No images to process.")
            return None
        self.text = self.ocr_core(self.images)
        return self.text.upper()

    def is_readable(self):
        """
        Checks if text was successfully extracted.

        :return: True if text is not None, False otherwise.
        """
        return bool(self.text)