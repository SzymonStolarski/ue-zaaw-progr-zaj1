from classes.firmy import *
from classes.odcinek import *
from classes.pojazd import *


class Kurs:
    """
    Klasa zawierajaca informacje o kursie
    """
    def __init__(self) -> None:
        self.__firma = None
        self.__odcinki = None
        self.__data_kursu = None
        self.__kierowca = None
        self.__czas_minuty = None
        self.__pojazd = None

    @property
    def firma(self) -> Firma:
        return self.__firma

    @firma.setter
    def firma(self, value) -> None:
        self.__firma = value

    @property
    def odcinki(self) -> list[Odcinek]:
        return self.__odcinki

    @odcinki.setter
    def odcinki(self, value) -> None:
        self.__odcinki = value

    @property
    def data_kursu(self) -> str:
        return self.__data_kursu

    @data_kursu.setter
    def data_kursu(self, value) -> None:
        self.__data_kursu = value

    @property
    def kierowca(self) -> str:
        return self.__kierowca

    @kierowca.setter
    def kierowca(self, value) -> None:
        self.__kierowca = value

    @property
    def czas_minuty(self) -> float:
        return self.__czas_minuty

    @czas_minuty.setter
    def czas_minuty(self, value) -> None:
        self.__czas_minuty = value

    @property
    def pojazd(self) -> float:
        return self.__pojazd

    @pojazd.setter
    def pojazd(self, value) -> None:
        self.__pojazd = value

    def __str__(self) -> str:
        return f'Informacje o kursie. {self.__dict__}'

    def oblicz_sume_kilometrow(self):
        return sum([odcinek.dlugosc for odcinek in self.__odcinki])

    def zwroc_marke_pojazdu(self):
        return self.__pojazd.marka
