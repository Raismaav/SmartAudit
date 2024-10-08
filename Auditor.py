from datetime import datetime
from DataReader import DataReader
import re

class Auditor:
    """
    Auditor class for verifying text and date entries against provided data.

    Attributes:
        text (str): The text data to be audited.
        date (str): The date to be used for verification.
    """

    def __init__(self, data=None, date=None, file_path=None):
        """
        Initializes the Auditor with data and a date or a file path.

        Parameters:
            data (str, optional): The data to be audited. Can be a string or a dictionary.
            date (str, optional): The date to be used for verification.
            file_path (str, optional): The path to the file containing the data and date.
        """
        self.search_results = {}

        if file_path:
            reader = DataReader(file_path)
            self.text = reader.get_text()
            self.date = reader.get_date()
        elif data and date:
            if isinstance(data, str):
                self.text = data
            else:
                raise ValueError("Invalid data type. Expected str")
            self.date = date
        else:
            raise ValueError("Either file_path or both data and date must be provided")

    def audit_values_in_dict(self, check_dict, correct_dict):
        """
        Audits the values in the provided dictionary against the correct values dictionary.

        Parameters:
            check_dict (dict): The dictionary containing the values to be audited. The keys should be the names of the
            entries, and the values should be the entries to be verified.
            correct_dict (dict): The dictionary containing the correct values. The keys should be the same as in check_dict.

        Returns:
            dict: A dictionary with the same keys as `check_dict`, where the values are boolean indicating the audit
            results for each entry. True if the entry matches the correct value, False otherwise.

        Raises:
            ValueError: If `check_dict` or `correct_dict` is not a dictionary.
        """
        if not isinstance(check_dict, dict) or not isinstance(correct_dict, dict):
            raise ValueError("Both parameters must be dictionaries.")

        results = {}
        for key, value in check_dict.items():
            if key == "date":  # Special handling for the date entry.
                results[key] = self.__verify_date(value, key, correcte_date=correct_dict[key])
            else:  # Verification for text entries.
                results[key] = self.__verify_entry(value, key, text=correct_dict[key])

        return results

    def audit_values_in_text(self, check_dict):
        """
        Audits the values in the provided dictionary against the text data.

        Parameters:
            check_dict (dict): The dictionary containing the values to be audited. The keys should be the names of the
            entries, and the values should be the entries to be verified.

        Returns:
            dict: A dictionary with the same keys as `check_dict`, where the values are boolean indicating the audit
            results for each entry. True if the entry is found as a complete word in the text or if the date matches,
            False otherwise.

        Raises:
            ValueError: If `check_dict` is not a dictionary or if the text data is not initialized.
        """
        if not isinstance(check_dict, dict):
            raise ValueError("Parameter must be a dictionary.")
        if self.text is None:
            raise ValueError("Text data is not initialized.")
        results = {}
        for key, value in check_dict.items():
            if key == "date":  # Special handling for the date entry.
                results[key] = self.__verify_date(value, key)
            else:  # Verification for text entries.
                results[key] = self.__verify_entry(value, key)

        return results

    def __verify_entry(self, entry, key, text=None):
        """
        Verifies if the entry is a complete word in the given text and prints the closest complete word.

        Parameters:
            entry (str): The entry to be verified.
            key (str): The key associated with the entry.
            text (str, optional): The text to be used for verification. If not provided, uses the initialized text.

        Returns:
            bool: True if the entry is found as a complete word in the text, False otherwise.
        """
        if not text:
            text = self.text

        if not entry or len(entry) == 1:  # Check for empty string or single character
            self.search_results[key] = 'No matches found'
            return False

        # Find all words in the text
        words = re.findall(r'\b[\w\.\-]+\b', text.upper())

        # Find the closest match
        closest_word = None
        min_distance = float('inf')
        for word in words:
            distance = self.__levenshtein_distance(entry.upper(), word)
            if distance < min_distance:
                min_distance = distance
                closest_word = word

        # Print the closest word
        if closest_word:
            self.search_results[key] = closest_word
        else:
            self.search_results[key] = 'No matches found'

        # Check if the entry is a complete word in the text
        pattern = r'(?<!\w)' + re.escape(entry) + r'(?!\w)'
        match = re.search(pattern, text.upper(), re.IGNORECASE)
        if match:
            self.search_results[key] = match.group(0)
            return True
        else:
            return False

    def __levenshtein_distance(self, s1, s2):
        """
        Computes the Levenshtein distance between two strings.

        Parameters:
            s1 (str): The first string.
            s2 (str): The second string.

        Returns:
            int: The Levenshtein distance between the two strings.
        """
        if len(s1) < len(s2):
            return self.__levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def __verify_date(self, date, key, correct_date=None):
        """
        Verifies if the given date matches the initialized date.

        Parameters:
            date (str): The date to be verified.

        Returns:
            bool: True if the dates match, False otherwise.
        """
        if not correct_date:
            correct_date = self.date
        try:
            parsed_date = self.__parse_date(date)
            self.search_results[key] = correct_date
            return self.__parse_date(correct_date) == parsed_date
        except ValueError:
            self.search_results[key] = 'No matches found'
            return False

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
            "%b %d %Y",  # Mon DD, YYYY (e.g., May 13 2024)
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
