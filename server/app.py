from config import app
from flask import make_response, request
from flask_restful import Api, Resource

from models import db, Restaurant, Food, FoodAtRestaurant

if __name__ == '__main__':
    app.run(port = 5555, debug = True)