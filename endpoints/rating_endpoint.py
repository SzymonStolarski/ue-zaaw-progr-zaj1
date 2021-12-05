from flask import Flask
from flask_restful import Resource
from data_connector.csv_data_connector import CSVDataConnector
from data_models.rating import Rating


class Ratings(Resource):
    def get(self):
        data = CSVDataConnector(r'endpoints/endpoints_data/ratings.csv').load_data()
        list_of_ratings = []
        for i in data:
            list_of_ratings.append(Rating(**i))

        return [serialized_obj.__dict__ for serialized_obj in list_of_ratings]
