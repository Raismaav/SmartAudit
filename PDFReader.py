import PyPDF2

class PDFReader:
    """
    A class to read and extract text from PDF files.

    Attributes:
        file_path (str): The path to the PDF file to be read.
        text (str): Extracted text from the PDF file.
    """

    def __init__(self, file_path):
        """
        Initializes the PDFReader with a path to a PDF file.

        :param file_path: Path to the PDF file.
        """
        self.file_path = file_path
        self.text = None

    def read_pdf(self):
        """
        Reads and extracts text from the PDF file specified in the file_path attribute.

        :return: The extracted text in uppercase if successful, None otherwise.
        """
        if self.is_encrypted():
            print("PDF is encrypted. Unable to read without a password.")
            return None

        try:
            with open(self.file_path, 'rb') as file:
                reader = PyPDF2.PdfFileReader(file)
                self.text = self.extract_text(reader)
                return self.text.upper()
        except Exception as e:
            print(f'An error occurred: {e}')
            return None

    def is_encrypted(self):
        """
        Checks if the PDF file is encrypted.

        :return: True if the file is encrypted, False otherwise.
        """
        with open(self.file_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            return reader.isEncrypted

    def extract_text(self, reader):
        """
        Extracts text from all pages of the PDF file.

        :param reader: A PyPDF2.PdfFileReader object of the PDF file.
        :return: Extracted text as a string.
        """
        text = ""
        for page_num in range(reader.getNumPages()):
            page = reader.getPage(page_num)
            page_text = page.extractText()
            if page_text:
                text += page_text + "\n"
        return text

    def is_readable(self):
        """
        Verifies if the PDF file is readable by checking if text was extracted.

        :return: True if text was extracted, False otherwise.
        """
        return bool(self.text)