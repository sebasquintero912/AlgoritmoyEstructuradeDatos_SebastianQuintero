def intercambiar_columnas(matriz, c1, c2):
    for i in range(len(matriz)):
        matriz[i][c1], matriz[i][c2] = matriz[i][c2], matriz[i][c1]
    return matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(intercambiar_columnas(matriz, 0, 2))
