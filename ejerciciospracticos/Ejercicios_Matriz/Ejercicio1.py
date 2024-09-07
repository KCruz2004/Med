filas=3
columnas=3


#Inicializar la matriz
matriz=[]
print("\n Por favor ingrese los valores de la matriz")

suma=0
#LLenar la matriz con los valores ingresados por el usuario
for i in range(filas):
    fila=[]
    for j in range(columnas):
        valor=float(input(f"Elemento[{i+1}][{j+1}]: "))
        
        fila.append(valor)
        suma+=valor

    matriz.append(fila)
  

#Mostrar la matriz resultante
print(f"\n La matriz ingresada es: ")
for fila in matriz:
    print(fila)
print(f"\n La suma de la matriz es igual:  {suma}")