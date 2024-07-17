from datetime import datetime


class DebugAudit:
    """
    A class to perform debugging audits by verifying text and date information against user inputs.

    Attributes:
        text_info (str): The text information to be verified.
        date_info (str): The date information to be verified in various formats.
    """

    def __init__(self, text_info, date_info):
        """
        Initializes the DebugAudit with text and date information.

        Parameters:
            text_info (str): The text information for the audit.
            date_info (str): The date information for the audit.
        """
        self.text_info = text_info
        self.date_info = date_info

    def verify_and_mark(self, entry_widgets, check_widgets):
        """
        Verifies each entry widget's text against the stored text and date information. Marks the corresponding check widget based on the verification result.

        Parameters:
            entry_widgets (list): A list of tkinter Entry widgets containing user inputs.
            check_widgets (list): A list of tkinter Checkbutton widgets to be marked based on verification.
        """
        for index, entry_widget in enumerate(entry_widgets):
            entry_text = entry_widget.get().upper()
            print(entry_text)
            if entry_text:  # Verifies if the string is not empty.
                if index == 0:  # Special handling for the date entry.
                    new_date = self.convert_date_format(self.date_info)
                    print(new_date)
                    if entry_text in self.date_info or entry_text in new_date:
                        print(f"Found {entry_text}")
                        check_widgets[index].select()
                    else:
                        print(entry_text)
                        check_widgets[index].deselect()
                    continue
                # Verification for text entries.
                if entry_text in self.text_info:
                    print(f"Found {entry_text}")
                    check_widgets[index].select()
                else:
                    print(f"Not found {entry_text}")
                    check_widgets[index].deselect()

    @staticmethod
    def convert_date_format(date):
        """
        Converts the given date into a different format based on predefined formats.

        Parameters:
            date (str): The date string to be converted.

        Returns:
            str: The date in a new format if conversion is successful.

        Raises:
            ValueError: If the date does not match any of the expected formats.
        """
        formats = ["%m/%d/%Y", "%d/%m/%Y", "%Y/%m/%d"]
        for fmt in formats:
            try:
                date_object = datetime.strptime(date, fmt)
                new_date = date_object.strftime("%d/%m/%Y") if fmt == "%m/%d/%Y" else date_object.strftime("%m/%d/%Y")
                return new_date
            except ValueError:
                continue
        raise ValueError(f"La fecha {date} no coincide con ninguno de los formatos esperados.")
