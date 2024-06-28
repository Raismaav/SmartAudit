import cv2
import pytesseract
import tkinter as tk
from tkinter import messagebox
import platform

if platform.system() == 'Windows':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread('test_image.png')
# cv2.imshow('Image', image)
# cv2.waitKey(0)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(image)
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
