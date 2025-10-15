import datetime
from decimal import Decimal


def add(
    items: dict[str, list[dict]],
    title: str,
    amount: Decimal,
    expiration_date: str | None = None
):
    # Если дата передана строкой — конвертируем в объект date
    if expiration_date is not None:
        expiration_date = datetime.datetime.strptime(expiration_date, r'%Y-%m-%d').date()

    # Если товара с таким названием ещё нет — создаём пустой список партий
    items[title] = items.get(title, [])

    # Ищем уже существующую партию с такой же датой
    for index_item in range(len(items[title])):
        if items[title][index_item]['expiration_date'] == expiration_date:
            items[title][index_item]['amount'] += amount
            break
    else:
        # Если партии с этой датой нет — добавляем новую запись
        items[title] = items.get(title, []) + [
            {'amount': amount, 'expiration_date': expiration_date}
        ]

    if len(items[title]) == 0:
        items[title] += [
            {'amount': amount, 'expiration_date': expiration_date}
        ]


def add_by_note(items: dict, note: str):
    parts = note.split()

    # Проверка на наличие даты: если последний элемент списка похож на дату — значит указана дата
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
    finder = [item for item in items.keys() if needle in item.lower()]
    return finder


def amount(items: dict, needle: str):
    keys = find(items, needle)

    for title, batches in items.items():
        if title in keys:
            # Суммируем количество по всем партиям найденного товара
            # (batches — список словарей с amount и expiration_date)
            total = sum(batch['amount'] for batch in batches)

    return Decimal(total)