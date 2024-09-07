filas= 2
columnas=2

matriz1=[]
matriz2=[]
multiplicacion_matriz=[[0,0],[0,0]]

print("Elementos de la primera matriz")
for i in range(filas):
    fila=[]
    for j in range(columnas):
        valor=float(input(f"Ingrese el valor del Elemento [{i+1}][{j+1}] :"))

        fila.append(valor)
    matriz1.append(fila)


print("Elementos de la segunda matriz")
for i in range(filas):
    fila=[]
    for j in range(columnas):
        valor=float(input(f"Ingrese el valor del Elemento [{i+1}][{j+1}] :"))

        fila.append(valor)
    matriz2.append(fila)

for i in range(filas):
    for j in range(columnas):
        multiplicacion_matriz[i][j] = (matriz1[i][0] * matriz2[0][j] +
                           matriz1[i][1] * matriz2[1][j])

#Mostrar la matriz resultante
print(f"\n La primera matriz ingresada es: ")
for fila in matriz1:
    print(fila)

#Mostrar la matriz resultante
print(f"\n La segunda matriz ingresada es: ")
for fila in matriz2:
    print(fila)

#Mostrar la multiplicacion
print(f"\n El resultado de la multiplicacion de las dos matrices ingresadas es: ")
for fila in multiplicacion_matriz:
    print(fila)

