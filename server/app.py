from config import app
from flask import make_response

from models import db, Restaurant, Food, FoodAtRestaurant

@app.route('/restaurants', methods = ['GET'])
def restaurants():
    restaurants = Restaurant.query.all()

    restaurants_dict = [restaurant.to_dict() for restaurant in restaurants]

    response = make_response(
        restaurants_dict,
        200
    )

    return response

@app.route('/foods', methods = ['GET'])
def foods():
    foods = Food.query.all()

    foods_dict = [food.to_dict() for food in foods]

    response = make_response(
        foods_dict,
        200
    )

    return response

@app.route('/restaurants_foods', methods = ['GET'])
def rfs():
    rfs = FoodAtRestaurant.query.all()

    rfs_dict = [rf.to_dict() for rf in rfs]

    response = make_response(
        rfs_dict,
        200
    )

    return response

if __name__ == '__main__':
    app.run(port = 5555, debug = True)