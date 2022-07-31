# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
import os

def letters_to_rle():
    path ='folder' + os.sep + 'hm_5_t_4.txt'
    with open(path, 'r') as my_file:
        letters = my_file.readline()
        letters_c = letters[0]
        letters_rle = ""
        count = 1
        for i in range(1, len(letters)):
            if letters[i] == letters_c[-1]:
                count += 1
            else:
                letters_rle += str(count) + letters_c[-1]
                letters_c += letters[i]
                count = 1
        letters_rle += str(count) + letters_c[-1]

    path ='folder' + os.sep + 'hm_5_t_4final.txt'
    with open(path, 'w') as my_file:   
        my_file.write(letters_rle)

def rle_to_letters():
    path ='folder' + os.sep + 'hm_5_t_4final.txt'
    with open(path, 'r') as my_file:
        letters_rle = my_file.readline()
        letters =''
        count = ''
        for i in range(len(letters_rle)):
            if letters_rle[i].isdigit(): count += letters_rle[i]
            else:
                letters += int(count) * letters_rle[i]
                count = ''

letters_to_rle()
rle_to_letters()