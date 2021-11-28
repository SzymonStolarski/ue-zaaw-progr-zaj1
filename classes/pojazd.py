class Pojazd:
    """
    Klasa zawierajaca informacje o pojezdzie.
    """
    def __init__(self, marka: str, model: str, rocznik: int,
                 przebieg: int, pojemnosc_silnika: float) -> None:

        self.__marka = marka
        self.__model = model
        self.__rocznik = rocznik
        self.__przebieg = przebieg
        self.__pojemnosc_silnika = pojemnosc_silnika

    @property
    def marka(self) -> str:
        return self.__marka

    @property
    def model(self) -> str:
        return self.__model

    @property
    def rocznik(self) -> int:
        return self.__rocznik

    @property
    def przebieg(self) -> int:
        return self.__przebieg

    @property
    def pojemnosc_silnika(self) -> float:
        return self.__pojemnosc_silnika

    def __str__(self) -> str:
        return f'Informacje o pojeździe: {self.__dict__}'
