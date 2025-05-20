class User:
    def __init__(self, first_name, last_name, age, location, email):
        # Initialize attributes for user's first name, last name, and additional details
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0  # Initialize login attempts to 0

    def describe_user(self):
        # Print a summary of the user's information
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")
        print()

    def greet_user(self):
        # Print a personalized greeting to the user
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")
        print()

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
user1 = User("John", "Doe", 28, "New York", "john.doe@example.com")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")

user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")
