roman_map = {
    'I': 1, 'V': 5, 'X': 10,
    'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

int_map = {v: k for k, v in roman_map.items()} # перевернули ключ с значением из roman_map


def roman_to_int(roman_digit: str) -> int:
    result = 0

    roman_digits = list(roman_digit)
    roman_int_digits = [roman_map.get(x) for x in roman_digits] + [0]   # 0 добавляется для того, чтобы алгоритм
                                                                        # проверял все члены списка
    
    for index in range(len(roman_int_digits) - 1): # тут суммируем все значения с учетом правил
        if roman_int_digits[index] >= roman_int_digits[index + 1]: # если справа старшая степень - вычитаем курентное из резалта, в противном случае наоборот
            result += roman_int_digits[index]
        else:
            result -= roman_int_digits[index]

    return result


def int_to_roman(int_digit: int) -> str:
    result = []

    while int_digit != 0: # пока не добьем число до 0 будем вычитать близжайшие к нему числа (или добавлять)
        closest_key = {roman_digit: abs(int_digit - roman_digit) for roman_digit in roman_map.values()} # создаем словарь где ключ - цифры (римские), а значение - модуль разницы между курентным числом и цифрой
        sorted_closest_key = sorted(list(closest_key.items()), key=lambda x: x[1]) # сортируем словарь по значениям (модулю разницы)
        closest_num = sorted_closest_key[0][0] # берем элемент с наименьшей разницей

        result.append(int_map[closest_num])

        if int_digit > 0:
            int_digit -= closest_num # если все норм и число не зашло за 0 вычитаем разницу
        elif int_digit < 0:          #в противном случае добавляем и на result[-2] ставим число соотносимое
            result[-2], result[-1] = result[-1], result[-2] # переворачиваем чтобы сделать "вычитание" в римских цифрах
            int_digit += closest_num

    return "".join(result)

print(roman_to_int("MMCMXCIX")) # MMIM
print(int_to_roman(2999))