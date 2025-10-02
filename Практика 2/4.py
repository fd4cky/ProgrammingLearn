from string import ascii_lowercase, ascii_uppercase, digits
from random import choices
symbols = "!@#$%^&*"
alphabit = [ascii_lowercase, ascii_uppercase, symbols, digits]


def password_generate(is_lowercase: bool, is_uppercase: bool, 
                      is_symbols: bool, is_digits: bool, 
                      length: int) -> str:
    
    alphabit_password = ""
    
    for index, is_bool in enumerate([is_lowercase, is_uppercase, is_symbols, is_digits]):
        alphabit_password += alphabit[index] if is_bool else ""

    result = "".join(choices(alphabit_password, k=length))

    return result


settings = map(int, input('Впишите параметры генерации:\n' \
'Перечисляйте через пробел: 1 - True, 0 - False\n' \
'Нижний регистр | Верхний регистр | Спец. символы | Цифры | Длина пароля\n').split())

print(password_generate(*settings))