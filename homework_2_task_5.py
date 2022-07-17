# Реализуйте алгоритм перемешивания списка.

import random

def mix_list(list: list):
    for i in range(0, len(list)):
        mixed_list_i = random.randint(0, len(list)-1)
        list[i], list[mixed_list_i] = list[mixed_list_i], list[i]
    return list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Исходный список:', list)

mixed_list = mix_list(list)
print('Перемешанный список:', mixed_list)