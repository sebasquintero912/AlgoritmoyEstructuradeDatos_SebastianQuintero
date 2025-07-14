def rotar_derecha(matriz):
    filas = len(matriz)
    cols = len(matriz[0])
    ultimo = matriz[filas-1][cols-1]

    for i in reversed(range(filas)):
        for j in reversed(range(cols)):
            if j == 0:
                if i == 0:
                    matriz[i][j] = ultimo
                else:
                    matriz[i][j] = matriz[i-1][cols-1]
            else:
                matriz[i][j] = matriz[i][j-1]
    return matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotar_derecha(matriz))
