import func_calc as calc

def pegar_lista_num()->list:
    lst_num = []
    i = 1
    while True:
        try:
            str_num = input(f'Digite o {i}º número, digite (=) para finalizar')
            if str_num == '=':
                break
            else:
                num = float(str_num)
                lst_num.append(num)
        except ValueError:
            print('Por valor digite apenas números ou =')
    return lst_num
def pegar_numeros_para_divisao()->dict:
    nums_dct = {'numerador':0,'denominador':1}
    while True:
        try:
            num = float(input('Digite o numerador: '))
            den = float(input('Digite o denominador: '))
            if den == 0:
                print('Denominador não pode ser 0')
            else:
                nums_dct = dict(numerador = num, denominador = den)
                break
        except ValueError:
            print('Por favor digitar apenas numeros')
    return nums_dct



            

while True:
    print('Entre as opções')
    try:
        flg = int(input('\
                    \n(1)Somar\
                    \n(2)Subtrair\
                    \n(3)Multiplicar\
                    \n(4)Dividir dois números\
                    \n(0)Finalizar\
                    \nDigite sua operação: '
                    ))
        match flg:
            case 1:
                lst_num = pegar_lista_num()
                soma = calc.somar(lst_num)
                print(f'A soma dos números {lst_num} é = {soma}')
            case 2:
                lst_num = pegar_lista_num()
                subtracao = calc.subtrair(lst_num)
                print(f'A subtração dos números {lst_num} é = {subtracao}')
            case 3:
                lst_num = pegar_lista_num()
                multicacao = calc.multiplicar(lst_num)
                print(f'A multiplicação dos números {lst_num} é = {multicacao}')
            case 4:
                nums_dct = {'numerador':0,'denominador':1}
                nums_dct = pegar_numeros_para_divisao()
                div = calc.dividir(nums_dct)
                print(f'A divisão dos números {nums_dct["numerador"]}/{nums_dct["denominador"]} é = { div}')
                # multicacao = calc.multiplicar(lst_num)
                # print(f'A multiplicação dos números {lst_num} é = {multicacao}')
    except ValueError:
        print('Por valor digitar apenas as opções indicadas.')
        