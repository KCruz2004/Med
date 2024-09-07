numeros_enteros=[]
numeros_positivos=[]
for i in range(8):
    numeros=int(input("Ingrese un numero, ya sea positivo o negativo "))
    numeros_enteros.append(numeros)
    if numeros>0:
        numeros_positivos.append(numeros)
    
print(f"\n Numeros ingresados: {numeros_enteros}")
print(f"\n Numeros positivos ingresados: {numeros_positivos} \n Se han ingresado {len(numeros_positivos)} numeros positivos")