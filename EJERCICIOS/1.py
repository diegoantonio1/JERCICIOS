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