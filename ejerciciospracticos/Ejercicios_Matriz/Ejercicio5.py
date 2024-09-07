# Solicitar los datos para una matriz 3x3
print("Ingrese los elementos de la matriz 3x3: ")
matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        valor = float(input(f"Elemento [{i+1},{j+1}]: "))
        fila.append(valor)
    matriz.append(fila)

# Mostrar la matriz ingresada
print("\nMatriz 3x3:")
for fila in matriz:
    print(fila)

# Mostrar los elementos de la diagonal principal
print("\nElementos de la diagonal principal:")
for i in range(3):
    print(matriz[i][i])