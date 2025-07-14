def inversa_2x2(matriz):
    a, b = matriz[0]
    c, d = matriz[1]
    det = a * d - b * c
    if det == 0:
        return None 
    inv = [
        [d/det, -b/det],
        [-c/det, a/det]
    ]
    return inv

matriz = [
    [4, 7],
    [2, 6]
]

print(inversa_2x2(matriz))
