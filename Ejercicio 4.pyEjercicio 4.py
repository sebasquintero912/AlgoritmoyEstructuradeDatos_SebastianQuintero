def fila_maximo_en_columna(matriz, columna):
    maximo = matriz[0][columna]
    indice = 0
    for i in range(1, len(matriz)):
        if matriz[i][columna] > maximo:
            maximo = matriz[i][columna]
            indice = i
    return indice

matriz = [
    [0, 4, 2, 1],
    [5, 0, 3, 2],
    [0, 2, 0, 1],
    [1, 0, 2, 0]
]

print(fila_maximo_en_columna(matriz, 2))  
