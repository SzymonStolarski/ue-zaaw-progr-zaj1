from flask import Flask
from flask_restful import Resource
from data_connector.csv_data_connector import CSVDataConnector
from data_models.link import Link


class Links(Resource):
    def get(self):
        data = CSVDataConnector(r'endpoints/endpoints_data/links.csv').load_data()
        list_of_links = []
        for i in data:
            list_of_links.append(Link(**i))

        return [serialized_obj.__dict__ for serialized_obj in list_of_links]
