# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример: - x=34; y=-30 -> 4 , - x=2; y=4-> 1 , - x=-34; y=-30 -> 3

print('Поиск номера четверти плоскости заданной точки')
x = int (input ('Введите координаты точки Х≠ 0 '))
y = int (input ('Введите координаты точки Y≠ 0 '))
if x > 0 and y > 0:
    print(' -> 1')
elif x < 0 and y > 0:
    print(' -> 2')
elif x < 0 and y < 0:
    print(' -> 3')
elif x > 0 and y < 0:
    print(' -> 4')

