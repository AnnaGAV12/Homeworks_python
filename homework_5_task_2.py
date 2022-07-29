# Сздайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint
import os
os.system('cls' if os.name == 'nt' else 'clear')


def case_1(n):
    while True:
        num = int(input("Игрок_1 введите число от 1 - 28: "))
        if 1 <= num <= 28:
            break
        else:
            print('Нужно ввести от 1 до 28')        
    return num
def case_2(n):
    while True:
        num = int(input("Игрок_2 введите число от 1 - 28: "))
        if 1 <= num <= 28:
            break
        else:
            print('Нужно ввести от 1 до 28')        
    return num
def case_3(n):
    num = randint(1,28)
    print(f'Бот вводит {num}')
    return num
def case_4(n, count):
    if count > 300:
            num = randint(1,28)
            print(f'Бот вводит {num}')
            return num
    elif count > 29:
        count = count - 29
        num = count % 28
        if num == 0:
            num = 28
        print(f'Бот вводит {num}')
        return num
    elif count == 29:
        num = 28
        print(f'Бот вводит {num}')
        return num
    elif count < 29:
        count = count * 1
        num = count
        print(f'Бот вводит {num}')
        return num
def game_start(check):
    if check == 0:
        print(f'Игру начинает ИГРОК_1. У нас {count} конфет')
    elif check == 1:
        print(f'Игру начинает ИГРОК_2. У нас {count} конфет') 
def game_start2(check):
    if check == 0:
        print(f'Игру начинает ИГРОК_1. У нас {count} конфет')
    elif check == 1:
        print(f'Игру начинает бот. У нас {count} конфет')
def game_over(check):
        if check == 0:
            print(f'GAME OVER  Win ИГРОК_2')
        if check == 1:
            print(f'GAME OVER  Win ИГРОК_1')
def game_over2(check):
        if check == 0:
            print(f'GAME OVER  Win ИГРОК_2')
        if check == 1:
            print(f'GAME OVER  Win бот')

count = 300
player_one = 0
player_two = 0

pp_ii = int(input('Выбирите против кого играть: \n- Игрок против игрока = 0:\n- Играть с ботом = 1:\nВведите число: '))

# Игрок против Игрока
if pp_ii == 0: 
    check = randint(0,1)
    game_start(check)
    while count >= 1:
        while check == 0: 
            player_one = int(case_1(player_one))
            count -= player_one
            check += 1
            print(f'У нас осталось {count} конфет')
            if count <= 0:
                break        
        else:
            check == 1
            player_two = int(case_2(player_two))
            count -= player_two
            check -= 1
            print(f'У нас осталось {count} конфет')
    if count <=0:
        game_over(check)

elif pp_ii == 1: 
    dif = int(input('Выбирите уровень сложности:\n- простой бот = 0\n- бот с интеллектом = 1\nВведите число: '))

 #  Игрок против простого бота

    if dif == 0:
        check = randint(0,1)
        game_start2(check)  
        while count >= 1:
            while check == 0: 
                player_one = int(case_1(player_one))
                count -= player_one
                check += 1
                print(f'У нас осталось {count} конфет')
                if count <= 0:
                    break
            else:
                check == 1
                player_two = int(case_3(player_two))
                count -= player_two
                check -= 1
                print(f'У нас осталось {count} конфет')
        if count <=0:
            game_over2(check)

 #  Игрок против бота с интеллектом

    if dif == 1:
        check = randint(0,1)
        game_start2(check)  
        while count >= 1:
            while check == 0: 
                player_one = int(case_1(player_one))
                count -= player_one
                check += 1
                print(f'У нас осталось {count} конфет')
                if count <= 0:
                    break
            else:
                check == 1
                player_two = int(case_4(player_two, count))
                count -= player_two
                check -= 1
                print(f'У нас осталось {count} конфет')
        if count <=0:
            game_over2(check)