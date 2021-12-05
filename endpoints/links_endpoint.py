from flask import Flask
from flask_restful import Resource
from data.data_connector.csv_data_connector import CSVDataConnector
from data.data_models.link import Link


class Links(Resource):
    def get(self) -> list[dict]:
        data = CSVDataConnector(r'data/input_data/links.csv').load_data()
        list_of_links = []
        for i in data:
            list_of_links.append(Link(**i))

        return [serialized_obj.__dict__ for serialized_obj in list_of_links]
