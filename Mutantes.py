def is_mutant(dna):
    # Verificar que el ADN tiene exactamente 6 filas y 6 columnas
    if len(dna) != 6 or any(len(row) != 6 for row in dna):
        return False

    # Verificar que cada caracter en el ADN sea válido (A, T, C, G)
    valid_chars = set('ATCG')
    if any(any(char.upper() not in valid_chars for char in row) for row in dna):
        return False

    # Lógica para determinar si el ADN es mutante
    # Verificar horizontalmente, verticalmente y diagonalmente
    for i in range(6):
        for j in range(3):
            # Verificar horizontalmente
            if dna[i][j] == dna[i][j + 1] == dna[i][j + 2] == dna[i][j + 3]:
                return True
            # Verificar verticalmente
            if dna[j][i] == dna[j + 1][i] == dna[j + 2][i] == dna[j + 3][i]:
                return True
            # Verificar diagonalmente (derecha)
            if i < 3 and dna[i][j] == dna[i + 1][j + 1] == dna[i + 2][j + 2] == dna[i + 3][j + 3]:
                return True
            # Verificar diagonalmente (izquierda)
            if i < 3 and dna[i][j + 3] == dna[i + 1][j + 2] == dna[i + 2][j + 1] == dna[i + 3][j]:
                return True

    # Si no se cumplen las condiciones anteriores, el ADN no es mutante
    return False

def solicitar_matriz_al_usuario():
    tabla = [[' ' for _ in range(6)] for _ in range(6)]
    for i in range(6):
        for j in range(6):
            mensaje = f"Ingrese un valor para la posición ({i+1}, {j+1}): "
            dato = input(mensaje).upper()

            # Verificar que el dato ingresado sea uno de los permitidos (A, T, C, G)
            while dato not in ['A', 'T', 'C', 'G']:
                print("Por favor, ingrese un valor válido (A, T, C, G).")
                dato = input(mensaje).upper()

            # Almacenar el dato en la tabla
            tabla[i][j] = dato

    return tabla

# Solicitar al usuario que complete la matriz
matriz_ingresada = solicitar_matriz_al_usuario()

# Imprimir la matriz resultante
print("\nMatriz ingresada por el usuario:")
for fila in matriz_ingresada:
    print(fila)

# Comprobar si el ADN es mutante
resultado = is_mutant(matriz_ingresada)
print("\n¿Es mutante?", resultado)
