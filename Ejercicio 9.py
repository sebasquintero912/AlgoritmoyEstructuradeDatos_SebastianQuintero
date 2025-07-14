def suma_fila(matriz, fila):
    total = 0
    for num in matriz[fila]:
        total += num
    return total

matriz = [
    [0, 4, 2, 1],
    [5, 0, 3, 2],
    [0, 2, 0, 1],
    [1, 0, 2, 0]
]

print(suma_fila(matriz, 0)) 
