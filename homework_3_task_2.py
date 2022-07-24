# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]

def multiplication (array):
    if len(array) % 2 == 0:
        l = len(array) // 2
    else: l = len(array) // 2 + 1
    multi_array = []
    for i in range(l):
        multi_array.append(array[i]* array[-i - 1])
    return multi_array

print (f'Произведение пар чисел списка {list} => ', multiplication (list))