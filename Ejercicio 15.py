def sumar_matrices(m1, m2):
    filas = len(m1)
    cols = len(m1[0])
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(cols):
            fila.append(m1[i][j] + m2[i][j])
        resultado.append(fila)
    return resultado

m1 = [
    [1.1, 2.2],
    [3.3, 4.4]
]

m2 = [
    [5.5, 6.6],
    [7.7, 8.8]
]

print(sumar_matrices(m1, m2))
