from config import app
from flask import make_response, request
from flask_restful import Api, Resource

from models import db, Restaurant, Food, FoodAtRestaurant

api = Api(app) # necessary if using Flask-RESTful library

@app.route('/restaurants', methods = ['GET']) # establishes endpoint and methods
def restaurants():
    restaurants = Restaurant.query.all() # grab objects from DB

    restaurants_dict = [restaurant.to_dict() for restaurant in restaurants] # turn each object into dictionary

    # response includes response body of API and HTTPS status code
    response = make_response(
        restaurants_dict,
        200
    )

    return response

@app.route('/foods', methods = ['GET'])
def foods():
    foods = Food.query.all()

    foods_dict = [food.to_dict(rules = ('-restaurants_with_food', )) for food in foods] # rules for how API displys for this route only

    response = make_response(
        foods_dict,
        200
    )

    return response

@app.route('/restaurants_foods/<int:id>', methods = ['GET', 'DELETE'])
def restaurants_foods(id):
    rf = FoodAtRestaurant.query.filter(FoodAtRestaurant.id == id).first()

    # need to check if ID leads to valid row
    if rf:
        if request.method == 'GET':
            rf_dict = rf.to_dict()

            response = make_response(
                rf_dict,
                200
            )
        elif request.method == 'DELETE':
            db.session.delete(rf) # deletes row from DB
            db.session.commit()

            response = make_response(
                {},
                200
            )
    else:
        response = make_response(
            {"Error" : "FoodAtRestaurant object not found!"},
            404
        )

    return response

class FoodByID(Resource):

    def get(self, id):
        food = Food.query.filter(Food.id == id).first()

        if food:
            food_dict = food.to_dict()

            response = make_response(
                food_dict,
                200
            )
        else:
            response = make_response(
                {"Error" : "Food object not found!"},
                404
            )

        return response
    
    def delete(self, id):
        food = Food.query.filter(Food.id == id).first()

        if food:
            # manual cascading delete of dependent rows
            assoc_rfs = FoodAtRestaurant.query.filter(FoodAtRestaurant.food_id == id).all()

            for assoc_rf in assoc_rfs:
                db.session.delete(assoc_rf)

            db.session.delete(food)

            db.session.commit()

            response = make_response(
                {},
                200
            )
        else:
            response = make_response(
                {"Error" : "Food object not found!"},
                404
            )

        return response
    
api.add_resource(FoodByID, "/foods/<int:id>") # Flask-RESTful manner of attaching resource to endpoint

@app.route('/restaurants/<int:id>', methods = ['DELETE'])
def restaurant_by_id(id):
    restaurant = Restaurant.query.filter(Restaurant.id == id).first()

    if restaurant:
        db.session.delete(restaurant)

        db.session.commit()

        response = make_response(
            {},
            200
        )
    else:
        response = make_response(
            {"Error" : "Restaurant object not found!"},
            404
        )

    return response

if __name__ == '__main__':
    app.run(port = 5555, debug = True)