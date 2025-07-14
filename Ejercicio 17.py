def producto_matrices(m1, m2):
    filas_m1 = len(m1)
    cols_m1 = len(m1[0])
    filas_m2 = len(m2)
    cols_m2 = len(m2[0])

    if cols_m1 != filas_m2:
        return None  

    resultado = []
    for i in range(filas_m1):
        fila = []
        for j in range(cols_m2):
            suma = 0
            for k in range(cols_m1):
                suma += m1[i][k] * m2[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

m1 = [
    [1, 2, 3],
    [4, 5, 6]
]

m2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

print(producto_matrices(m1, m2))
