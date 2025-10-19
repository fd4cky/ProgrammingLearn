class Employee():
    def __init__(self, hours):
        self.hours = hours #часов работы в день

    @property
    def salary(self): # В баксах
        return self.hours * 10 # базовая ставка


class Manager(Employee):
    def __init__(self, hours, clients_count):
        super().__init__(hours)
        self.clients_count = clients_count

    @property
    def salary(self):
        return self.hours * 10 + self.clients_count * 4 # к базовой ставке добавляем кол-во приведенных клиентов и умножаем на коэф.


class Developer(Employee):
    def __init__(self, hours, lines_of_code):
        super().__init__(hours)
        self.lines_of_code = lines_of_code

    @property
    def salary(self):
        return self.hours * 10 + self.lines_of_code * 6 # к базовой ставке добавляем кол-во строк кода и умножаем на коэф.
    

sanya = Developer(16, 400)
dima = Manager(8, 20)
print(f'зп сани программиста: {sanya.salary} $\nзп димы менеджера: {dima.salary} $')