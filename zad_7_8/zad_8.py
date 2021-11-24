import argparse
from brewery.brewery_connector import *
from brewery.brewery import *

# Added some additional filtering options
parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Filter based on name",
                    type=str, required=False)
parser.add_argument("--city", help="Filter based on city",
                    type=str, required=False)
parser.add_argument("--state", help="Filter based on state",
                    type=str, required=False)
parser.add_argument("--country", help="Filter based on country",
                    type=str, required=False)
args = parser.parse_args()

brewery_connector_zad_8 = BreweryConnector(name=args.name, city=args.city,
                                           state=args.state,
                                           country=args.country).load()
brewery_dict = {}
# This loop needed to change compared to zad 7
# I cannot take first 20 observations anymore as there is not that much data
for i in range(0, len(brewery_connector_zad_8)):
    brewery_dict[f'brewery_{i + 1}'] = Brewery(**brewery_connector_zad_8[i])
print("ZAD 7b")
[print(brewery, info) for brewery, info in brewery_dict.items()]
