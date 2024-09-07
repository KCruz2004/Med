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
  