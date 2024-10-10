def eliminar_menores(numeros, limite):
    return [num for num in numeros if num >= limite]

# Ejemplo 
numeros = [1, 2, 3, 4, 5]
limite = 3
resultado = eliminar_menores(numeros, limite)
print(resultado) 