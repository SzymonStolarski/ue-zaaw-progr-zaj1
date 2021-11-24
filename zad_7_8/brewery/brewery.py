from datetime import datetime


class Brewery:
    """
    Brewerey class storing the info about a single brewery from the json
    """
    def __init__(self, id: str, name: str, brewery_type: str, street: str,
                 address_2: str, address_3, city: str, state: str,
                 county_province: str, postal_code: str, country: str,
                 longitude: str, latitude: str, phone: str,
                 website_url: str, updated_at: str,
                 created_at: str) -> None:

        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.county_province = county_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at
        self.created_at = created_at

    def __str__(self) -> str:
        return f'Brewery info: {self.__dict__}'
