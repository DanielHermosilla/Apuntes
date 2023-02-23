
def dividir(array):

    largo = len(array)//2

    if largo == 0: 
        return array
    
    print(array)
    return dividir(array[0:largo])

lista = [1,2,3,4,5,6,7,8,9,10,11,12]

print(dividir(lista))