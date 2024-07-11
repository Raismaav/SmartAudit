import PyPDF2

class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = None

    def read_pdf(self):
        """Lee y extrae el texto de un archivo PDF."""
        try:
            with open(self.file_path, 'rb') as file:
                reader = PyPDF2.PdfFileReader(file)
                self.text = ""
                for page_num in range(reader.getNumPages()):
                    page = reader.getPage(page_num)
                    page_text = page.extract_text()
                    if page_text:
                        self.text += page_text + "\n"
                return self.text.upper()
        except Exception as e:
            print(f'Ocurrió un error: {e}')
            return None

    def is_readable(self):
        """Verifica si el PDF es legible."""
        return bool(self.text)