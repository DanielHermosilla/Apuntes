
def swap(lst, i , j):

	lst[i], lst[j] = lst[j], lst[i]
        
def dividir(array):

    largo = len(array)//2
    izquierda = array[0:largo]
    derecha = array[largo:]

    if len(izquierda) == 1 or len(derecha) == 1:
        return merge(array, izquierda, derecha)
         
    return dividir(izquierda) and dividir(derecha)

lista = [11,33,44,77,88,99,55,44,33]

def merge(array, izq, der): 

    for i in range(0,min(len(izq),len(der)),2):

        if izq[i] > der[i]:
            array[i] = der[i]
            array[i+1] = izq[i]

        else: 
            array[i] = izq[i]
            array[i+1] = der[i]

    return array


print(dividir(lista))