
# Va a ir intercambiando los elementos del arbol
def swap(lst, i , j):
    lst[i], lst[j] = lst[j], lst[i]

# Sacar el elemento raiz
def siftDown(lst, i, upper):
    while (True):

        l, r = i*2+1, i*2+2

        if max(l, r) < upper:
            if lst[i] >= max(lst[l], lst[r]):
                break

            elif lst[l] > lst[r]:
                swap(lst, i, l)
                i = l
            else :
                swap(lst, i, r)

        elif l < upper: 

            if lst[l] > lst[i]:
                swap(lst, i, l)
                i = l
            else: 
                break
        
        elif r < upper: 

            if lst[r] > lst[i]:
                swap(lst, i, r)
                i = r
            
            else: 
                break

        else: 
            break

# Función principal 
def heapsort(lst):
    for j in range(len(lst)-2//2, -1, -1):
        siftDown(lst, j , len(lst))

    for end in range(len(lst)-1, 0, -1):
        swap(lst, 0, end)
        siftDown(lst, 0, end)

# Test 

lst = [5, 16, 18, 20, 43, 90, 21, 6, 1, 32, 24, 6, 7]
heapsort(lst)
print(lst)