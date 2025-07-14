def suma_columna(matriz, columna):
    total = 0
    for fila in matriz:
        total += fila[columna]
    return total

matriz = [
    [0, 4, 2, 1],
    [5, 0, 3, 2],
    [0, 2, 0, 1],
    [1, 0, 2, 0]
]

print(suma_columna(matriz, 1))  
