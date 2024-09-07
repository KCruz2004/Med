vector=[]

for i in range(5):
    numero=int(input(f"Ingrese el numero {i+1}: "))
    vector.append(numero)
    suma=sum(vector)

print(f"\n Vector ingresado {vector}")
print(f"\n Sumatoria de los elementos del vector {suma}")