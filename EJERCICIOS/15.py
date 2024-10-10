def clave_valor_maximo(diccionario):
    return max(diccionario, key=diccionario.get)

# Ejemplo de uso
diccionario = {'a': 10, 'b': 20, 'c': 5}
resultado = clave_valor_maximo(diccionario)
print(resultado)  # Salida: 'b'
