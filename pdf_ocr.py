# Importa librerias necesarias
from pdf2image import convert_from_path
import pytesseract
import tkinter as tk
from tkinter import messagebox

# Configura el path de tesseract
def pdf_to_img(pdf_file):
    return convert_from_path(pdf_file)

# Convierte el pdf a imagenes
def ocr_core(images):
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text

# Extrae el texto de las imagenes
images = pdf_to_img('factura.pdf')
text = ocr_core(images)
print(text)

# Verifica si el texto ingresado es correcto
def check_input():
    input_text = entry.get()
    if input_text in text:
        messagebox.showinfo("Resultado", "Numero de factura correcto")
    else:
        messagebox.showinfo("Resultado", "Numero de factura incorrecto")

# Crea la interfaz grafica
root = tk.Tk()
root.title("Verificador de factura")
# Crea los elementos de la interfaz
entry = tk.Entry(root)
entry.pack()
# Crea el boton de verificacion
button = tk.Button(root, text="Verificar", command=check_input)
button.pack()
# Inicia la interfaz grafica
root.mainloop()