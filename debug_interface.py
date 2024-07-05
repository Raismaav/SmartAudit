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
    forms = tk.Tk()
    predefined_width = 600
    predefined_height = 300
    forms.title("Auditoría de remesas")
    # Configuramos la responsividad de la ventana y la centramos
    forms.rowconfigure(0, weight=1)
    forms.columnconfigure(0, weight=1)
    center_window(forms, predefined_width, predefined_height)
    # Definimos un frame para colocar el botón de verificación
    frame = tk.Frame(forms)
    frame.config(width=predefined_width, height=60)
    frame.config(bg="#ff6b00")
    frame.pack(fill=tk.X)
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
    y_position = 70
    # Iteramos sobre los textos de las etiquetas para colocarlas en la ventana
    for text in label_texts:
        label = tk.Label(forms, text=text, font=("Arial", 11))
        label.place(x=10, y=y_position)
        entry = tk.Entry(forms, width=50)
        entry.place(x=200, y=y_position)
        entry_widgets.append(entry)
        check = tk.Checkbutton(forms, state=tk.DISABLED)
        check.place(x=500, y=y_position)
        check_widgets.append(check)
        y_position += 33
    # Definimos un botón para verificar
    verify_button = tk.Button(frame, text="Verificar", width=20, height=1, command=verify_and_mark)
    verify_button.place(x=430, y=17)
    forms.mainloop()