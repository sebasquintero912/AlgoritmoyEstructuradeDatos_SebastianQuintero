def rotar_izquierda(matriz):
    filas = len(matriz)
    cols = len(matriz[0])
    primero = matriz[0][0]

    for i in range(filas):
        for j in range(cols):
            if j == cols - 1:
                if i == filas - 1:
                    matriz[i][j] = primero
                else:
                    matriz[i][j] = matriz[i+1][0]
            else:
                matriz[i][j] = matriz[i][j+1]
    return matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotar_izquierda(matriz))
