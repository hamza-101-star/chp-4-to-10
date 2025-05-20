class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print()

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant1 = Restaurant("La Bella Italia", "Italian")
restaurant2 = Restaurant("Sushi Express", "Japanese")
restaurant3 = Restaurant("Taco Haven", "Mexican")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
