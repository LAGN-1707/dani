# 8   #validar cantidad de caracteres
tamanio = (input("Ingrese dato: "))
print("El tamanio de la variante es: ", len(tamanio))

if (len(tamanio) > 11):
    print("Ingreso correcto")
else:
    print("Ingreso debe ser al menos de 12 caracteres")


#validar que un numero sea positivo

numero = int(input("Ingrese un numero: "))

while(numero <= 0):
    print("¡dato de investifacion invalido! ingrese un entero positivo")
    numero = int(input("ingrese un numero:\n"))

#como controlo que las opciones sean solamente numeros

opcion = 0
while(opcion == 0):
    try:
        opcion = int(input("Ingrese una opcion: "))
    except:
        print("ha ocurrido un error")
        opcion = 0


#eliminar espacios

palabra = " hola mundo "

print(palabra.strip())