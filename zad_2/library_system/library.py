class Library:
    """
    Class containing info about particular library
    """
    def __init__(self, city: str, street: str, zip_code: str,
                 open_hours: str, phone: str) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f'Library from {self.city}, located on {self.street}. \
                Zip-code: {self.zip_code}, opened: {self.open_hours}, \
                phone: {self.phone}'
