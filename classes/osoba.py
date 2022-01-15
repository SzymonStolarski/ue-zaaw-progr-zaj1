class Osoba:
    """
    Klasa zawierajaca informacje o osobie
    """
    def __init__(self, imie: str, nazwisko: str,
                 telefon: int) -> None:
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__telefon = telefon

    @property
    def imie(self) -> str:
        return self.__imie

    @property
    def nazwisko(self) -> str:
        return self.__nazwisko

    @property
    def telefon(self) -> int:
        return self.__telefon

    def __str__(self) -> str:
        return f'Informacje o osobie {self.__dict__}'


class Pacjent(Osoba):
    """
    Klasa zawierajaca informacje o pacjencie zamawiajacym diete
    """
    def __init__(self, imie: str, nazwisko: str,
                 telefon: int, rok_urodzenia: int,
                 adres: str) -> None:
        super().__init__(imie, nazwisko, telefon)
        self.__rok_urodzenia = rok_urodzenia
        self.__adres = adres

    @property
    def rok_urodzenia(self) -> int:
        return self.__rok_urodzenia

    @property
    def adres(self) -> str:
        return self.__adres

    def __str__(self) -> str:
        return f'Informacje o Pacjencie {self.__dict__}'


class Dietetyk(Osoba):
    """
    Klasa zawierajaca informacje o dietetyku przygotowujacym diete
    """
    def __init__(self, imie: str, nazwisko: str, telefon: int,
                 specjalizacja: str, data_zatrudnienia: str) -> None:
        super().__init__(imie, nazwisko, telefon)
        self.__specjalizacja = specjalizacja
        self.__data_zatrudnienia = data_zatrudnienia

    @property
    def specjalizacja(self) -> str:
        return self.__specjalizacja

    @property
    def data_zatrudnienia(self) -> str:
        return self.__data_zatrudnienia

    def __str__(self) -> str:
        return f'Informacje o Dietetyku: {self.__dict__}'
