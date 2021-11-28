from classes.pojazd import Pojazd


class Firma:
    """
    Klasa zawierajaca informacje o firmie.
    """
    def __init__(self, nazwa: str, miasto: str, telefon: int) -> None:
        self.__nazwa = nazwa
        self.__miasto = miasto
        self.__telefon = telefon

    @property
    def nazwa(self) -> str:
        return self.__nazwa

    @property
    def miasto(self) -> str:
        return self.__miasto

    @property
    def telefon(self) -> int:
        return self.__telefon

    def __str__(self) -> str:
        return f'Informacje o firmie: {self.__dict__}'


class FirmaTransportowa(Firma):
    """
    Klasa zawierajaca informacje o firmie transportowej.
    Dziedziczy po klasie bazowej Firma.
    """
    def __init__(self, nazwa: str, miasto: str, telefon: int,
                 ilosc_floty: int, pojazdy: list[Pojazd]) -> None:
        super().__init__(nazwa, miasto, telefon)
        self.__ilosc_floty = ilosc_floty
        self.__pojazdy = pojazdy

    @property
    def ilosc_floty(self) -> int:
        return self.__ilosc_floty

    @property
    def pojazdy(self) -> str:
        return self.__pojazdy

    def __str__(self) -> str:
        return f'Informacja o firmie transportowej: {self.__dict__}'


class FirmaSpozywcza(Firma):
    """
    Klasa zawierajaca informacje o firmie spozywczej.
    Dziedziczy po klasie bazowej Firma.
    """
    def __init__(self, nazwa: str, miasto: str, telefon: int,
                 rodzaj_produktow: str, firma_sieciowa: bool) -> None:
        super().__init__(nazwa, miasto, telefon)
        self.__rodzaj_produktow = rodzaj_produktow
        self.__firma_sieciowa = firma_sieciowa

    @property
    def rodzaj_produktow(self) -> str:
        return self.__rodzaj_produktow

    @property
    def firma_sieciowa(self) -> bool:
        return self.__firma_sieciowa

    def __str__(self) -> str:
        return f'Informacja o firmie spozywczej: {self.__dict__}'
