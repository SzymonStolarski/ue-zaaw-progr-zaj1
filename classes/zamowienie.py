from classes.osoba import *
from classes.dieta import Dieta


class Zamowienie:
    """
    Klasa zawierajaca informacje o zamowieniu diety
    """
    def __init__(self) -> None:
        self.__pacjent = None
        self.__dietetyk = None
        self.__diety = None
        self.__data_zamowienia = None

    @property
    def pacjent(self) -> Pacjent:
        return self.__pacjent

    @pacjent.setter
    def pacjent(self, value) -> None:
        self.__pacjent = value

    @property
    def dietetyk(self) -> Dietetyk:
        return self.__dietetyk

    @dietetyk.setter
    def dietetyk(self, value) -> None:
        self.__dietetyk = value

    @property
    def diety(self) -> list[Dieta]:
        return self.__diety

    @diety.setter
    def diety(self, value) -> None:
        self.__diety = value

    @property
    def data_zamowienia(self) -> str:
        return self.__data_zamowienia

    @data_zamowienia.setter
    def data_zamowienia(self, value) -> None:
        self.__data_zamowienia = value

    def __str__(self) -> str:
        return f'Informacje o zamowieniu: {self.__dict__}'

    def oblicz_wartosc_zamowienia(self):
        """Metoda zwracajaca calkowita wartosc zamowienia"""
        return sum([round(dieta.cena, 2) for dieta in self.__diety])

    def oblicz_kalorycznosc_zamowienia(self):
        """Metoda zawierajaca calkowita kalorycznosc diety"""
        return sum([dieta.kalorycznosc for dieta in self.__diety])
