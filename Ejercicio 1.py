def suma_total(matriz):
    total = 0
    for fila in matriz:
        for elemento in fila:
            total += elemento
    return total

matriz = [
    [0, 4, 2, 1],
    [5, 0, 3, 2],
    [0, 2, 0, 1],
    [1, 0, 2, 0]
]

print(suma_total(matriz))  
