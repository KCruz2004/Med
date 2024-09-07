#Solicitar el numero de filas y columnas
filas=int(input("Ingrese el numero de filas: "))
columnas=int(input("Ingrese el numero de columnas: "))

#Inicializar la matriz
matriz=[]
print("\n Por favor ingrese los valores de la matriz")

#LLenar la matriz con los valores ingresados por el usuario
for i in range(filas):
    fila=[]
    for j in range(columnas):
        valor=float(input(f"Elemento[{i+1}][{j+1}]: "))
        fila.append(valor)
        matriz.append(fila)

#Mostrar la matriz resultante
print("\n La matriz ingresada es: ")
for fila in matriz: 
    print(fila)