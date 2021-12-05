from flask import Flask
from flask_restful import Resource
from data_connector.csv_data_connector import CSVDataConnector
from data_models.tag import Tag


class Tags(Resource):
    def get(self):
        data = CSVDataConnector(r'endpoints/endpoints_data/tags.csv').load_data()
        list_of_tags = []
        for i in data:
            list_of_tags.append(Tag(**i))

        return [serialized_obj.__dict__ for serialized_obj in list_of_tags]
