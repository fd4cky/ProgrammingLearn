from string import ascii_lowercase as ang_lower

rus_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet = {"rus": rus_lower, "ang": ang_lower}

word_input = input().strip().lower()
current_alph = "rus" if word_input[0] in rus_lower else "ang"


def encode(word):
    result = ""
    for ch in word:
        if ch == " ":
            result += " "
        else:
            result += alphabet[current_alph][alphabet[current_alph].index(ch) + 3]
    return result


def decode(word):
    result = ""
    for ch in word:
        if ch == " ":
            result += " "
        else:
            result += alphabet[current_alph][alphabet[current_alph].index(ch) - 3]
    return result


print(f'encode: {encode(word_input)}')
print(f'decode: {decode(encode(word_input))}')