"""
Модуль для генерации случайных паролей с настройкой использования
строчных и заглавных букв, цифр и специальных символов.
"""
from string import ascii_lowercase, ascii_uppercase, digits
from random import choices

symbols = "!@#$%^&*"
alphabit = [ascii_lowercase, ascii_uppercase, symbols, digits]


def password_generate(is_lowercase: bool, is_uppercase: bool,
                      is_symbols: bool, is_digits: bool,
                      length: int) -> str:
    """
    Генерирует случайный пароль в соответствии с указанными параметрами.

    Аргументы:
        is_lowercase (bool): Использовать ли строчные буквы.
        is_uppercase (bool): Использовать ли заглавные буквы.
        is_symbols (bool): Использовать ли специальные символы.
        is_digits (bool): Использовать ли цифры.
        length (int): Длина генерируемого пароля.

    Возвращает:
        str: Сгенерированный пароль.
    """
    alphabit_password = ""

    for index, is_bool in enumerate([is_lowercase, is_uppercase, is_symbols, is_digits]):
        alphabit_password += alphabit[index] if is_bool else ""

    result = "".join(choices(alphabit_password, k=length))

    return result


settings = map(
    int,
    input(
        'Впишите параметры генерации:\n'
        'Перечисляйте через пробел: 1 - True, 0 - False\n'
        'Нижний регистр | Верхний регистр | Спец. символы | Цифры | Длина пароля\n'
    ).split()
)

print(password_generate(*settings))