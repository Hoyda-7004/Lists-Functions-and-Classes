# Hoyda Al Yahiri
# 11/10/23
# Lists, Functions, and Classes

class Vehicle:
    def __init__(self):
        self.vehicle_type = ""

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = 0
        self.make = ""
        self.model = ""
        self.doors = 0
        self.roof_type = ""

    def get_user_input(self):
        self.set_vehicle_type ("car ")
        self.year = int(input("Enter the year: "))
        self.make = input("Enter the make: ")
        self.model = input("Enter the model: ")
        self.doors = int(input("Enter the number of doors (2 or 4): "))
        self.roof_type = input("Enter the type of roof (solid or sun roof): ")

    def display_vehicle_info(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof_type)


def main():
    # Create an instance of the Automobile class
    car = Automobile()

    # Get user input for the car
    car.get_user_input()

    # Display the car information
    print("\nCar Information:")
    car.display_vehicle_info()


if __name__ == "__main__":
    main()
