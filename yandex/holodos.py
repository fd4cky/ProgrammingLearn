import datetime
from decimal import Decimal


def add(
    items: dict[str, list[dict]],
    title: str,
    amount: Decimal,
    expiration_date: datetime = None
):
    # Если дата передана строкой — конвертируем в объект date
    if expiration_date is not None:
        expiration_date = datetime.datetime.strptime(expiration_date, r'%Y-%m-%d').date()

    # Если товара с таким названием ещё нет — создаём пустой список партий и добавляем новую партию
    items[title] = items.get(title, []) + [{
        'amount': amount,
        'expiration_date': expiration_date
    }]


def add_by_note(items: dict, note: str):
    parts = note.split()
    # Проверка на наличие даты: если последний элемент похож на дату — значит указана дата
    if '-' in parts[-1]:
        title = ' '.join(parts[:-2])
        amount = Decimal(parts[-2])
        expiration_date = parts[-1]
    else:
        title = ' '.join(parts[:-1])
        amount = Decimal(parts[-1])
        expiration_date = None

    add(items, title, amount, expiration_date)


def find(items: dict, needle: str):
    needle = needle.lower()
    # Проходим по всем ключам и ищем подстроку без учёта регистра
    return [item for item in items.keys() if needle in item.lower()]


def amount(items: dict, needle: str):
    keys = find(items, needle)
    count = Decimal(0)

    for title, item in items.items():
        if title in keys:
            # Суммируем количество по всем партиям найденного товара
            count += sum(batch['amount'] for batch in item)

    return count