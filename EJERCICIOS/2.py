def combinar_diccionarios(dic1, dic2):
    resultado = dic1.copy()  # Comenzamos con una copia de dic1
    for clave, valor in dic2.items():
        if clave in resultado:
            resultado[clave] += valor  # Sumamos los valores si la clave ya existe
        else:
            resultado[clave] = valor  
    return resultado

# Ejemplo de uso
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
resultado = combinar_diccionarios(dic1, dic2)
# Salida: {'a': 1, 'b': 5, 'c': 4}
print(resultado)  