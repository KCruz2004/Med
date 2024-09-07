print("\n Información Sobre la Universidad")
print("\n 1- Inicio de ciclo 01-2025")
print("\n 2- Fecha de inscripción 01-2025")
print("\n3-Finalización de ciclo 01-2025")
print("\n Salir del programa")
print("\n Seleccione una de las opciones del 1 al 3")

while True:
    opcion=int(input("Ingresar opcion: "))

    if opcion==1:
        print("\nLa fecha de inicio del ciclo 01-2025 es el 20 de Enero del 2025")
    elif opcion==2:
        print("\nFecha de inscripción es del 2 al 15 de enero del 2025")
    elif opcion==3:
        print("\n El ciclo 01-2025 finalizara el 20 de Junio de 2025")
    elif opcion==4:
        print("Cierre del programa")
        break
    else:
        print("Ingrese una opcion valida entre el 1 y 3")
