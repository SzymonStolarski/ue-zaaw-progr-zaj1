class Odcinek:
    """
    Klasa zawierajaca informacje o pojedynczym odcinku kursu.
    """
    def __init__(self, miejscowosc_od: str, miejscowosc_do: str,
                 dlugosc: float, odcinek_platny: bool,
                 autostrada: bool) -> None:

        self.__miejscowosc_od = miejscowosc_od
        self.__miejscowosc_do = miejscowosc_do
        self.__dlugosc = dlugosc
        self.__odcinek_platny = odcinek_platny
        self.__autostrada = autostrada

    @property
    def miejscowosc_od(self) -> str:
        return self.__miejscowosc_od

    @property
    def miejscowosc_do(self) -> str:
        return self.__miejscowosc_do

    @property
    def dlugosc(self) -> float:
        return self.__dlugosc

    @property
    def odcinek_platny(self) -> bool:
        return self.__odcinek_platny

    @property
    def autostrada(self) -> bool:
        return self.__autostrada
