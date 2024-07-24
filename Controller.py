from DebugView import DebugView
from DebugAudit import DebugAudit
from DataReader import DataReader


class Controller:
    """
    Controller class to manage the application flow.

    This class is responsible for initializing the application components,
    processing the data file, and setting up the DebugView with the processed data.

    Attributes:
        file_path (str): The path to the data file to be processed.
        label_texts (list of str): Labels for the input fields in the DebugView.
    """

    def __init__(self, file_path=None):
        """
        Initializes the Controller with the file path.

        Parameters:
            file_path (str, optional): The path to the data file. Defaults to None.
        """
        self.file_path = file_path
        self.label_texts = [
            "Fecha de presentación",
            "Cliente",
            "Domicilio",
            "Ciudad",
            "Estado",
            "RFC",
            "Guia",
            "Factura",
            "Codigo postal",
            "Proveedor",
            "Numero de parte",
            "Descripción",
            "Cantidad",
            "medida",
            "Fraccion",
            "Peso unitario",
            "Peso total",
            "Peso bruto",
            "Valor unitario",
            "Valor total",
            "Incoterm"
        ]

    def run(self):
        """
        Processes the data file and initializes the DebugView.
        """
        reader = DataReader(self.file_path)
        reader.process_file()
        debug_audit = DebugAudit(reader.get_text(), reader.get_date())
        DebugView(self.label_texts, debug_audit)
