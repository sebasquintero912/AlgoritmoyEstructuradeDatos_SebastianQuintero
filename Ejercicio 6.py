def columna_maximo_general(matriz):
    maximo = matriz[0][0]
    columna_max = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
                columna_max = j
    return columna_max

matriz = [
    [0, 4, 2, 1],
    [5, 0, 3, 2],
    [0, 2, 0, 1],
    [1, 0, 2, 0]
]

print(columna_maximo_general(matriz))  
