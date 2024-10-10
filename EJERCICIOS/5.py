# 4. Inversión de Tuplas
def invertir_tuplas(lista_tuplas):
    return [tuple(reversed(t)) for t in lista_tuplas]

# Ejemplo de uso
tuplas = [(1, 2), (3, 4), (5, 6)]
print("\n4. Tuplas invertidas:")
print(invertir_tuplas(tuplas))