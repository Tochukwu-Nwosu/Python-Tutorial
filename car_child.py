from car import Car

class Car_Child (Car):
    def drive (self):
        print("Driving a", self.name,"car")

car1 = Car_Child()
car1.details()
car1.show_details()
car1.drive()
print(car1.name)