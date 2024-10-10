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