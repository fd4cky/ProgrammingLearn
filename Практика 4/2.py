class Car:
    """Базовый класс для транспортных средств.

    Атрибуты:
        color (str): Цвет транспортного средства.
    """

    def __init__(self, color):
        """Инициализация экземпляра Car.

        Args:
            color (str): Цвет транспортного средства.
        """
        self.color = color

    def info(self):
        """Возвращает информацию о транспортном средстве.

        Returns:
            str: Описание транспортного средства с указанием цвета.
        """
        return f'Транспорт {self.color} цвета'

    def eng_volume(self, volume):
        """Возвращает информацию о транспортном средстве и объеме двигателя.

        Args:
            volume (float): Объем двигателя в литрах.

        Returns:
            str: Описание транспортного средства, цвета и объема двигателя.
        """
        return f'Транспорт {self.color} цвета, с обьемом двигателя {volume} л.'

    def __str__(self):
        """Возвращает строковое представление объекта.

        Returns:
            str: Информация о транспортном средстве.
        """
        return self.info()


class BMW(Car):
    """Класс для автомобилей BMW, наследуется от Car."""

    def info(self):
        """Возвращает информацию о BMW.

        Returns:
            str: Описание BMW с указанием цвета.
        """
        return f'Беха {self.color} цвета'

    def eng_volume(self, volume):
        """Возвращает информацию о BMW и объеме двигателя.

        Args:
            volume (float): Объем двигателя в литрах.

        Returns:
            str: Описание BMW, цвета и объема двигателя.
        """
        return f'Беха {self.color} цвета, с обьемом двигателя {volume} л.'


class Bus(Car):
    """Класс для автобусов, наследуется от Car."""

    def info(self):
        """Возвращает информацию об автобусе.

        Returns:
            str: Описание автобуса с указанием цвета.
        """
        return f'Автобус {self.color} цвета'

    def eng_volume(self, volume):
        """Возвращает информацию об автобусе и объеме двигателя.

        Args:
            volume (float): Объем двигателя в литрах.

        Returns:
            str: Описание автобуса, цвета и объема двигателя.
        """
        return f'Автобус {self.color} цвета, с обьемом двигателя {volume} л.'


class Taxi(Car):
    """Класс для такси, наследуется от Car."""

    def info(self):
        """Возвращает информацию о такси.

        Returns:
            str: Описание такси с указанием цвета.
        """
        return f'Такси {self.color} цвета'

    def eng_volume(self, volume):
        """Возвращает информацию о такси и объеме двигателя.

        Args:
            volume (float): Объем двигателя в литрах.

        Returns:
            str: Описание такси, цвета и объема двигателя.
        """
        return f'Такси {self.color} цвета, с обьемом двигателя {volume} л.'


car1 = BMW('красного')
car2 = Bus('синего')
car3 = Taxi('черного')


def func(ex: Car, volume: int):
    """Возвращает информацию о транспортном средстве с объемом двигателя.

    Args:
        ex (Car): Экземпляр транспортного средства.
        volume (int): Объем двигателя.

    Returns:
        str: Описание транспортного средства с объемом двигателя.
    """
    return ex.eng_volume(volume)


print(func(car1, 4.4))
print(func(car2, 8))