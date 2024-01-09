from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = "restaurants"

    serialize_rules = ('-foods_at_restaurant.restaurant', )

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

    foods_at_restaurant = db.relationship('FoodAtRestaurant', back_populates = 'restaurant')

class Food(db.Model, SerializerMixin):
    __tablename__ = "foods"

    serialize_rules = ('-restaurants_with_food.food', )

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

    restaurants_with_food = db.relationship('FoodAtRestaurant', back_populates = 'food')

class FoodAtRestaurant(db.Model, SerializerMixin):
    __tablename__ = "food_at_restaurant"

    serialize_rules = ('-restaurant.foods_at_restaurant', '-food.restaurants_with_food')

    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Float)

    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))
    food_id = db.Column(db.Integer, db.ForeignKey("foods.id"))

    restaurant = db.relationship('Restaurant', back_populates = 'foods_at_restaurant')
    food = db.relationship('Food', back_populates = 'restaurants_with_food')