def is_mutant(dna):
    if len(dna) != 6 or any(len(row) != 6 for row in dna):
        return False

    valid_chars = set('ATCG')
    if any(any(char.upper() not in valid_chars for char in row) for row in dna):
        return False

    for i in range(6):
        for j in range(3):
            if dna[i][j] == dna[i][j + 1] == dna[i][j + 2] == dna[i][j + 3]:
                return True
            if dna[j][i] == dna[j + 1][i] == dna[j + 2][i] == dna[j + 3][i]:
                return True
            if i < 3 and dna[i][j] == dna[i + 1][j + 1] == dna[i + 2][j + 2] == dna[i + 3][j + 3]:
                return True
            if i < 3 and dna[i][j + 3] == dna[i + 1][j + 2] == dna[i + 2][j + 1] == dna[i + 3][j]:
                return True

    return False

def solicitar_matriz_al_usuario():
    tabla = [[' ' for _ in range(6)] for _ in range(6)]
    for i in range(6):
        for j in range(6):
            mensaje = f"Ingrese un valor para la posición ({i+1}, {j+1}): "
            dato = input(mensaje).upper()

            while dato not in ['A', 'T', 'C', 'G']:
                print("Por favor, ingrese un valor válido (A, T, C, G).")
                dato = input(mensaje).upper()

            tabla[i][j] = dato

    return tabla

matriz_ingresada = solicitar_matriz_al_usuario()

print("\nMatriz ingresada por el usuario:")
for fila in matriz_ingresada:
    print(fila)

resultado = is_mutant(matriz_ingresada)
print("\n¿Es mutante?", resultado)
