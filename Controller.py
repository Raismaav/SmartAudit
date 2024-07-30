from DebugView import DebugView
from Auditor import Auditor
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
        self.dict_texts = {
            "date": "Fecha de presentación",
            "client": "Cliente",
            "address": "Domicilio",
            "city": "Ciudad",
            "state": "Estado",
            "rfc": "RFC",
            "guide": "Guia",
            "invoice": "Factura",
            "postal_code": "Codigo postal",
            "supplier": "Proveedor",
            "part_number": "Numero de parte",
            "description": "Descripción",
            "quantity": "Cantidad",
            "measure": "medida",
            "fraction": "Fraccion",
            "unit_weight": "Peso unitario",
            "total_weight": "Peso total",
            "gross_weight": "Peso bruto",
            "unit_value": "Valor unitario",
            "total_value": "Valor total",
            "incoterm": "Incoterm"
        }

    def run(self):
        """
        Processes the data file and initializes the DebugView.
        """
        reader = DataReader(self.file_path)
        reader.process_file()
        auditor = Auditor(reader.get_text(), reader.get_date())
        DebugView(self.dict_texts, auditor)
