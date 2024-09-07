<<<<<<< HEAD
filas=2
columnas=3

matriz=[]
print("\n Rellenar la siguiente matriz")

for i in range(filas):
    fila=[]
    for j in range(columnas):
        valor=float(input(f"Elemento[{i+1}][{j+1}]: "))
        
        fila.append(valor)
    matriz.append(fila)

matriz_transpuesta = [[0] * filas for _ in range(columnas)]

# Llenar la matriz transpuesta
for i in range(filas):
    for j in range(columnas):
        matriz_transpuesta[j][i] = matriz[i][j]


#Mostrar la matriz resultante
print(f"\n La matriz ingresada es: ")
for fila in matriz:
    print(fila)

#Mostrar matriz transpuesta

print(f"\n La matriz transpuesta es: ")
for fila in matriz_transpuesta:
    print(fila) 
=======
filas=2
columnas=3

matriz=[]
print("\n Rellenar la siguiente matriz")

for i in range(filas):
    fila=[]
    for j in range(columnas):
        valor=float(input(f"Elemento[{i+1}][{j+1}]: "))
        
        fila.append(valor)
    matriz.append(fila)

#Mostrar la matriz resultante
print(f"\n La matriz ingresada es: ")
for fila in matriz:
    print(fila)
  
>>>>>>> 5b78f254765360b52878af115752c13b19febdab
