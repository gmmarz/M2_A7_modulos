from calculadora import *

def init():
    while True:
        try:
            flg_op = int(input('Digite uma operação: 1-somar, 2-multiplicar, 0-Sair'))
            match flg_op:
                case 0:
                    print('Programa finalizado')
                case 1:
                    lst_num = []
                    
        except ValueError:
            print('Digite um das opções informadas')


        



if __name__ == '__main__':
    init()