def restar_matrices(m1, m2):
    filas = len(m1)
    cols = len(m1[0])
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(cols):
            fila.append(m1[i][j] - m2[i][j])
        resultado.append(fila)
    return resultado

print(restar_matrices(m1, m2))
