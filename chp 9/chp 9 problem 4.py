class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Initialize attributes for restaurant name and cuisine type
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value for number_served

    def describe_restaurant(self):
        # Print the restaurant's name and its cuisine type
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

restaurant = Restaurant("The Gourmet Grill", "American")

print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(150)
print(f"Number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(50)
print(f"Number of customers served: {restaurant.number_served}")
