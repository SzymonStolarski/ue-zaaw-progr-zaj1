class Student:
    """
    Class storing info about students - the main users of the library
    """
    def __init__(self, name: str, surname: str, pesel: int) -> None:
        self.name = name
        self.surname = surname
        self.pesel = pesel

    def __str__(self) -> str:
        return f'Student: {self.name} {self.surname}, pesel: {self.pesel}'
