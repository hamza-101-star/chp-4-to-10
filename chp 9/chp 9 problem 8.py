class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin():
    def __init__(self, first_name, last_name, age, location, email, privileges=None):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges(privileges)

admin1 = Admin(
    "Alice", 
    "Johnson", 
    30, 
    "Texas", 
    "alice.johnson@example.com", 
    ["can add post", "can delete post", "can ban user", "can promote user"]
)

admin1.privileges.show_privileges()
