# Вычислить число Pi c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

def accuracy(number: float):
    count = 0
    while number != 1:
        number *= 10
        count += 1
    return count

d = float(input('Введите математическую точность: '))
c = accuracy(d) 
pi_str = str(math.pi)
e = 2 + c
print(f'- при математической точности d = {d}, π = ', pi_str[0:e])