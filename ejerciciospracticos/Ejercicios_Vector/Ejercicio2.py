numeros_promedio=[]

for i in range(10):
    numero=int(input("Ingrese 10 numeros: "))
    numeros_promedio.append(numero)
    promedio=sum(numeros_promedio)/len(numeros_promedio)
print(f"\n Numeros ingresados: {numeros_promedio}")
print(f"\n Promedio de los numeros ingresados: {promedio}")
