def somar(*args):
    return sum(args)

def multiplicar(*args):
    result = 1
    for num in args:
        result = num * result
    return result

if __name__ == '__main__':
    print('Este é um modulo não deve ser executado diretamente')