def somar(*args)->float:
    return sum(args)

def subtrair(*args)->float:
    resultado = args[0]
    for num in args[1:]:
        resultado -= num
    return resultado

def dividir(nums_dict):
    div = nums_dict['numerador'] / nums_dict['denominador']
    return div
    
def multiplicar(*args):
    result = 1
    for num in args:
        result = result * num
    return result
        