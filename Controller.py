from DebugView import DebugView
from DebugAudit import DebugAudit
from DataReader import DataReader


label_texts = [
"Fecha de presentación",
    "Cliente",
    "Domicilio",
    "Ciudad",
    "Estado",
    "RFC",
    "Guia",
    "Factura"
]

file_path = 'files/factura.pdf'
reader = DataReader(file_path)
reader.process_file()
debug_audit = DebugAudit(reader.get_text(), reader.get_date())
debug_view = DebugView(label_texts, debug_audit)
