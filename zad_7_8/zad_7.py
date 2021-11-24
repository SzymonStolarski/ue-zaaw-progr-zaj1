from brewery.brewery_connector import *
from brewery.brewery import *


# zad 7 a)
brewery_connector_zad_7 = BreweryConnector().load()
brewery_list = []
for i in range(0, 20):
    brewery_list.append(Brewery(**brewery_connector_zad_7[i]))
print("ZAD 7a")
[print(brewery) for brewery in brewery_list]

# zad 7 b) would be nicer to have it in dictionary :)
brewery_dict = {}
for i in range(0, 20):
    brewery_dict[f'brewery_{i + 1}'] = Brewery(**brewery_connector_zad_7[i])
print("ZAD 7b")
[print(brewery, info) for brewery, info in brewery_dict.items()]
