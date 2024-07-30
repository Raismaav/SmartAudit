import tkinter as tk
from Auditor import Auditor

class DebugView:
    """
    A class to create and manage the GUI for debugging audits.

    This class is responsible for setting up the user interface, which includes input fields for user data,
    labels for each input field, and check buttons to indicate the verification status of each input.
    It dynamically creates the UI elements based on the provided labels.

    Attributes:
        verify_function (function): A callback function to be called when the "Verify" button is clicked.
        label_texts (list of str): A list of labels for the input fields.
        entry_widgets (list of tkinter.Entry): A list to store the entry widgets created for user inputs.
        check_widgets (list of tkinter.Checkbutton): A list to store the check buttons corresponding to each entry widget.
    """

    def __init__(self, label_texts, auditor: Auditor):
        """
        Initializes the DebugView with a verification function and a list of label texts.

        Parameters:
            verify_function (function): The function to call for verification.
            label_texts (list of str): The texts for the labels of the input fields.
        """

        self.label_texts = label_texts  # Store label_texts as an instance variable
        self.entry_widgets = []
        self.scan_widgets = []
        self.check_widgets = []
        self.auditor = auditor
        self.setup_ui()

    def __verify_and_mark(self):
        """
        Creates a dictionary pairing label texts with their corresponding entry widget values.
        """
        entries = {label: entry.get() for label, entry in zip(self.label_texts, self.entry_widgets)}
        results = self.auditor.audit_values_in_text(entries)
        for index, result in enumerate(results):
            if result:
                self.check_widgets[index].select()
            else:
                self.check_widgets[index].deselect()


    def center_window(self, window, width, height):
        """
        Centers the window on the screen.

        Parameters:
            window (tk.Tk): The window to be centered.
            width (int): The width of the window.
            height (int): The height of the window.
        """
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def setup_ui(self):
        """
        Sets up the user interface for the DebugView window.

        This method initializes the main window and its components, including labels, entry fields, and checkbuttons
        for each label text provided. It also configures the window's appearance and layout.
        """
        forms = tk.Tk()
        forms.title("Auditoría de remesas")
        preferred_width = 610
        preferred_height = 760
        forms.rowconfigure(0, weight=1)
        forms.columnconfigure(0, weight=1)
        self.center_window(forms, preferred_width, preferred_height)

        background_color = "#ececec"
        background_color_frame = "#ff6b00"
        input_background = "#ffffff"
        font_button = ("Arial", 11)
        font = ("Arial", 11)

        # Create header frame
        header_frame = tk.Frame(forms, bg=background_color_frame)
        header_frame.grid(row=0, column=0, sticky="new")
        header_frame.columnconfigure([0, 1, 2, 3], weight=1)

        reference_label = tk.Label(header_frame, text="Referencia", bg=background_color_frame, fg="white", font=font)
        reference_label.grid(row=0, column=0, sticky="ew", padx=10)
        reference = tk.Entry(header_frame, bg=input_background, font=font)
        reference.grid(row=0, column=1, sticky="ew", padx=10)

        search = tk.Button(header_frame, text="Buscar", width=10, font=font_button)
        search.grid(row=0, column=2, sticky="ew", padx=10)

        verify_button = tk.Button(header_frame, text="Verificar", width=20, height=1, command=self.__verify_and_mark,
                                  font=font_button)
        verify_button.grid(row=0, column=3, sticky="ew", padx=10, pady=10)


        for index, text in enumerate(self.label_texts):
            frame_window = tk.Frame(forms, bg=background_color)
            frame_window.grid(row=index + 1, column=0, sticky="ew", padx=5, pady=5)
            frame_window.columnconfigure(1, weight=1)
            label = tk.Label(frame_window, width=16, text=text, font=font)
            label.grid(row=0, column=0, sticky="w")
            entry = tk.Entry(frame_window, width=32, bg=input_background, font=font)
            entry.grid(row=0, column=1, sticky="ew")
            self.entry_widgets.append(entry)
            scan = tk.Entry(frame_window, width=32, bg=input_background, font=font)
            scan.grid(row=0, column=2, sticky="ew")
            self.scan_widgets.append(scan)
            check = tk.Checkbutton(frame_window, state=tk.DISABLED, bg=background_color)
            check.grid(row=0, column=3, sticky="e")
            self.check_widgets.append(check)

        forms.mainloop()
