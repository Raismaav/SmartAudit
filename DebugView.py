import tkinter as tk


class DebugView:
    def __init__(self, verify_function, label_texts):
        self.verify_function = verify_function
        self.label_texts = label_texts  # Guardar label_texts como variable de instancia
        self.entry_widgets = []
        self.check_widgets = []
        self.setup_ui()

    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def setup_ui(self):
        forms = tk.Tk()
        forms.title("Auditoría de remesas")
        preferred_width = 610
        preferred_height = 320
        forms.rowconfigure(0, weight=1)
        forms.columnconfigure(0, weight=1)
        self.center_window(forms, preferred_width, preferred_height)

        background_color = "#ececec"
        background_color_frame = "#ff6b00"
        input_background = "#ffffff"
        font_button = ("Arial", 11)
        font = ("Arial", 11)

        forms.configure(bg=background_color)
        frame = tk.Frame(forms, bg=background_color_frame)
        frame.config(height=60)
        frame.grid(row=0, sticky="ew")
        frame.columnconfigure(0, weight=1)

        # Utilizar self.label_texts aquí
        for index, text in enumerate(self.label_texts):
            frame_window = tk.Frame(forms, bg=background_color)
            frame_window.grid(row=index + 1, column=0, sticky="ew", padx=5, pady=5)
            frame_window.columnconfigure(1, weight=1)
            label = tk.Label(frame_window, text=text, font=font)
            label.grid(row=0, column=0, sticky="w")
            entry = tk.Entry(frame_window, width=50, bg=input_background, font=font)
            entry.grid(row=0, column=1, sticky="ew")
            self.entry_widgets.append(entry)
            check = tk.Checkbutton(frame_window, state=tk.DISABLED, bg=background_color)
            check.grid(row=0, column=2, sticky="e")
            self.check_widgets.append(check)

        reference_label = tk.Label(frame, text="Referencia", bg=background_color_frame, fg="white", font=font)
        reference_label.grid(row=0, column=0, sticky="ew", padx=10)
        reference = tk.Entry(frame, bg=input_background, font=font)
        reference.grid(row=0, column=1, sticky="ew", padx=10)

        search = tk.Button(frame, text="Buscar", width=10, font=font_button)
        search.grid(row=0, column=2, sticky="ew", padx=10)

        verify_button = tk.Button(frame, text="Verificar", width=20, height=1, command=self.verify_function, font=font_button)
        verify_button.grid(row=0, column=3, sticky="ew", padx=10, pady=10)

        forms.mainloop()



