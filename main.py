# 1
# celsius = int(input())
# fahrenheit = (celsius * 9/5) + 32
# kelvin = celsius + 273.15

# print(f'{celsius}C = {fahrenheit}F', f'{celsius}C = {kelvin}K', sep='\n')


#2
# n = int(input())

# quest = ["четное?", "знак", "принадлежит ли диапазону [10; 50]"]

# if n % 2 == 0:
#     print(f'{quest[0]} - Да')
# else:
#     print(f'{quest[0]} - Нет')

# if n > 0:
#     print(f'{quest[1]} - Большие 0')
# elif n < 0:
#     print(f'{quest[1]} - Меньше 0')
# else:
#     print(f'{quest[1]} - 0')

# if n in range(10, 51):
#     print(f'{quest[2]} - Да')
# else:
#     print(f'{quest[2]} - Нет')


#3
# from random import choices, shuffle
# from string import ascii_uppercase, digits
# chars = '!@#$%^&*'

# psw = ''.join(choices(ascii_uppercase, k=3)) + ''.join(choices(digits, k=3)) + ''.join(choices(chars, k=2))
# password = list(psw)
# shuffle(password)
# print(''.join(password))


#4
s = input().lower()

counts = dict()
for i in s:
    counts[i] = counts.get(i, 0) + 1

print('\n'.join(f'{i[0]}: {i[1]}' for i in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]))
