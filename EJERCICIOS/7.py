def es_subconjunto(conjunto1, conjunto2):
    return conjunto1.issubset(conjunto2)

# Ejemplo de uso
conjunto1 = {1, 2, 3}
conjunto2 = {1, 2, 3, 4, 5}
resultado = es_subconjunto(conjunto1, conjunto2)
print(resultado)  