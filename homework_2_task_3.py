# Задайте список из n чисел последовательности (1+ 1/n)^n
# и выведите на экран их сумму.
# Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def sequence_of_numbers(number: float):
    list = []
    for i in range(1, number+1):
        list.append((1 + 1 / i) ** i)
    return list

def sum_of_numbers(list: list):
    sum = 0
    for i in list:
        sum += i
    return sum

num = int(input('Введите число N: '))
list = sequence_of_numbers(num)
sum = sum_of_numbers(list)
print(f'Последовательность для заданного N: {list}')
print(f'Сумма элементов последовательности равна {sum}')