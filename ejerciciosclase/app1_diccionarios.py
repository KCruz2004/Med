Datos_Basicos={"Nombre": "Kevin Alexander",
               "Apellido":"Cruz",
               "DUI":"066690203-2",
               "Fecha_Nacimiento":"20/04/2004",
               "Lugar_Nacimiento": "Sivar Land",
               "Nacionalidad":"Salvadoreño",
               "Estado_Civil":"Negativo"}
print("\n Detalles del Diccionario")
print("---------------------------")

print("\n Claves del diccionario", Datos_Basicos.keys())
print("\n Valores del diccionario", Datos_Basicos.values())
print("\n Elementos del diccionario", Datos_Basicos.items())

#Ejemplo practico de los diccionarios
print("\nInscripcion del curso")
print("---------------------------")

print("\n Datos del participante")
print("---------------------------")

print("DUI", Datos_Basicos["DUI"])
print("\n Nombre completo: ",Datos_Basicos["Nombre"]+" "+Datos_Basicos["Apellido"])
