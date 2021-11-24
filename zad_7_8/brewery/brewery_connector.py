import urllib.request
import json


class BreweryConnector:
    """
    BreweryConnector object that connects to the openbrewerydb API and gets
    the data from the json file to a list of dictionaries. Additionally,
    the data can be filtered on name, city, state or country.
    """
    # TODO: filtering via the api, not on the machine
    BREWERY_API = "https://api.openbrewerydb.org/breweries"

    def __init__(self, name: str = None, city: str = None,
                 state: str = None, country: str = None) -> None:
        self.name = name
        self.country = country
        self.state = state
        self.city = city

    def load(self) -> list:
        with urllib.request.urlopen(BreweryConnector.BREWERY_API) as url:
            data = json.loads(url.read().decode())
        data_copy = data.copy()

        # Select parameters that were passed during in the constructor and
        # filter the data based on the not empty parameters
        filter_parameters = {key: value for (key, value)
                             in self.__dict__.items() if value is not None}
        if filter_parameters:
            for key, value in filter_parameters.items():
                data_copy = [item for item in data_copy if item[key] == value]

        return data_copy
