def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 0:
        return (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
    else:
        return numeros_ordenados[n//2]

# Ejemplo de uso
numeros = [1, 3, 2, 4, 5]
resultado = calcular_mediana(numeros)
print(resultado)  # Salida: 3
