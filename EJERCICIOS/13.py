def duplicar_elementos(numeros):
    return [num for num in numeros for _ in range(2)]

# Ejemplo de uso
numeros = [1, 2, 3]
resultado = duplicar_elementos(numeros)
print(resultado)  