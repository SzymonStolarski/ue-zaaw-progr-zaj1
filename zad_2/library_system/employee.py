class Employee:
    """
    Class containing info on employees from the libraries
    """
    def __init__(self, first_name: str, last_name: str,
                 hire_date: str, birth_date: str,
                 city: str, street: str, zip_code: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code

    def __str__(self) -> str:
        return f'Employee name {self.first_name} {self.last_name}, \
                 hired on {self.hire_date}, born on {self.birth_date}, \
                 city: {self.city}, street: {self.street}, \
                 zip-code: {self.zip_code}'
