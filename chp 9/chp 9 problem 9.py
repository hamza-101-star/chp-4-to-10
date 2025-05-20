class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 100:
            range = 370
        return range

class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

    def get_range(self):
        return self.battery.get_range()

car = ElectricCar('Tesla', 'Model S', 2021)
print(f"Range before upgrade: {car.get_range()} miles")
car.battery.upgrade_battery()
print(f"Range after upgrade: {car.get_range()} miles")
