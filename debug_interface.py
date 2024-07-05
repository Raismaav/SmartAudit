# Importamos las librerías necesarias
import tkinter as tk
from datetime import datetime

# Definimos las variables globales
entry_widgets = []
check_widgets = []
text_info = ""
date_info = ""

# Definimos una función para centrar la ventana
def center_window(window, weight, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (weight // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{weight}x{height}+{x}+{y}")

# Definimos una función para verificar y marcar los elementos
def verify_and_mark():
    for index, entry_widget in enumerate(entry_widgets):
        entry_text = entry_widget.get()
        if entry_text:  # Verifica si la cadena no está vacía
            if index == 0:
                new_date = convert_date_format(date_info)
                print(new_date)
                if entry_text in date_info:
                    print(f"Found {entry_text}")
                    check_widgets[index].select()
                elif entry_text in new_date:
                    print(f"Found {new_date}")
                    check_widgets[index].select()
                else:
                    print(entry_text)
                    check_widgets[index].deselect()
                continue
            if entry_text in text_info:
                print(f"Found {entry_text}")
                check_widgets[index].select()
            else:
                print(f"Not found {entry_text}")
                check_widgets[index].deselect()

def convert_date_format(date):
    formats = ["%m/%d/%Y", "%d/%m/%Y", "%Y/%m/%d"]  # Agrega el nuevo formato a la lista
    for fmt in formats:
        try:
            date_object = datetime.strptime(date, fmt)
            new_date = date_object.strftime("%d/%m/%Y") if fmt == "%m/%d/%Y" else date_object.strftime("%m/%d/%Y")
            return new_date
        except ValueError:
            continue
    raise ValueError(f"La fecha {date} no coincide con ninguno de los formatos esperados.")

# Definimos una función para mostrar la ventana de depuración
def debug_window(text="", date=""):
    global text_info, date_info
    text_info = text
    date_info = date
    # Definimos una ventana de tkinter
    forms = tk.Tk()
    # Definimos el título de la ventana y las dimensiones
    forms.title("Auditoría de remesas")
    prefered_width = 600
    prefered_height = 300
    # Configuramos la responsividad de la ventana y la centramos
    forms.rowconfigure(0, weight=1)
    forms.columnconfigure(0, weight=1)
    center_window(forms, prefered_width, prefered_height)
    # Esquema de colores y fuentes
    background_color = "#ececec"
    background_color_frame = "#ff6b00"
    input_background = "#ffffff"
    button_color = "#0E63C2"
    font_button = ("Arial", 12, "bold")
    font = ("Arial", 11)
    # Configuramos el color de fondo de la ventana
    forms.configure(bg=background_color)
    # Definimos un frame para colocar el botón de verificación
    frame = tk.Frame(forms, bg=background_color_frame)
    frame.config(height=60)
    frame.grid(row=0, sticky="ew")
    frame.columnconfigure(0, weight=1)
    # Definimos un array con los textos de las etiquetas
    label_texts = [
        "Fecha de presentación",
        "Cliente",
        "Domicilio",
        "Ciudad/Edo",
        "RFC",
        "Guia",
        "Factura"
    ]
    # Iteramos sobre los textos de las etiquetas para colocarlas en la ventana
    for i, text in enumerate(label_texts):
        frame_window = tk.Frame(forms, bg=background_color)
        frame_window.grid(row=i + 1, column=0, sticky="ew", padx=5, pady=5)
        frame_window.columnconfigure(1, weight=1)
        label = tk.Label(frame_window, text=text, font=font)
        label.grid(row=0, column=0, sticky="w")
        entry = tk.Entry(frame_window, width=50, bg=input_background, font=font)
        entry.grid(row=0, column=1, sticky="ew")
        entry_widgets.append(entry)
        check = tk.Checkbutton(frame_window, state=tk.DISABLED, bg=background_color)
        check.grid(row=0, column=2, sticky="e")
        check_widgets.append(check)
    # Definimos un botón para verificar
    verify_button = tk.Button(frame, text="Verificar", width=20, height=1,
                              command=verify_and_mark, bg=button_color, font=font_button, fg="white")
    verify_button.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
    forms.mainloop()