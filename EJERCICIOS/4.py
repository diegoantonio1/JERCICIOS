def filtrar_palabras_largas(palabras, longitud):
    return [palabra for palabra in palabras if len(palabra) > longitud]

# Ejemplo de uso
palabras = ["hola", "mundo", "python", "programación"]
longitud = 5
print("\n3. Palabras largas:")
print(filtrar_palabras_largas(palabras, longitud))