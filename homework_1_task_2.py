# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    print(x,end=' ')
for y in range(2):
    print( y,end=' ')
for z in range(2):
    print( z,end=' ')

print(not (x or y or z) == (not x and not y and not z))