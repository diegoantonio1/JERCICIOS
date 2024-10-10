def flatten_list(lista_de_listas):
    return [item for sublist in lista_de_listas for item in sublist]

# Ejemplo
lista_de_listas = [[1, 2], [3, 4], [5]]
resultado = flatten_list(lista_de_listas)
print(resultado)  