def columna_maximo_en_fila(matriz, fila):
    maximo = matriz[fila][0]
    indice = 0
    for i in range(1, len(matriz[fila])):
        if matriz[fila][i] > maximo:
            maximo = matriz[fila][i]
            indice = i
    return indice

matriz = [
    [0, 4, 2, 1],
    [5, 0, 3, 2],
    [0, 2, 0, 1],
    [1, 0, 2, 0]
]
print(columna_maximo_en_fila(matriz, 1))  
