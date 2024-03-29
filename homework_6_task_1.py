# Реализуйте алгоритм перемешивания списка.

# def list_minus_n_to_n(number: int) -> list:
#     list = []
#     for i in range(-number, number+1):
#         list.append(i)
#     return list

import random
def mix_list(list: list) -> list:
    for i in range(0, len(list)):
        mixed_list_i = random.randint(0, len(list)-1)
        list[i], list[mixed_list_i] = list[mixed_list_i], list[i]
    return list

num = int(input('\nВведите размерность создаваемого списка: '))
initial_list = [n for n in range(-num, num+1)]
print(f'\nСозданный начальный список:\n{initial_list}')
mixed_list = mix_list(initial_list)
print(f'\nПеремешанный список:\n{mixed_list}\n')