
principales = 0
asistentes = 0
total = 0

valido = False
while valido == False:
    try:
        cantidad = int(input("¿Cuántos científicos desea registrar? "))
        if cantidad > 0:
            valido = True
        else:
            print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")
    except:
        print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")

for i in range(cantidad):
    print("--- Científico", i + 1, "---")

    id_valido = False
    while id_valido == False:
        id_cientifico = input("Ingresa el ID del científico: ")
        if len(id_cientifico) >= 12 and " " not in id_cientifico:
            id_valido = True
        else:
            print("ID inválido. Debe tener al menos 12 caracteres y no puede tener espacios.")

    pub_valido = False
    while pub_valido == False:
        try:
            publicaciones = int(input("Ingresa el número de publicaciones: "))
            if publicaciones > 0:
                pub_valido = True
            else:
                print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")
        except:
            print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")

    if publicaciones > 12:
        print("El científico", id_cientifico, "es Investigador Principal.")
        principales = principales + 1
    else:
        print("El científico", id_cientifico, "es Investigador Asistente.")
        asistentes = asistentes + 1

    total = total + 1

print("=== RESUMEN DE REGISTRO ===")
print("Total de científicos registrados:", total)
print("Investigadores Principales:", principales)
print("Investigadores Asistentes:", asistentes)
print("¡El instituto cuenta con", principales, "Investigadores Principales y", asistentes, "Investigadores Asistentes! ¡Ciencia en marcha!")