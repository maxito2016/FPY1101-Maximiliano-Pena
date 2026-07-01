def registarar_usuario():
    nombre = input("Ingrese su nombre el estudiante: ")
    carrera = input("Ingrese su carrera: ")
    return nombre, carrera

def registrar_libro():
    libro = input("Ingrese el nombre del libro: ")

    while True:
        try:
            dias = int(input("Ingrese el número de días que desea el prestamo del libro: "))
            if dias < 0:
                return libro, dias

            else:
                print("Los días deben ser mayores que cero.")
        except:
            print("Por favor, ingrese un número válido para los días.")

def generar_resumen(nombre, carrera, libro, dias):
    print("------Resumen del préstamo-------")
    print(f"Nombre del estudiante: {nombre}")
    print(f"Carrera: {carrera}")
    print(f"Libro prestado: {libro}")
    print(f"Días de préstamo: {dias}")

    if dias > 14:
        print("El préstamo excede el tiempo permitido de 14 días.")

    else:
        print("El préstamo está dentro del tiempo permitido de 14 días.")

print("------Sistema de reservas-------")
nombre, carrera = registarar_usuario()
libro, dias = registrar_libro()

generar_resumen(nombre, carrera, libro, dias)


print("----COMPROBACIÓN DE VENCIMIENTO----")
if dias <= 14: 
    dias_restantes = 14 - dias
    print(f"-> Registro exitoso. Al alumno le quedan {dias_restantes} días de margen antes del límite.")
else:
    print("-> Alerta: El sistema bloqueará al usuario hasta que regularice los días.")