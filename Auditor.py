from datetime import datetime
import re

class Auditor:
    """
    Auditor class for verifying text and date entries against provided data.

    Attributes:
        text (str): The text data to be audited.
        data_dict (dict): The dictionary data to be audited.
        date (str): The date to be used for verification.
    """

    def __init__(self, data, date):
        """
        Initializes the Auditor with data and a date.

        Parameters:
            data (str or dict): The data to be audited. Can be a string or a dictionary.
            date (str): The date to be used for verification.
        """
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
        """
        Audits the values in the provided dictionary against the text data.

        Parameters:
            check_dict (dict): The dictionary containing the values to be audited.

        Returns:
            list of bool: A list of boolean values indicating the audit results for each entry.
        """
        if not isinstance(check_dict, dict):
            raise ValueError("Parameter must be a dictionary.")
        if self.text is None:
            raise ValueError("Text data is not initialized.")
        results = []
        for key, value in check_dict.items():
            if key == "date":  # Special handling for the date entry.
                results.append(self.__verify_date(value))
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

    def __parse_date(self, date_str):
        """
        Parses the given date string into a datetime object.

        Parameters:
            date_str (str): The date string to be parsed.

        Returns:
            datetime: The parsed datetime object.

        Raises:
            ValueError: If the date string does not match any of the expected formats.
        """
        date_formats = [
            "%m/%d/%Y",  # MM/DD/YYYY
            "%d/%m/%Y",  # DD/MM/YYYY
            "%Y/%m/%d",  # YYYY/MM/DD
            "%d-%m-%Y",  # DD-MM-YYYY
            "%m-%d-%Y",  # MM-DD-YYYY
            "%Y-%m-%d",  # YYYY-MM-DD
            "%Y.%m.%d",  # YYYY.MM.DD
            "%B %d, %Y",  # Month DD, YYYY (e.g., May 13, 2024)
            "%d %B %Y",  # DD Month YYYY (e.g., 13 May 2024)
            "%d-%b-%Y",  # DD-Mon-YYYY (e.g., 13-May-2024)
            "%b %d, %Y",  # Mon DD, YYYY (e.g., May 13, 2024)
            "%d %b %y",  # DD Mon YY (e.g., 13 May 24)
            "%d/%m/%y",  # DD/MM/YY
            "%m/%d/%y",  # MM/DD/YY
        ]

        for date_format in date_formats:
            try:
                return datetime.strptime(date_str, date_format)
            except ValueError:
                continue

        raise ValueError(f"Formato de fecha no reconocido: {date_str}")

    def __verify_date(self, date):
        """
        Verifies if the given date matches the initialized date.

        Parameters:
            date (str): The date to be verified.

        Returns:
            bool: True if the dates match, False otherwise.
        """
        try:
            parsed_date = self.__parse_date(date)
            return self.__parse_date(self.date) == parsed_date
        except ValueError:
            return False
