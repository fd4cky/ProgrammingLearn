def print_pack_report(count: int) -> None:
    """
    Определяет способ расфасовки в зависимости от переданного количества.

    Аргументы:
        count (int): Количество товара.

    Возвращает:
        None: Выводит способ расфасовки или сообщение о невозможности заказа.
    """
    match count:
        case x if x % 5 == 0 and x % 3 == 0:
            print("расфасуем по 3 или по 5")
        case x if x % 5 == 0:
            print("расфасуем по 5")
        case x if x % 3 == 0:
            print("расфасуем по 3")
        case _:
            print("не заказываем!")


count = int(input())

print_pack_report(count)