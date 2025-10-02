count = int(input())


def print_pack_report(count: int) -> None:
    match count:
        case x if x % 5 == 0 and x % 3 == 0:
            print("расфасуем по 3 или по 5")
        case x if x % 5 == 0:
            print("расфасуем по 5")
        case x if x % 3 == 0:
            print("расфасуем по 3")
        case _:
            print("не заказываем!")


print_pack_report(count)