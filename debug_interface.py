# Importamos las librerías necesarias
import tkinter as tk

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
    print(text_info)
    for index, entry_widget in enumerate(entry_widgets):
        entry_text = entry_widget.get()
        if entry_text:  # Verifica si la cadena no está vacía
            if index == 0:
                if entry_text in date_info:
                    print(f"Found {entry_text}")
                    check_widgets[index].select()
                else:
                    print(entry_text)
                    check_widgets[index].deselect()
                continue
            if entry_text in text_info:
                print(f"Found {entry_text}")
                check_widgets[index].select()
            else:
                print(entry_text)
                check_widgets[index].deselect()

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