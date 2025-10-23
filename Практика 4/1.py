class Employee:
    """Представляет сотрудника с атрибутом количества рабочих часов в день."""

    def __init__(self, hours):
        """
        Инициализирует экземпляр Employee.

        Args:
            hours (int): Количество рабочих часов в день.
        """
        self.hours = hours  # часов работы в день

    @property
    def salary(self):
        """
        Вычисляет зарплату в долларах.

        Returns:
            int: Зарплата, основанная на рабочих часах и базовой ставке.
        """
        return self.hours * 10  # базовая ставка


class Manager(Employee):
    """Представляет менеджера, у которого есть клиенты помимо рабочих часов."""

    def __init__(self, hours, clients_count):
        """
        Инициализирует экземпляр Manager.

        Args:
            hours (int): Количество рабочих часов в день.
            clients_count (int): Количество приведенных клиентов.
        """
        super().__init__(hours)
        self.clients_count = clients_count

    @property
    def salary(self):
        """
        Вычисляет зарплату в долларах.

        Returns:
            int: Зарплата, основанная на рабочих часах и количестве клиентов с коэффициентами.
        """
        return self.hours * 10 + self.clients_count * 4  # к базовой ставке добавляем кол-во приведенных клиентов и умножаем на коэф.


class Developer(Employee):
    """Представляет разработчика, у которого есть количество написанных строк кода помимо рабочих часов."""

    def __init__(self, hours, lines_of_code):
        """
        Инициализирует экземпляр Developer.

        Args:
            hours (int): Количество рабочих часов в день.
            lines_of_code (int): Количество написанных строк кода.
        """
        super().__init__(hours)
        self.lines_of_code = lines_of_code

    @property
    def salary(self):
        """
        Вычисляет зарплату в долларах.

        Returns:
            int: Зарплата, основанная на рабочих часах и количестве строк кода с коэффициентами.
        """
        return self.hours * 10 + self.lines_of_code * 6  # к базовой ставке добавляем кол-во строк кода и умножаем на коэф.
    

sanya = Developer(16, 400)
dima = Manager(8, 20)
print(f'зп сани программиста: {sanya.salary} $\nзп димы менеджера: {dima.salary} $')