class Car():
    def __init__(self, color):
        self.color = color

    def info(self):
        return f'Транспорт {self.color} цвета'
    
    def __str__(self):
        return self.info()
    

class BMW(Car):
    def info(self):
        return f'Беха {self.color} цвета'
    

class Bus(Car):
    def info(self):
        return f'Автобус {self.color} цвета'
    

class Taxi(Car):
    def info(self):
        return f'Такси {self.color} цвета'
    

car1 = BMW('красного')
car2 = Bus('синего')
car3 = Taxi('черного')

print(car1)
print(car2)
print(car3)