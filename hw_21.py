from datetime import datetime


"""опис авто"""
class Car:
    def __init__(self, year, brand, model, mileage, fuel:float):
        self.year = year
        self.brand = brand
        self.model = model
        self.mileage = mileage
        self.fuel = fuel
    def __str__(self)->str:
        return f'Car: {self.year} {self.brand} {self.model} {self.mileage} {self.fuel}'


    @property
    def age(self):
        year_car = datetime.today().year
        return year_car - self.year

car1 = Car("2020", "TESLA", "Y", "32123", "3,5")
car2 = Car("2020", "Hyundai", "Accent", "32133", "4,5")


print(car1)
print(car2)
