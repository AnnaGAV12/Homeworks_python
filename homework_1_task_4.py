# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int (input ('Введите номер четверти плоскости '))
if number == 1:
    print(f'В {number} четверти диапазон координат X (0; ∞) и Y (0; ∞)')
elif number == 2:
    print(f'Во {number} четверти диапазон координат X (-∞; 0) и Y (0; ∞)')
elif number == 3:
    print(f'В {number} четверти диапазон координат X (-∞; 0) и Y (-∞; 0)')
elif number == 4:
    print(f'В {number} четверти диапазон координат X (0; ∞) и Y (-∞; 0)')