from DebugView import DebugView
from DataReader import DataReader
# Ejemplo de cómo se usaría la clase

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


def verify_and_mark():
    print("Verificación y marcado")


debug_view = DebugView(verify_and_mark, label_texts)