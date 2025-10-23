from __future__ import annotations

from typing import Dict, List, Tuple

# Словарь товаров: название → [цена, количество, категория]
tovars: Dict[str, List] = {
    "apple": [24, 50, "fruits"],
    "bananos": [30, 10, "fruits"],
    "baklagan": [12, 33, "vegetables"],
    "potatos": [8, 121, "vegetables"],
}

# Словарь пользователей и их покупок
users: Dict[str, Dict[str, int | float]] = {
    "user": {
        "total": 0,  # суммарный чек пользователя
        "apple": 3,  # история покупок
        "bananos": 4,
    }
}


class Product:
    """Базовый продукт (товар) каталога."""

    def __init__(self, title: str) -> None:
        """
        Инициализирует товар по названию.

        Args:
            title (str): Название товара (ключ в словаре `tovars`).
        """
        self.title = title

    @property
    def category(self) -> str:
        """
        Возвращает категорию товара.

        Returns:
            str: Название категории.
        """
        return tovars[self.title][2]

    @property
    def price(self) -> float:
        """
        Возвращает цену товара.

        Returns:
            float: Цена за единицу товара.
        """
        return float(tovars[self.title][0])

    @property
    def is_available(self) -> bool:
        """
        Проверяет наличие товара на складе.

        Returns:
            bool: True, если количество на складе больше 0, иначе False.
        """
        return tovars[self.title][1] > 0

    @property
    def stock(self) -> int:
        """
        Возвращает текущее количество товара на складе.

        Returns:
            int: Количество единиц товара.
        """
        return int(tovars[self.title][1])


class Order(Product):
    """Заказ на покупку товара определённым пользователем."""

    VAT_RATE = 0.20  # ставка НДС 20%

    def __init__(self, title: str, count: int, username: str) -> None:
        """
        Инициализирует заказ.

        Args:
            title (str): Название товара.
            count (int): Заказываемое количество.
            username (str): Имя пользователя (покупателя).
        """
        super().__init__(title)
        self.count = count
        self.username = username

    def buy(self) -> str | float:
        """
        Оформляет покупку: списывает товар со склада и обновляет данные пользователя.

        Returns:
            str | float: Стоимость покупки с НДС (float) при успехе,
                либо сообщение об ошибке (str).
        """
        # Если пользователя нет — создаём карточку покупок с нулевым итогом.
        if self.username not in users:
            users[self.username] = {"total": 0}

        # Проверяем доступность товара и достаточное количество.
        if not self.is_available or self.stock < self.count:
            return "Товар не в наличии или недостаточное количество"

        base_cost = self.price * self.count
        cost_with_vat = round(base_cost * (1 + self.VAT_RATE), 1)

        # Списываем со склада
        tovars[self.title][1] -= self.count

        # Обновляем историю покупок пользователя
        users[self.username][self.title] = users[self.username].get(self.title, 0) + self.count
        users[self.username]["total"] = float(users[self.username].get("total", 0)) + cost_with_vat

        return cost_with_vat


class Customer:
    """Покупатель/клиент, позволяющий запросить агрегированную информацию."""

    def __init__(self, username: str) -> None:
        """
        Инициализирует покупателя по имени.

        Args:
            username (str): Имя пользователя.
        """
        self.username = username

    @property
    def userinfo(self) -> str:
        """
        Возвращает сводную информацию о тратах и покупках пользователя.

        Returns:
            str: Отформатированная строка с суммой трат и перечнем купленных товаров.
        """
        if self.username in users:
            user = users[self.username]
            lines: List[str] = []
            for key, val in list(user.items())[1:]:
                lines.append(f"{val} {key}")
            return (
                f"{self.username} потратил суммарно {user['total']}, купив \n" + "\n".join(lines)
            )
        return "Пользователь не найден"

    def __str__(self) -> str:
        """
        Возвращает строковое представление пользователя.

        Returns:
            str: То же, что и `userinfo`.
        """
        return self.userinfo


class ShoppingCart(Product):
    """Инвентаризация: операции с количеством товара на складе."""

    def __init__(self, title: str) -> None:
        """
        Инициализирует корзину по названию товара.

        Args:
            title (str): Название товара.
        """
        super().__init__(title)

    def add(self, count: int) -> int:
        """
        Увеличивает количество товара на складе.

        Args:
            count (int): Сколько добавить.

        Returns:
            int: Новое количество товара.
        """
        tovars[self.title][1] += count
        return int(tovars[self.title][1])

    def minus(self, count: int) -> int:
        """
        Уменьшает количество товара на складе (не опускаясь ниже нуля).

        Args:
            count (int): Сколько убрать.

        Returns:
            int: Новое количество товара.
        """
        tovars[self.title][1] = max(tovars[self.title][1] - count, 0)
        return int(tovars[self.title][1])

    def update(self, count: int) -> int:
        """
        Устанавливает точное количество товара на складе.

        Args:
            count (int): Новое количество.

        Returns:
            int: Новое количество товара.
        """
        tovars[self.title][1] = count
        return int(tovars[self.title][1])

    def __str__(self) -> str:
        """
        Возвращает строковое представление текущего остатка.

        Returns:
            str: Количество товара в виде строки.
        """
        return str(tovars[self.title][1])


# Демонстрация работы
tovar = Product("apple")
order = Order("apple", 4, "user")
user = Customer("user")
cart = ShoppingCart("apple")

print(f"Изначальное количество яблок {cart}, по цене за штуку {tovar.price}")
print(f"купили 4 яблока за {order.buy()}")
print(user)
print(f"Количество яблок после покупки {cart}")
cart.add(1000)
print(f"Добавили 1000 яблок и стало {cart} яблок")