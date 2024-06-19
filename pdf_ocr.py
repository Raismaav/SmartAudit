from pdf2image import convert_from_path
import pytesseract
import tkinter as tk
from tkinter import messagebox

def pdf_to_img(pdf_file):
    return convert_from_path(pdf_file)

def ocr_core(images):
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text

images = pdf_to_img('factura.pdf')
text = ocr_core(images)
print(text)

def check_input():
    input_text = entry.get()
    if input_text in text:
        messagebox.showinfo("Resultado", "Numero de factura correcto")
    else:
        messagebox.showinfo("Resultado", "Numero de factura incorrecto")

root = tk.Tk()
root.title("Verificador de factura")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Verificar", command=check_input)
button.pack()
root.mainloop()