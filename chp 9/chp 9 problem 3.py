class User:
    def __init__(self, first_name, last_name, age, location, email):
        # Initialize attributes for user's first name, last name, and additional details
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        # Print a summary of the user's information
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")
        print()

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")
        print()

user1 = User("John", "Doe", 28, "New York", "john.doe@example.com")
user2 = User("Jane", "Smith", 34, "California", "jane.smith@example.com")
user3 = User("Alice", "Johnson", 25, "Texas", "alice.johnson@example.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
