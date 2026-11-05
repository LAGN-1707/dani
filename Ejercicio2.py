
CAPACIDAD_MAXIMA = 20   
disponibles = 25        
historial = 0           

print("¡Bienvenido al sistema de gestión de equipos del Laboratorio Central de Investigación!")

opcion = 0
while opcion != 5:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1.- Equipos disponibles.")
    print("2.- Asignar equipo.")
    print("3.- Liberar equipo.")
    print("4.- Historial de usos.")
    print("5.- Salir.")

    try:
        opcion = int(input("Elige una opción: "))
    except:
        opcion = 0
        print("Opción inválida. Ingresa un número del 1 al 5.")
        continue

    if opcion == 1:
        print("Equipos disponibles:", disponibles)

    elif opcion == 2:
        try:
            cantidad = int(input("¿Cuántos equipos desea asignar? "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.")
            elif cantidad > disponibles:
                print("No hay suficientes equipos disponibles. Solo quedan", disponibles)
            else:
                disponibles = disponibles - cantidad
                historial = historial + cantidad
                print("Se asignaron", cantidad, "equipos. Quedan", disponibles, "disponibles.")
        except:
            print("Debes ingresar un número entero.")

    elif opcion == 3:
        try:
            cantidad = int(input("¿Cuántos equipos desea liberar? "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0.")
            elif disponibles + cantidad > CAPACIDAD_MAXIMA:
                print("No se puede liberar esa cantidad: se superaría la capacidad máxima de", CAPACIDAD_MAXIMA, "equipos.")
            else:
                disponibles = disponibles + cantidad
                historial = historial - cantidad
                print("Se liberaron", cantidad, "equipos. Ahora hay", disponibles, "disponibles.")
        except:
            print("Debes ingresar un número entero.")

    elif opcion == 4:
        print("Total de equipos asignados durante la sesión:", historial)

    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")

    else:
        print("Opción inválida. Ingresa un número del 1 al 5.")
