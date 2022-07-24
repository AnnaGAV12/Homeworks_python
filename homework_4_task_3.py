# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

def non_repeat_numbers(array):
    s_array = set(array)  
    empty_array = [] 
    for num_s in s_array:
        count = 0
        for num in array:
            if num == num_s:
                count += 1
        if count == 1:
            empty_array.append(num_s)
    return empty_array

list = [1, 2, 2, 3, 89, 56, 1]
print(f' Исходная последовательность чисел', list)
print(f' Cписок неповторяющихся элементов', non_repeat_numbers(list))