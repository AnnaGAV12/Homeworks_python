# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр
# Пример: - 6782 -> 23    - 0,56 -> 11

def digit(number: float):
    digits_string = str(number)
    sum = 0
    for num in digits_string:
        if num != '.':
            sum += int(num)
    return sum

num = float(input('Введите число: '))
print(f'Сумма цифр введенного числа равна {digit(num)}')