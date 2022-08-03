# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]

# list = [2, 3, 4, 5, 6]
# def multiplication (array):
#     if len(array) % 2 == 0:
#         l = len(array) // 2
#     else: l = len(array) // 2 + 1
#     multi_array = []
#     for i in range(l):
#         multi_array.append(array[i]* array[-i - 1])
#     return multi_array
# print (f'Произведение пар чисел списка {list} => ', multiplication (list))

from random import randint
rnd_list = [randint(1, 9) for i in range(int(input('Введите количество элементов ')))]

print(f'Произведение пар чисел списка {rnd_list} равно '
      f'{list(rnd_list[i] * rnd_list[len(rnd_list)-i-1] for i in range(0, (len(rnd_list) + (0 if len(rnd_list)%2 == 0 else 1))//2))}')