
def dividir(array):

    largo = len(array)//2

    if largo == 0: 
        return array
    
    izquierda = array[0:largo]
    derecha = array[largo:]

    print(array)

    return dividir(izquierda) and dividir(derecha)

lista = [1,2,3,4,5,6,7,8,9,10,11,12]

def merge(array, izq, der): 
    pass

print(dividir(lista))