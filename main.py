# Importa librerias necesarias
import cv2
import pytesseract
import tkinter as tk
from tkinter import messagebox
import platform
import debug_interface
import re

# Configura el path de tesseract en Windows
if platform.system() == 'Windows':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Carga la imagen
image = cv2.imread('test_image.png')
# cv2.imshow('Image', image)
# cv2.waitKey(0)

# Convierte el espectro de colores de BGR a RGB y lo transforma a texto
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(image)
# print(text)

# Obtención de fecha
# Define el patrón de la fecha
date_pattern = '\d{2}/\d{2}/\d{4}'

# Encuentra todas las fechas en text
dates = re.findall(date_pattern, text)
for date in dates:
    print(date)
debug_interface.debug_window(text)

# def check_input():
#     input_text = entry.get()
#     if input_text in text:
#         messagebox.showinfo("Resultado", "Numero de factura correcto")
#     else:
#         messagebox.showinfo("Resultado", "Numero de factura incorrecto")
# root = tk.Tk()
# root.title("Verificador de factura")
# entry = tk.Entry(root)
# entry.pack()
# button = tk.Button(root, text="Verificar", command=check_input)
# button.pack()
# root.mainloop()
