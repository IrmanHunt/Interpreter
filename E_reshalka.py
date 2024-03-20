from B_sklad import *

def exp_1_func(result, line_number):

    while re.fullmatch(f'{exp_1_template}', result) != None:

        while re.search(r'\d\-\d', result):

            tak_nado = tak_nado_2 = re.search(r'\d\-\d', result).group(0)
            tak_nado_2 = tak_nado.replace('-', '+-')
            result = result.replace(tak_nado, tak_nado_2)
        
        if re.search(f'{figure_template}[*/]{figure_template}', result):

            mini_result = mini_result_2 = re.search(f'{figure_template}[*/]{figure_template}', result).group(0)
            
            figure_1 =  re.findall(f'({figure_template})', mini_result)[0][0]
            figure_2 =  re.findall(f'({figure_template})', mini_result)[1][0]

            if '*' in mini_result:

                mini_result = str(float(figure_1) * float(figure_2))

                result = result.replace(mini_result_2, mini_result)

                continue
            
            elif '/' in mini_result:

                if figure_2 == '0':
                    print(f'Ошибка в строке {line_number}! Деление на 0!')
                    exit()

                mini_result = str(float(figure_1) / float(figure_2))

                result = result.replace(mini_result_2, mini_result)

                continue

        if re.search(f'{figure_template}[+-]{figure_template}', result):

            result = result.replace('--', '+')

            mini_result = mini_result_2 = re.search(f'{figure_template}[+-]{figure_template}', result).group(0)

            figure_1 =  re.findall(f'({figure_template})', mini_result)[0][0]
            figure_2 =  re.findall(f'({figure_template})', mini_result)[1][0]

            mini_result = str(float(figure_1) + float(figure_2))

            result = result.replace(mini_result_2, mini_result)

            continue

    result = result.replace('(', '').replace(')', '')

    return result

def exp_2_func(result, line_number):
    
    while re.fullmatch(f'{exp_2_template}', result) != None:
            
            if re.search(f'({figure_template}|{bool_template})[><=]({figure_template}|{bool_template})', result):

                mini_result = mini_result_2 = re.search(f'({figure_template}|{bool_template})[><=]({figure_template}|{bool_template})', result).group(0)

                figure_bool_1 =  re.findall(f'({figure_template}|{bool_template})', mini_result)[0][0]
                figure_bool_2 =  re.findall(f'({figure_template}|{bool_template})', mini_result)[1][0]

                if re.findall(f'({figure_template})', figure_bool_1):
                    figure_bool_1 = float(figure_bool_1)
                elif figure_bool_1 == 'False':
                    figure_bool_1 = False
                else:
                    figure_bool_1 = bool(figure_bool_1)

                if re.findall(f'({figure_template})', figure_bool_2):
                    figure_bool_2 = float(figure_bool_2)
                elif figure_bool_2 == 'False':
                    figure_bool_2 = False
                else:
                    figure_bool_2 = bool(figure_bool_2)

                if '>' in mini_result:

                    mini_result = str(figure_bool_1 > figure_bool_2)

                    result = result.replace(mini_result_2, mini_result)

                    continue
                
                elif '<' in mini_result:

                    mini_result = str(figure_bool_1 < figure_bool_2)

                    result = result.replace(mini_result_2, mini_result)

                    continue

                elif '=' in mini_result:

                    mini_result = str(figure_bool_1 == figure_bool_2)

                    result = result.replace(mini_result_2, mini_result)

                    continue

            if re.search(f'({figure_template}|{bool_template})a({figure_template}|{bool_template})', result):

                mini_result = mini_result_2 = re.search(f'({figure_template}|{bool_template})a({figure_template}|{bool_template})', result).group(0)

                figure_bool_1 =  re.findall(f'({figure_template}|{bool_template})', mini_result)[0][0]
                figure_bool_2 =  re.findall(f'({figure_template}|{bool_template})', mini_result)[1][0]
                
                if re.findall(f'({figure_template})', figure_bool_1):
                    figure_bool_1 = float(figure_bool_1)
                elif figure_bool_1 == 'False':
                    figure_bool_1 = False
                else:
                    figure_bool_1 = bool(figure_bool_1)

                if re.findall(f'({figure_template})', figure_bool_2):
                    figure_bool_2 = float(figure_bool_2)
                elif figure_bool_2 == 'False':
                    figure_bool_2 = False
                else:
                    figure_bool_2 = bool(figure_bool_2)

                mini_result = str(figure_bool_1 and figure_bool_2)

                result = result.replace(mini_result_2, mini_result)

                continue

            if re.search(f'({figure_template}|{bool_template})o({figure_template}|{bool_template})', result):

                mini_result = mini_result_2 = re.search(f'({figure_template}|{bool_template})o({figure_template}|{bool_template})', result).group(0)

                figure_bool_1 =  re.findall(f'({figure_template}|{bool_template})', mini_result)[0][0]
                figure_bool_2 =  re.findall(f'({figure_template}|{bool_template})', mini_result)[1][0]

                if re.findall(f'({figure_template})', figure_bool_1):
                    figure_bool_1 = float(figure_bool_1)
                else:
                    figure_bool_1 = bool(figure_bool_1)

                if re.findall(f'({figure_template})', figure_bool_2):
                    figure_bool_2 = float(figure_bool_2)
                else:
                    figure_bool_2 = bool(figure_bool_2)

                mini_result = str(figure_bool_1 or figure_bool_2)

                result = result.replace(mini_result_2, mini_result)

                continue

    result = result.replace('(', '').replace(')', '')

    return result

def reshalka_func(expression, line_number):

    for i in var_dict:
        if f'{i}' in expression:
            expression = expression.replace(f'{i}', var_dict[f'{i}'])

    expression = expression.replace(' ', '')
    expression = expression.replace('and','a')
    expression = expression.replace('or', 'o')

    while re.fullmatch(rf'{INT.template}|{FLOAT.template}|{BOOL.template}', expression) == None:
    
        if re.search(f'{exp_1_template}', f'{expression}'):

            result = result_template = re.search(f'{exp_1_template}', f'{expression}').group(0)
            result = exp_1_func(result, line_number)

        elif re.search(f'{exp_2_template}', f'{expression}'):

            result = result_template = re.search(f'{exp_2_template}', f'{expression}').group(0)
            result = exp_2_func(result, line_number)

        else:
            print(f'Ошибка в строке {line_number}! Некорретное выражение!')
            exit()


        expression = expression.replace(result_template, result)

    return expression