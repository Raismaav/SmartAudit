from datetime import datetime
import re

class Auditor:
    def __init__(self, data, date):
        if isinstance(data, str):
            self.text = data
            self.data_dict = None
        elif isinstance(data, dict):
            self.data_dict = data
            self.text = None
        else:
            raise ValueError("Invalid data type. Expected str or dict.")
        self.date = date

    def audit_values_in_text(self, check_dict):
        if not isinstance(check_dict, dict):
            raise ValueError("Parameter must be a dictionary.")
        if self.text is None:
            raise ValueError("Text data is not initialized.")
        results = []
        for key, value in check_dict.items():
            if key == "date":  # Special handling for the date entry.
                new_date = self.__convert_date_format(self.date)
                if value in self.date or value in new_date:
                    results.append(True)
                else:
                    results.append(False)
            else:  # Verification for text entries.
                results.append(self.__verify_entry(value))
        return results

    def __verify_entry(self, entry):
        """
        Verifies if the entry is a complete word in the given text.

        Parameters:
            entry (str): The entry to be verified.

        Returns:
            bool: True if the entry is found as a complete word in the text, False otherwise.
        """
        if not entry:  # Check for empty string
            return False
        # Adjust the pattern to handle special characters and spaces
        pattern = r'\b' + re.escape(entry) + r'\b'
        return bool(re.search(pattern, self.text, re.IGNORECASE))

    @staticmethod
    def __convert_date_format(date):
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