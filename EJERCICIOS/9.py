def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    medio = len(arr) // 2
    izquierda = merge_sort(arr[:medio])
    derecha = merge_sort(arr[medio:])
    
    return merge(izquierda, derecha)

def merge(izq, der):
    resultado = []
    i = j = 0
    
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    
    return resultado

# Ejemplo
numeros = [5, 3, 8, 6, 2]
resultado = merge_sort(numeros)
print(resultado)  