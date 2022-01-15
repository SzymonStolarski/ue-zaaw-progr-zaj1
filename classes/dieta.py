class Dieta:
    """
    Klasa zawierajaca informacje o diecie
    """
    def __init__(self, id_diety: int, nazwa_diety: str,
                 cena: float, kalorycznosc: int) -> None:

        self.__id_diety = id_diety
        self.__nazwa_diety = nazwa_diety
        self.__cena = cena
        self.__kalorycznosc = kalorycznosc

    @property
    def id_diety(self) -> int:
        return self.__id_diety

    @property
    def nazwa_diety(self) -> str:
        return self.__nazwa_diety

    @property
    def cena(self) -> float:
        return self.__cena

    @property
    def kalorycznosc(self) -> int:
        return self.__kalorycznosc

    def __str__(self) -> str:
        return f'Informacje o diecie: {self.__dict__}'
