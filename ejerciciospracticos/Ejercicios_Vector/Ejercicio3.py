numeros_ingresados=[]

for i in range(7):
    numero= int(input("Ingrese 7 numeros "))
    numeros_ingresados.append(numero)


#Tambien lo podemos hacer utilizando la funcion max  
numero_max= max(numeros_ingresados)
print(f"Numero mayor utilizando max {numero_max}")

numero_mayor= numeros_ingresados[0]
for numero in numeros_ingresados:
    if numero>numero_mayor:
        numero_mayor=numero


print(f"El numero mayor de la lista es {numero_mayor}")
