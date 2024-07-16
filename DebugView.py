# Importamos las librerías necesarias
import tkinter as tk
from datetime import datetime

# Definimos las variables globales
entry_widgets = []
check_widgets = []
label_texts = [
        "Fecha de presentación",
        "Cliente",
        "Domicilio",
        "Ciudad",
        "Estado",
        "RFC",
        "Guia",
        "Piezas",
        "Factura"
    ]


# Definimos una función para centrar la ventana
def center_window(window, weight, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (weight // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{weight}x{height}+{x}+{y}")


# Definimos una función para mostrar la ventana de depuración
def debug_window(text="", date=""):
    global text_info, date_info
    text_info = text
    date_info = date
    # Definimos una ventana de tkinter
    forms = tk.Tk()
    # Definimos el título de la ventana y las dimensiones
    forms.title("Auditoría de remesas")
    prefered_width = 610
    prefered_height = 320
    # Configuramos la responsividad de la ventana y la centramos
    forms.rowconfigure(0, weight=1)
    forms.columnconfigure(0, weight=1)
    center_window(forms, prefered_width, prefered_height)
    # Esquema de colores y fuentes
    background_color = "#ececec"
    background_color_frame = "#ff6b00"
    input_background = "#ffffff"
    font_button = ("Arial", 11)
    font = ("Arial", 11)
    # Configuramos el color de fondo de la ventana
    forms.configure(bg=background_color)
    # Definimos un frame para colocar el botón de verificación
    frame = tk.Frame(forms, bg=background_color_frame)
    frame.config(height=60)
    frame.grid(row=0, sticky="ew")
    frame.columnconfigure(0, weight=1)
    # Definimos un array con los textos de las etiquetas

    # Iteramos sobre los textos de las etiquetas para colocarlas en la ventana
    for index, text in enumerate(label_texts):
        frame_window = tk.Frame(forms, bg=background_color)
        frame_window.grid(row=index + 1, column=0, sticky="ew", padx=5, pady=5)
        frame_window.columnconfigure(1, weight=1)
        label = tk.Label(frame_window, text=text, font=font)
        label.grid(row=0, column=0, sticky="w")
        entry = tk.Entry(frame_window, width=50, bg=input_background, font=font)
        entry.grid(row=0, column=1, sticky="ew")
        entry_widgets.append(entry)
        check = tk.Checkbutton(frame_window, state=tk.DISABLED, bg=background_color)
        check.grid(row=0, column=2, sticky="e")
        check_widgets.append(check)
    # Definimos un label y un entry para la referencia
    reference_label = tk.Label(frame, text="Referencia", bg=background_color_frame, fg="white", font=font)
    reference_label.grid(row=0, column=0, sticky="ew", padx=10)
    reference = tk.Entry(frame, bg=input_background, font=font)
    reference.grid(row=0, column=1, sticky="ew", padx=10)
    # Definimos un botón para buscar
    search = tk.Button(frame, text="Buscar", width=10, font=font_button)
    search.grid(row=0, column=2, sticky="ew", padx=10)
    # Definimos un botón para verificar
    verify_button = tk.Button(frame, text="Verificar", width=20, height=1, command=verify_and_mark, font=font_button)
    verify_button.grid(row=0, column=3, sticky="ew", padx=10, pady=10)
    forms.mainloop()
