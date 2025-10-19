class Car():
    def __init__(self, color):
        self.color = color

    def info(self):
        return f'Транспорт {self.color} цвета'
    
    def eng_volume(self, volume):
        return f'Транспорт {self.color} цвета, с обьемом двигателя {volume} л.'
    
    def __str__(self):
        return self.info()
    

class BMW(Car):
    def info(self):
        return f'Беха {self.color} цвета'
    
    def eng_volume(self, volume):
        return f'Беха {self.color} цвета, с обьемом двигателя {volume} л.'
    

class Bus(Car):
    def info(self):
        return f'Автобус {self.color} цвета'
    
    def eng_volume(self, volume):
        return f'Автобус {self.color} цвета, с обьемом двигателя {volume} л.'
    

class Taxi(Car):
    def info(self):
        return f'Такси {self.color} цвета'
    
    def eng_volume(self, volume):
        return f'Такси {self.color} цвета, с обьемом двигателя {volume} л.'
    

car1 = BMW('красного')
car2 = Bus('синего')
car3 = Taxi('черного')

def func(ex: Car, volume: int):
    return ex.eng_volume(volume)

print(func(car1, 4.4))
print(func(car2, 8))