class Car:
    def details(self):
        print("CAR PROPERTIES")
        self.name = input("Name: ")
        self.color = input("Color: ")
        self.fuel_level = input("Increment Fuel Level: ")
    def show_details(self):
        print(f"CAR PROPERTIES\n Name: {self.name}\n Color: {self.color}\n Increment Fuel Level: {self.fuel_level}\n")