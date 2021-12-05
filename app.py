from flask import Flask
from flask_restful import Resource, Api
from endpoints.movies_endpoint import Movies
from endpoints.tags_endpoint import Tags
from endpoints.rating_endpoint import Ratings
from endpoints.links_endpoint import Links


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
api.add_resource(Movies, '/movies')
api.add_resource(Links, '/links')
api.add_resource(Ratings, '/ratings')
api.add_resource(Tags, '/tags')

if __name__ == '__main__':
    app.run(debug=True)
