# Создайте программу для игры в ""Крестики-нолики"".

import random
import os

player_1 = []
player_2 = []

def player_2_turn():

    while True:
        num = random.randint(0,8)
        if cell[num] == '':
            cell[num] = 'O'

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'{cell[0]:^5}|{cell[1]:^5}|{cell[2]:^5}')
            print(f'-----------------')
            print(f'{cell[3]:^5}|{cell[4]:^5}|{cell[5]:^5}')
            print(f'-----------------')
            print(f'{cell[6]:^5}|{cell[7]:^5}|{cell[8]:^5}')
            lenn = len(player_1_turns)
            if lenn >= 3:
                player_2 = [(i, j, k) for i in player_1_turns for j in player_1_turns for k in player_1_turns]
            return


cell = ['' for x in range(9)]
print(f'{cell[0]:^5}|{cell[1]:^5}|{cell[2]:^5}')
print(f'-----------------')
print(f'{cell[3]:^5}|{cell[4]:^5}|{cell[5]:^5}')
print(f'-----------------')
print(f'{cell[6]:^5}|{cell[7]:^5}|{cell[8]:^5}')
turn = 0

win_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

player_1_turns = []
game = True
while game:
    while True:
        number = int(input('Введите ячейку от 0 до 8: '))
        if cell[number] == '':
            cell[number] = 'X'
            break
    player_1_turns.append(number)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{cell[0]:^5}|{cell[1]:^5}|{cell[2]:^5}')
    print(f'-----------------')
    print(f'{cell[3]:^5}|{cell[4]:^5}|{cell[5]:^5}')
    print(f'-----------------')
    print(f'{cell[6]:^5}|{cell[7]:^5}|{cell[8]:^5}')
    print(player_1_turns)
    lenn = len(player_1_turns)
    if lenn >= 3:
        player_1 = [(i, j ,k) for i in player_1_turns for j in player_1_turns for k in player_1_turns]

    for elemnt in player_1:
        if elemnt in win_combinations:
            print('Победа')
            game = False
    if game: player_2_turn()
    turn += 1
