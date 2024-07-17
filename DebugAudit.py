from datetime import datetime


class DataAudit:
    def __init__(self, text_info, date_info):
        self.text_info = text_info
        self.date_info = date_info

    def verify_and_mark(self, entry_widgets, check_widgets):
        for index, entry_widget in enumerate(entry_widgets):
            entry_text = entry_widget.get().upper()
            print(entry_text)
            if entry_text:  # Verifica si la cadena no está vacía
                if index == 0:
                    new_date = self.convert_date_format(self.date_info)
                    print(new_date)
                    if entry_text in self.date_info:
                        print(f"Found {entry_text}")
                        check_widgets[index].select()
                    elif entry_text in new_date:
                        print(f"Found {new_date}")
                        check_widgets[index].select()
                    else:
                        print(entry_text)
                        check_widgets[index].deselect()
                    continue
                if entry_text in self.text_info:
                    print(f"Found {entry_text}")
                    check_widgets[index].select()
                else:
                    print(f"Not found {entry_text}")
                    check_widgets[index].deselect()

    @staticmethod
    def convert_date_format(date):
        formats = ["%m/%d/%Y", "%d/%m/%Y", "%Y/%m/%d"]
        for fmt in formats:
            try:
                date_object = datetime.strptime(date, fmt)
                new_date = date_object.strftime("%d/%m/%Y") if fmt == "%m/%d/%Y" else date_object.strftime("%m/%d/%Y")
                return new_date
            except ValueError:
                continue
        raise ValueError(f"La fecha {date} no coincide con ninguno de los formatos esperados.")
