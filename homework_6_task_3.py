# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел.

import random
def int_list_from_string(positions: str) -> list:
    positions_list = positions.split(' ')
    positions_list = [int(pos) for pos in positions_list]
    return positions_list

def multiplicity_in_list(list: list, positions_list: list) -> int:
    multiplicity = 1
    for i in positions_list:
        multiplicity *= list[i-1]
    return multiplicity

num = int(input('Введите N: '))
randlam = lambda n: random.randint(-n,n+1)
list = [randlam(num) for i in range(0, num)]

print(f'Полученный список с числами из промежутка -{num} до {num}\n{list}\n')
positions = input(
    f'Введите позиции элементов для вычисления произведения через пробел (от 1 до {num}):\n')
pos_list = int_list_from_string(positions)
print(f'Произведение элементов равно {multiplicity_in_list(list, pos_list)}')