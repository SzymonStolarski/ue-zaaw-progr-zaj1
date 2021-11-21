class Property:
    def __init__(self, area: str, rooms: int, price: float,
                 adress: str) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.adress = adress


class House(Property):
    def __init__(self, area: str, rooms: int, price: float, adress: str,
                 plot: int) -> None:
        super().__init__(area, rooms, price, adress)
        self.plot = plot

    def __str__(self) -> str:
        return f"This is a house located in {self.area}. \
                 Price: {self.price}, Rooms: {self.rooms}, \
                 Adress: {self.adress}, Plot: {self.plot}"


class Flat(Property):
    def __init__(self, area: str, rooms: int, price: float, adress: str,
                 floor: int) -> None:
        super().__init__(area, rooms, price, adress)
        self.floor = floor

    def __str__(self) -> str:
        return f"This is a flat located in {self.area}. \
                 Price: {self.price}, Rooms: {self.rooms}, \
                 Adress: {self.adress}, Floor: {self.floor}"
