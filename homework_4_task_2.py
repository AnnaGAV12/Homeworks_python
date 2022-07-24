# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def simple_multipliers(num):
    if num == 1:
        return ''
    i = 2
    while True:
        if num % i == 0: 
            break
        i+=1
    return str(i) + " " + simple_multipliers(int(num/i))
num = int(input("Введите натуральное число N = "))
print(f'список простых множителей числа :', simple_multipliers(num))