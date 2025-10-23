from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import Any


def add(
    items: dict[str, list[dict[str, Any]]],
    title: str,
    amount: Decimal,
    expiration_date: date | None = None,
) -> None:
    """
    Добавляет партию товара в хранилище.

    Args:
        items (dict[str, list[dict[str, Any]]]): Словарь со списками партий
            по названию товара. Каждая партия — словарь с ключами
            'amount' (Decimal) и 'expiration_date' (date | None).
        title (str): Название товара.
        amount (Decimal): Количество (в единицах товара).
        expiration_date (date | None, optional): Дата годности партии.
            Можно передавать None или дату; если дата будет строкой
            формата 'YYYY-MM-DD', преобразуйте её заранее (см. пример).

    Returns:
        None: Функция ничего не возвращает, изменяет словарь items на месте.

    Raises:
        ValueError: Если количество amount отрицательное.
    """
    if amount < 0:
        raise ValueError("Количество 'amount' не может быть отрицательным.")

    items[title] = items.get(title, []) + [
        {
            "amount": amount,
            "expiration_date": expiration_date,
        }
    ]


def add_by_note(items: dict[str, list[dict[str, Any]]], note: str) -> None:
    """
    Добавляет партию, распарсив строку заметки.

    Заметка имеет вид:
    - «<название> <кол-во>» — без даты,
    - «<название> <кол-во> YYYY-MM-DD» — с датой.

    Args:
        items (dict[str, list[dict[str, Any]]]): Хранилище партий по товарам.
        note (str): Строка заметки.

    Returns:
        None

    Raises:
        ValueError: Если не удалось распарсить количество или дату.
    """
    parts = note.split()
    if not parts:
        raise ValueError("Пустая строка заметки.")

    if "-" in parts[-1]:
        if len(parts) < 3:
            raise ValueError("Ожидались '<название> <кол-во> <дата>'.")
        title = " ".join(parts[:-2])
        try:
            amount = Decimal(parts[-2])
        except Exception as exc:  # DecimalException family
            raise ValueError("Некорректное количество в заметке.") from exc
        try:
            expiration_date = datetime.strptime(parts[-1], r"%Y-%m-%d").date()
        except ValueError as exc:
            raise ValueError("Некорректная дата, ожидается YYYY-MM-DD.") from exc
    else:
        if len(parts) < 2:
            raise ValueError("Ожидались '<название> <кол-во>'.")
        title = " ".join(parts[:-1])
        try:
            amount = Decimal(parts[-1])
        except Exception as exc:
            raise ValueError("Некорректное количество в заметке.") from exc
        expiration_date = None

    add(items, title, amount, expiration_date)


def find(items: dict[str, list[dict[str, Any]]], needle: str) -> list[str]:
    """
    Находит товары по подстроке без учёта регистра.

    Args:
        items (dict[str, list[dict[str, Any]]]): Хранилище товаров.
        needle (str): Подстрока для поиска.

    Returns:
        list[str]: Список названий товаров, содержащих needle.
    """
    query = needle.lower()
    return [name for name in items.keys() if query in name.lower()]


def amount(items: dict[str, list[dict[str, Any]]], needle: str) -> Decimal:
    """
    Возвращает суммарное количество по всем партиям найденных товаров.

    Поиск выполняется по подстроке без учёта регистра (см. find()).

    Args:
        items (dict[str, list[dict[str, Any]]]): Хранилище товаров.
        needle (str): Подстрока для поиска товаров.

    Returns:
        Decimal: Сумма по полю 'amount' во всех партиях найденных товаров.
    """
    names = set(find(items, needle))
    total = Decimal("0")

    for title, batches in items.items():
        if title in names:
            total += sum(batch["amount"] for batch in batches)

    return total