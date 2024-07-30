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

        return [value in self.text for value in check_dict.values()]