# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции вводит пользователь через пробел.

def list_of_numbers(n):
    array = list(range(-n , n + 1))
    return array

def element_position():
    elements = element.split(" ")
    return elements
    
def multiply_elements(list: list, elements: list):
    multiply = 1
    for i in elements:
        multiply *= list[int(i)]
    return multiply

n = int(input('Введите число N: ') )
element = input("Введите позиции элементов через пробел: ")
numbers = list_of_numbers(n)
elements = element_position()
print(numbers)
print(multiply_elements(numbers, elements))