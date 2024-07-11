from PDFReader import PDFReader

# Reemplaza 'ruta/a/tu/archivo.pdf' con la ruta real a tu archivo PDF
pdf_reader = PDFReader('test.pdf')
texto = pdf_reader.read_pdf()
if pdf_reader.is_readable():
    print("El PDF es legible. Aquí está el texto:")
    print(texto)
else:
    print("El PDF no es legible.")