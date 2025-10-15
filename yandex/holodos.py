import datetime
from decimal import Decimal


def add(items: dict[str: list[dict]], title: str, amount: Decimal, expiration_date: datetime = None):
    # Если дата передана строкой — конвертируем в объект date
    if expiration_date != None:
        expiration_date = datetime.datetime.strptime(expiration_date, r'%Y-%m-%d').date()
    
    # Если товара с таким названием ещё нет — создаём пустой список партий
    items[title] = items.get(title, [])

    for index_item in range(len(items[title])):
        if items[title][index_item]['expiration_date'] == expiration_date:
           items[title][index_item]['amount'] += amount
           break
    else: # Если партии с этой датой нет — добавляем новую запись
        items[title] = items.get(title, []) + [{'amount': amount, 'expiration_date': expiration_date}]
    if len(items[title]) == 0:
        items[title] += [{'amount': amount, 'expiration_date': expiration_date}]


def add_by_note(items: dict, note: str):
    # Проверка на наличие даты: если последний элемент списка похож на дату — значит указана дата
    if '-' in note.split()[-1]:
        title = ' '.join(note.split()[:-2])
        amount = Decimal(note.split()[-2])
        expiration_date = note.split()[-1]
    else:
        title = ' '.join(note.split()[:-1])
        amount = Decimal(note.split()[-1])
        expiration_date = None
    add(items, title, amount, expiration_date)


def find(items: dict, needle: str):
    needle = needle.lower()
    # Проходим по всем ключам и ищем подстроку без учёта регистра
    finder = [item for item in items.keys() if needle in item.lower()]
    return finder


def amount(items: dict, needle: str):
    keys = find(items, needle)
    count = 0

    for title, item in items.items():
        if title in keys:
            # Суммируем количество по всем партиям найденного товара
            count += sum([amount['amount'] for amount in item])

    return Decimal(count)