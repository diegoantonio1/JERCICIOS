def calcular_frecuencia(numeros):
    frecuencias = {}
    for num in numeros:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    return frecuencias

# Ejemplo
numeros = [1, 1, 2, 3, 3, 3]
print("\n2. Frecuencia de números:")
print(calcular_frecuencia(numeros))