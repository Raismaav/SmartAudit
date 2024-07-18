from PDFReader import PDFReader
from OCR import OCR
import re
import os


class DataReader:
    """
    A controller class to handle file processing, determining whether to use PDFReader or OCR
    based on the file extension, and extracting text from the file.
    """

    def __init__(self, file_path):
        """
        Initializes the FileController with the path to the file to be processed.

        :param file_path: The path to the file to be processed.
        """
        self.text = None
        self.file_path = file_path

    def get_date(self):
        """
        Searches for the first date in the extracted text using a regular expression and returns it.

        :return: The first date found in the text or None if no date is found.
        """
        date_pattern = r'\d{2}/\d{2}/\d{4}'
        dates = re.findall(date_pattern, self.text)
        if dates:
            return dates[0]
        else:
            return None

    def process_file(self):
        """
        Processes the file based on its type. Uses PDFReader for PDF files and OCR for image files.
        Prints the extracted text or an error message if the file is not readable.
        """
        file_type = self.__determine_file_type()
        if file_type == '.pdf':
            pdf_reader = PDFReader(self.file_path)
            self.text = pdf_reader.read_pdf()
            if pdf_reader.is_readable:
                self.__print_result(self.text)
            else:
                self.__print_error()
        elif file_type in ['.png', '.jpg', '.jpeg']:
            ocr_reader = OCR(self.file_path)
            self.text = ocr_reader.read_text()
            if ocr_reader.is_readable():
                self.__print_result(self.text)
            else:
                self.__print_error()
        else:
            print("Unsupported file type.")

    def get_text(self):
        """
        Returns the extracted text from the file.

        :return: The extracted text.
        """
        return self.text

    def __determine_file_type(self):
        """
        Determines the file type by checking the file extension.

        :return: The file extension.
        """
        _, extension = os.path.splitext(self.file_path)
        return extension

    def __print_result(self, text):
        """
        Prints the extracted text from the file.

        :param text: The extracted text.
        """
        print("The file is readable. Here is the extracted text:")
        print(text)

    def __print_error(self):
        """
        Prints an error message indicating that the file is not readable or text could not be extracted.
        """
        print("The file is not readable or text could not be extracted.")