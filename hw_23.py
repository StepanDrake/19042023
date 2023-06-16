# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    def __init__(self, car_brand: str, tank_volume: int, rest_of_fuel: int, speed: int, car_mileage: int):
        self.car_brand = car_brand      # марка
        self.tank_volume = tank_volume  # обєм баку
        self.rest_of_fuel = rest_of_fuel # залишок пального в баку
        self.speed = speed               # швидкість
        self.car_mileage = car_mileage   # пробіг
        
    
    def filling_tank(self, amount_of_fuel):
        """метод заправки"""
        
        if self.rest_of_fuel + amount_of_fuel > self.tank_volume:
           self.rest_of_fuel = self.tank_volume
        else: 
            self.rest_of_fuel = self.rest_of_fuel + amount_of_fuel
        print(f'Зараз пального: {self.rest_of_fuel}')
    
    
    def drains_fuel (self, other, amount_of_fuel):
        """метод переливу пального від себе іншому транспортному засобу"""
        
        if (self.rest_of_fuel < amount_of_fuel) and (other.tank_volume - other.rest_of_fuel < 
                                                     amount_of_fuel) and (self.rest_of_fuel <= other.tank_volume - other.rest_of_fuel):
           other.rest_of_fuel = other.rest_of_fuel + self.rest_of_fuel
           self.rest_of_fuel = 0
        elif (self.rest_of_fuel < amount_of_fuel) and (other.tank_volume - other.rest_of_fuel < 
                                                     amount_of_fuel) and (self.rest_of_fuel > other.tank_volume - other.rest_of_fuel):
            other.rest_of_fuel = other.tank_volume
            self.rest_of_fuel = other.tank_volume - other.rest_of_fuel
            
        elif (self.rest_of_fuel < amount_of_fuel) and (other.tank_volume - other.rest_of_fuel > amount_of_fuel):
                other.rest_of_fuel = self.rest_of_fuel +  other.rest_of_fuel
                self.rest_of_fuel = 0
        
        elif (self.rest_of_fuel >= amount_of_fuel) and (other.tank_volume - other.rest_of_fuel <= amount_of_fuel):
            other.rest_of_fuel = other.tank_volume
            self.rest_of_fuel = self.rest_of_fuel - (other.tank_volume - other.rest_of_fuel)
        
        elif (self.rest_of_fuel >= amount_of_fuel) and (other.tank_volume - other.rest_of_fuel >= amount_of_fuel):
            other.rest_of_fuel = other.rest_of_fuel + amount_of_fuel
            self.rest_of_fuel = self.rest_of_fuel - amount_of_fuel
        print(f'Залишилось пального {self.rest_of_fuel} ')
    @abstractmethod
    def __str__():
        pass


class Car(Vehicle):
    
    def __init__(self, number_passengers = 4, airbags = False, car_brand = '', tank_volume = 40, 
                              rest_of_fuel = 0, speed = 100, car_mileage = 0):
        super().__init__(car_brand, tank_volume, rest_of_fuel, speed, car_mileage)
        
        self.number_passengers = number_passengers # КІЛЬКІСТЬ ПАСАЖИРІВ
        self.airbags = airbags # ознака наявності подушок безпеки (тру/фолс)
        
    def __str__(self):
        return f'Машина марки {self.car_brand}, пробіг {self.car_mileage}'
    


class Motorcycle(Vehicle):
    
    def __init__(self, presence_stroller = False, car_brand = '', tank_volume = 0, 
                              rest_of_fuel = 0, speed = 0, car_mileage = 0):
        super().__init__(car_brand, tank_volume, rest_of_fuel, speed, car_mileage)
        
        self.presence_stroller = presence_stroller # опція наявності люльки (тру/фолс)
    
    def __str__(self):
        return f'Мотоцикл марки {self.car_brand}, пробіг {self.car_mileage}'
    
my_car = Car(airbags = True, tank_volume = 40)    

qw = Car(tank_volume = 40)
qw.filling_tank(13)
qw.drains_fuel(my_car, 6)