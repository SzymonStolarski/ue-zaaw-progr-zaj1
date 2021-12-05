from flask import Flask
from flask_restful import Resource
from data_connector.csv_data_connector import CSVDataConnector
from data_models.movie import Movie


class Movies(Resource):
    def get(self):
        data = CSVDataConnector(r'endpoints/endpoints_data/movies.csv').load_data()
        list_of_movies = []
        for i in data:
            list_of_movies.append(Movie(**i))

        return [serialized_obj.__dict__ for serialized_obj in list_of_movies]
