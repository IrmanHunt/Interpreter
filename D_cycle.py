from B_sklad import *

def cycle_func():

    line_number = 1

    while line_number < len(code_arr):

        cycle_line = code_arr[line_number]

        for i in range(len(possible_lines)):

            if possible_lines[i].template.fullmatch(cycle_line) :

                line_number = possible_lines[i].solution(cycle_line, line_number)

                break
        
        line_number += 1