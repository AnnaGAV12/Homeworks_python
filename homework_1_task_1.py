# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:  - 6 -> да, - 1 -> нет

print('Является ли день недели выходным ')
a = int (input ('Введите номер дня недели '))
if a > 0 and a < 6:
    print(' -> нет')
elif a > 5 and a < 8:
    print(' -> да')