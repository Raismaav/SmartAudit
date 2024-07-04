# Importa la librería PyPDF2 para leer archivos PDF
import PyPDF2

# Función para leer e imprimir texto de un archivo PDF
def read_pdf(file_path):
    try:
        # Abre el archivo PDF en modo lectura binaria
        with open(file_path, 'rb') as file:
            # Crea un objeto PdfFileReader
            reader = PyPDF2.PdfFileReader(file)
            # Itera sobre cada página y extrae el texto
            for page_num in range(reader.getNumPages()):
                page = reader.getPage(page_num)
                text = page.extract_text()
                print(f'--- Página {page_num + 1} ---')
                print(text)
                print()
    except Exception as e:
        print(f'Ocurrió un error: {e}')

# Ruta del archivo PDF
file_path = 'factura.pdf'
read_pdf(file_path)