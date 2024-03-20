import re

var_dict = {}
braces_arr = []
code_arr = []

code_arr.append('Язык программирования KrasovOneLove!')

with open('F_code.txt', encoding = 'utf-8') as f:
    for line in f:
        code_arr.append(line)



int_template = r'-*[0-9]+'
float_template = r'-*[0-9]+.[0-9]+'
bool_template = r'True|False'
var_template = r'[A-Z]+'
expression_template = r'\(.+\)'
from_keyboard_template = r'from_keyboard'

figure_template = r'-?\d+(\.\d+)?' 
exp_1_template = r'\(-?\d+(\.\d+)?([\+\-\*\/]-?\d+(\.\d+)?)+\)'
exp_2_template = r'\((True|False|0|-?\d+(\.\d+)?)([ao><=](True|False|0|-?\d+(\.\d+)?))+\)'

class INT:
    name = 'INT'
    template = r'-*[0-9]+'

class FLOAT:
    name = 'FLAOT'
    template = r'-*[0-9]+.[0-9]+'

class BOOL:
    name = 'BOOL'
    template = r'True|False'

class VAR:
    name = 'VAR'
    #template = r'\b(?:(?!(True|False|if|while))[a-zA-Z])+\b'
    template = r'[A-Z]+'

class FROM_KEYBOARD:
    name = 'FROM_KEYBOARD'
    template = r'from_keyboard'






class COMMENT:

    name = 'COMMENT'
    template = re.compile(' *!!![^\n]*\n')

    def solution(cycle_line, line_number):
        return line_number

class IF:

    def __init__(self, name, line, line_number):
        self.name = name
        self.line = line
        self.line_number = line_number

    template = re.compile(f' *if ({INT.template}|{BOOL.template}|{VAR.template}|{expression_template}): *\n')
    left_brace = 0
    right_brace = 0
    condition = 0

    def check(line, line_number):
        braces_arr.append(IF(f'if_{line_number}', line, line_number))


    def solution(cycle_line, line_number):

        IF.condition = ''.join(re.findall(f'({INT.template}|{BOOL.template}|{VAR.template}|{expression_template})',  cycle_line))

        from E_reshalka import reshalka_func

        if re.fullmatch(f'{expression_template}', IF.condition):
            IF.condition = reshalka_func(IF.condition, line_number)

        for i in var_dict:

            if f'{i}' in IF.condition:

                IF.condition = IF.condition.replace(f'{i}', var_dict[f'{i}'])

        if IF.condition == 'False' or IF.condition == '0':
            
            for i in range(len(braces_arr)):

                if braces_arr[i].line_number == line_number:

                    line_number = braces_arr[i].right_brace

                    return int(line_number)
        else:
            return line_number

class WHILE:

    def __init__(self, name, line, line_number):
        self.name = name
        self.line = line
        self.line_number = line_number

    template = re.compile(f' *while ({INT.template}|{BOOL.template}|{VAR.template}|{expression_template}): *\n')
    left_brace = 0
    right_brace = 0
    condition = 0

    def check(line, line_number):
        braces_arr.append(WHILE(f'while_{line_number}', line, line_number))



    def solution(cycle_line, line_number):

        WHILE.condition = ''.join(re.findall(f'({INT.template}|{BOOL.template}|{VAR.template}|{expression_template})',  cycle_line))

        from E_reshalka import reshalka_func

        if re.fullmatch(f'{expression_template}', WHILE.condition):
            WHILE.condition = reshalka_func(WHILE.condition, line_number)
       
        for i in var_dict:

            if f'{i}' in WHILE.condition:

                WHILE.condition = WHILE.condition.replace(f'{i}', var_dict[f'{i}'])

        if WHILE.condition == 'False' or WHILE.condition == '0':
            
            for i in range(len(braces_arr)):

                if braces_arr[i].line_number == line_number:

                    line_number = int(braces_arr[i].right_brace)

                    return line_number
        else:
            return line_number

class FROM_TO:

    def __init__(self, name, line, line_number):
        self.name = name
        self.line = line
        self.line_number = line_number

    template = re.compile(f' *from {INT.template} to {INT.template}: *\n')
    left_brace = 0
    right_brace = 0

    def check(line_number):
        braces_arr.append(FROM_TO(f'from_to_{line_number}', line_number))



    def solution(cycle_line, line_number):
        return line_number

class BRACES_L:

    name = 'BRACES_L'
    template = re.compile(' *{ *\n')

    def check(line, line_number):

        if len(braces_arr) == 0:
            print(f'Ошибка в строке {line_number}!', 'Использование фигурных скобок без оператора!')
            exit() 
        
        for i in range(len(braces_arr)):
            
            if braces_arr[i].left_brace == 0:
                braces_arr[i].left_brace = line_number
                return
        
        print(f'Ошибка в строке {line_number}!', 'Некорректное использование фигурных скобок!')
        exit()
            

    def solution(cycle_line, line_number):
        return line_number

class BRACES_R:

    name = 'BRACES_R'
    template = re.compile(' *} *\n')

    def check(line, line_number):

        if len(braces_arr) == 0:
            print(f'Ошибка в строке {line_number}!', 'Использование фигрурных скобок без оператора!')
            exit()

        braces_arr.reverse()

        for i in range(len(braces_arr)):
            if braces_arr[i].left_brace != 0 and braces_arr[i].right_brace == 0:
                braces_arr[i].right_brace = line_number
                braces_arr.reverse()
                return

        print(f'Ошибка в строке {line_number}!', 'Некорректное использование фигурных скобок!')
        exit()

    def solution(cycle_line, line_number):

        for i in range(len(braces_arr)):

            if braces_arr[i].right_brace == line_number and re.match(r'while', braces_arr[i].line):

                line_number = int(braces_arr[i].line_number) - 1

                return line_number

        return line_number

class ASSIGNMENT:

    name = 'ASSIGNMENT'
    template = re.compile(f' *{VAR.template} = ({INT.template}|{FLOAT.template}|{BOOL.template}|{VAR.template}|{FROM_KEYBOARD.template}|{expression_template}) *\n')

    def solution(cycle_line, line_number):

        var_name = cycle_line[:cycle_line.find("=")-1].replace(' ', '')
        var_content = cycle_line[cycle_line.find("=")+2:].replace(' ', '').replace('\n', '')

        from E_reshalka import reshalka_func

        if re.fullmatch(f'{expression_template}', var_content):
            var_content = reshalka_func(var_content, line_number)

        if re.fullmatch(f'{FROM_KEYBOARD.template}', var_content):
            var_content = input()

        var_dict[var_name] = var_content

        return line_number

class ON_SCREEN:

    name = 'ON_SCREEN'
    template = re.compile(' *on_screen\[.*\] *\n')

    def solution(cycle_line, line_number):

        screen_text = cycle_line[cycle_line.find('[')+1:cycle_line.rfind(']')]

        for i in var_dict:

            if f'[{i}]' in screen_text:

                screen_text = screen_text.replace(f'{i}', var_dict[f'{i}'])

        screen_text = screen_text.replace('[','').replace(']','')

        print(screen_text)

        return line_number
  
class EMPTY_STRING:

    name = 'EMPTY_STRING'
    template = re.compile(' *\n')

    def solution(cycle_line, line_number):
        
        return line_number

class END:

    name = 'END'
    template = re.compile(' *end *(\n)?')

    def solution(cycle_line, line_number):
        exit()

possible_lines = [COMMENT, IF, WHILE, FROM_TO, BRACES_L, BRACES_R, ASSIGNMENT, ON_SCREEN, EMPTY_STRING, END]

braces_lines = [IF, WHILE, FROM_TO, BRACES_L, BRACES_R]



















































# ————————————————————————————————— code graveyard —————————————————————————————————

# ———————————————————————————————————————††††———————————————————————————————————————
# ———————————————————————————————————————††††———————————————————————————————————————
# ———————————————————————————————————††††††††††††———————————————————————————————————
#————————————————————————————————————††††††††††††———————————————————————————————————
# ———————————————————————————————————————††††———————————————————————————————————————
# ———————————————————————————————————————††††———————————————————————————————————————
# ———————————————————————————————————————††††———————————————————————————————————————
# ———————————————————————————————————————††††———————————————————————————————————————
# ———————————————————————————————————————††††———————————————————————————————————————
# ———————————————————————————————————————††††———————————————————————————————————————


# class OTHER:

#     name = 'OTHER'
#     template = re.compile('[^\n]*\n')

#     def solution(cycle_line, line_number):

#         print(f'Ошибка в строке {line_number}! Невозможная строка!')
#         exit()   


# int_t = '-*[0-9]+'
# float_t = '-*[0-9]+.[0-9]+'
# bool_t = 'True|False'
# condition = f'{int_t}:|if{float_t}:|if{bool_t}'



# string_templates = [

#     (r'!!![^\n]*',                                           'comment'),
#     (rf'if({int_t}|{float_t}|{bool_t}):',                    'if'),
#     (rf'while({int_t}|{float_t}|{bool_t}):',                 'while'),
#     (rf'from{int_t}to{int_t}:',                              'from_to'),
#     (rf'[A-Za-z]+=({int_t}|{float_t}|{bool_t})',             'assignment'),
#     (r'',                                                    'empty_string')

# ]



# var_templates = [

#     (r'-*[0-9]+',                                            'int'),
#     (r'-*[0-9]+.[0-9]+',                                     'float'),
#     (r'True|False',                                          'bool'),
#     (r'[A-Za-z]+',                                           'var'),

# ]



# s = 'hasd=a'

# result = ASSIGNMENT.template.fullmatch(s)

# print(result)

#str_t = '\'[^\n]*\''
#   (r'\'[^\n]*\'',           'str'),




# condition = re.search(f'({INT.template}|{BOOL.template})', cycle_line)

# if condition != 'False' and condition != '0':

#     braces_arr = code_arr[:]
#     braces_arr = braces_arr[line_number + 1:]

#     first_left_brace_line = line_number + 1

#     if re.fullmatch(r' *{ *', braces_arr[0]) == False:
#         print(f'Ошибка в строке {line_number}! ', 'Нет { после if!')
#         exit()


#     left_braces = 0
#     right_braces = 0

#     for i in range(len(braces_arr)):

#         if re.fullmatch(r' *{ *', braces_arr[i]):

#             left_bracse += 1

#         if re.fullmatch(r' *} *', braces_arr[i]):

#             right_brace += 1

#         if left_braces < right_brace:

#             print(f'Ошибка в строке {line_number}! ', 'Некорректное употребление }!')
#             exit()

#         if left_braces == right_braces:

#             code_arr[first_left_brace_line] = '\n'
#             code_arr[first_left_brace_line] = '\n'


#import sys
#filename = sys.argv[1]
#filename = 'code.txt'

# print('\n\nИтоги:')
# print(var_dict)
# for i in range(len(braces_arr)):
#     print(braces_arr[i].line)
#     print(braces_arr[i].line_number)
#     print(braces_arr[i].left_brace)
#     print(braces_arr[i].right_brace)




# ..... (¯`v´¯)♥
# .......•.¸.•´
# ....¸.•´
# ... (
#  ☻/
# /▌ ♥♥
# / \ ♥♥







