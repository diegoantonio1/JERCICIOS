def encontrar_palindromos(palabras):
    return [palabra for palabra in palabras if palabra == palabra[::-1]]

# Ejemplo de uso
palabras = ["ana", "oso", "hola", "level"]
resultado = encontrar_palindromos(palabras)
print(resultado)  