def contar_palabras(frases):
    return {i: len(frase.split()) for i, frase in enumerate(frases)}

# Ejemplo de uso
frases = ["Hola mundo", "Python es genial", "Me gusta programar"]
resultado = contar_palabras(frases)
print(resultado)  # Salida: {0: 2, 1: 3, 2: 3}