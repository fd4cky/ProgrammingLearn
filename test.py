def fibonacci(n):
    digits = [0, 1]
    for i in range(2):
        yield digits[i]
    for i in range(2, n):
        digits.append(digits[i-1] + digits[i-2])
        yield digits[i]



sequence = fibonacci(10)
for number in sequence:
    print(number)