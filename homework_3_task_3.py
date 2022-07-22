# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]

def  fract_part(array):
    l = len(array)
    array_of_decimal_part = []
    for i in range(l):
        if "." in str(array[i]):
            tmp = float("0." + str(array[i]).split(".")[1])
            array_of_decimal_part.append(tmp)
    return array_of_decimal_part

def difference_max_min(array):
    array =  fract_part(array)
    l = len(array)
    imin = imax = 0
    for i in range(l):
        if array[i] < array[imin]:
            imin = i
        if array[i] > array[imax]:
            imax = i
    return array[imax] - array[imin]

print(f'Cписок из вещественных чисел {list}')
print(f'\nРазница между максимальным и минимальным значением дробной части элементов:',
 difference_max_min(list))