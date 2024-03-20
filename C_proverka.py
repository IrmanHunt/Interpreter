from B_sklad import *

def proverka_func():

    line_number = 1

    while line_number < len(code_arr):

        cycle_line = code_arr[line_number]

        flag = True

        for i in range(len(possible_lines)):

            if possible_lines[i].template.fullmatch(cycle_line) :

                flag = False

                break

        if flag:
            print(f'Ошибка в строке {line_number}! Невозможная строка!')
            exit()  

        for i in range(len(braces_lines)):

            if braces_lines[i].template.fullmatch(cycle_line) :

                braces_lines[i].check(cycle_line, line_number)

                break
        
        line_number += 1

    for i in range(len(braces_arr)):

        if braces_arr[i].right_brace == 0 or braces_arr[i].left_brace == 0:

            print(f'Ошибка в строке {braces_arr[i].line_number}!', 'Проблемы с фигурными скобками!')
            exit()

    return True