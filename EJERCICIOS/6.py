def valor_mas_frecuente(numeros):
    # Creamos un diccionario para contar la frecuencia de cada número
    frecuencias = {}
    
    # Contamos la frecuencia de cada número
    for num in numeros:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1
    
    # Encontramos el número con la mayor frecuencia
    max_frecuencia = 0
    valor_max_frecuencia = None
    
    for num, freq in frecuencias.items():
        if freq > max_frecuencia:
            max_frecuencia = freq
            valor_max_frecuencia = num
    
    return valor_max_frecuencia

# Ejemplo
numeros = [1, 2, 3, 1, 2, 1]
resultado = valor_mas_frecuente(numeros)
print(resultado) 