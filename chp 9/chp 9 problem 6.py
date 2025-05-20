class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Initialize attributes for restaurant name and cuisine type
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        # Print the restaurant's name and its cuisine type
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        
    def open_restaurant(self):
        # Print a message indicating the restaurant is open
        print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f"Available Ice Cream Flavors at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Sweet Treats Ice Cream",  "Ice Cream", ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip", "Cookie Dough"])

ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
ice_cream_stand.open_restaurant()
