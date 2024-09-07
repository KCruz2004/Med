# Definir el tamaño de la matriz
n = 4

# Crear una matriz de tamaño 4x4 inicializada con ceros
matriz_identidad = [[0 for _ in range(n)] for _ in range(n)]

# Asignar 1 a los elementos de la diagonal principal
for i in range(n):
    matriz_identidad[i][i] = 1

# Mostrar la matriz identidad
print("Matriz identidad 4x4:")
for fila in matriz_identidad:
    print(fila)
    