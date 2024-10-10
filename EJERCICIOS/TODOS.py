#EJER_1
def contar_ocurrencias(palabras):
    ocurrencias = {}
    for palabra in palabras:
        if palabra in ocurrencias:
            ocurrencias[palabra] += 1
        else:
            ocurrencias[palabra] = 1
    return ocurrencias
palabras = ["python", "java", "python", "c++"]
resultado = contar_ocurrencias(palabras)
print(resultado)

#EJER_2
def combinar_diccionarios(dic1, dic2):
    resultado = dic1.copy()  
    for clave, valor in dic2.items():
        if clave in resultado:
            resultado[clave] += valor  
        else:
            resultado[clave] = valor  
    return resultado

# Ejemplo 
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
resultado = combinar_diccionarios(dic1, dic2)
print(resultado)  

#EJER_3
def calcular_frecuencia(numeros):
    frecuencias = {}
    for num in numeros:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    return frecuencias

# Ejemplo
numeros = [1, 1, 2, 3, 3, 3]
print("\n2. Frecuencia de números:")
print(calcular_frecuencia(numeros))

#EJR_4
def filtrar_palabras_largas(palabras, longitud):
    return [palabra for palabra in palabras if len(palabra) > longitud]

# Ejemplo de uso
palabras = ["hola", "mundo", "python", "programación"]
longitud = 5
print("\n3. Palabras largas:")
print(filtrar_palabras_largas(palabras, longitud))

#EJER_5
def invertir_tuplas(lista_tuplas):
    return [tuple(reversed(t)) for t in lista_tuplas]

# Ejemplo de uso
tuplas = [(1, 2), (3, 4), (5, 6)]
print("\n4. Tuplas invertidas:")
print(invertir_tuplas(tuplas))

#EJER_6
def valor_mas_frecuente(numeros):
    
    frecuencias = {}
    
    
    for num in numeros:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1
    

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

#EJER_7
def es_subconjunto(conjunto1, conjunto2):
    return conjunto1.issubset(conjunto2)

# Ejemplo de uso
conjunto1 = {1, 2, 3}
conjunto2 = {1, 2, 3, 4, 5}
resultado = es_subconjunto(conjunto1, conjunto2)
print(resultado)  

#EJER_8
def agrupar_por_edad(personas):
    grupos = {}
    for persona in personas:
        edad = persona['edad']
        nombre = persona['nombre']
        if edad in grupos:
            grupos[edad].append(nombre)
        else:
            grupos[edad] = [nombre]
    return grupos

# Ejemplo
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "Carlos", "edad": 30}
]
resultado = agrupar_por_edad(personas)
print(resultado) 

#EJER_9
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

# Ejemplo de uso
numeros = [5, 3, 8, 6, 2]
resultado = merge_sort(numeros)
print(resultado)  

#EJER_10
def eliminar_menores(numeros, limite):
    return [num for num in numeros if num >= limite]

# Ejemplo 
numeros = [1, 2, 3, 4, 5]
limite = 3
resultado = eliminar_menores(numeros, limite)
print(resultado) 

#EJER_11
def flatten_list(lista_de_listas):
    return [item for sublist in lista_de_listas for item in sublist]

# Ejemplo
lista_de_listas = [[1, 2], [3, 4], [5]]
resultado = flatten_list(lista_de_listas)
print(resultado)  

#EJER_12
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
print(resultado) 

#EJER_13
def duplicar_elementos(numeros):
    return [num for num in numeros for _ in range(2)]

# Ejemplo de uso
numeros = [1, 2, 3]
resultado = duplicar_elementos(numeros)
print(resultado)  

#EJER_14
def contar_palabras(frases):
    return {i: len(frase.split()) for i, frase in enumerate(frases)}

# Ejemplo de uso
frases = ["Hola mundo", "Python es genial", "Me gusta programar"]
resultado = contar_palabras(frases)
print(resultado)  # Salida: {0: 2, 1: 3, 2: 3}

#EJER_15
def clave_valor_maximo(diccionario):
    return max(diccionario, key=diccionario.get)

# Ejemplo de uso
diccionario = {'a': 10, 'b': 20, 'c': 5}
resultado = clave_valor_maximo(diccionario)
print(resultado)  # Salida: 'b'

#EJER_16
def encontrar_palindromos(palabras):
    return [palabra for palabra in palabras if palabra == palabra[::-1]]

# Ejemplo de uso
palabras = ["ana", "oso", "hola", "level"]
resultado = encontrar_palindromos(palabras)
print(resultado)  

