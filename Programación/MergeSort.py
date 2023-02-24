


def dividir(array):

    largo = len(array)//2
    izquierda = array[0:largo]
    derecha = array [largo:]

    while len(izquierda) != 1 or len(derecha) != 1: 
        print(array)
        return dividir(izquierda) and dividir(derecha)
    
l = [33,44,11,88,77,33,22,11,99]

print(dividir(l))