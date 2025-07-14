def trasponer_matriz(matriz):
    filas = len(matriz)
    cols = len(matriz[0])
    resultado = []
    for j in range(cols):
        fila = []
        for i in range(filas):
            fila.append(matriz[i][j])
        resultado.append(fila)
    return resultado

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print(trasponer_matriz(matriz))
