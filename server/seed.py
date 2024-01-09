from app import app

from models import db, Restaurant, Food, FoodAtRestaurant

if __name__ == '__main__':
    with app.app_context():
        
        print("Clearing out tables...")

        Restaurant.query.delete()
        Food.query.delete()
        FoodAtRestaurant.query.delete()

        db.session.commit()

        print("Creating restaurants...")

        r1 = Restaurant(
            name = "Shake Shack"
        )
        r2 = Restaurant(
            name = "Byte Size"
        )

        db.session.add(r1)
        db.session.add(r2)

        db.session.commit()

        print("Creating foods...")

        foods = [
            Food(
                name = "burger"
            ),
            Food(
                name = "fries"
            ),
            Food(
                name = "hot dog"
            )
        ]

        db.session.add_all(foods)

        db.session.commit()

        print("Creating joint foods at restaurants...")

        rfs = [
            FoodAtRestaurant(
                price = 4.50,
                restaurant_id = r1.id,
                food_id = foods[0].id
            ),
            FoodAtRestaurant(
                price = 3.00,
                restaurant_id = r1.id,
                food_id = foods[2].id
            ),
            FoodAtRestaurant(
                price = 5.00,
                restaurant_id = r2.id,
                food_id = foods[0].id
            )
        ]

        db.session.add_all(rfs)

        db.session.commit()