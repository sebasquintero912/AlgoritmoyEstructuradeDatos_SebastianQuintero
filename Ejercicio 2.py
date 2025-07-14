def cantidad_positivos(matriz):
    contador = 0
    for fila in matriz:
        for elemento in fila:
            if elemento > 0:
                contador += 1
    return contador

matriz = [
    [0, 4, 2, 1],
    [5, 0, 3, 2],
    [0, 2, 0, 1],
    [1, 0, 2, 0]
]

print(cantidad_positivos(matriz)) 
