def validar_nota():
    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante: "))
            if nota >= 1.0 and nota <= 7.0:
                return nota
            else:
                print("Error: La nota debe estar entre 1.0 y 7.0.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

def determinar_estado(promedio):
    if promedio >= 4.0:
        return "Aprobado"
    else:
        return "Reprobado"

nombre = ""
nota1 = 0
nota2 = 0
nota3 = 0

while True:
    print("------Sistema de calificaciones-------")
    print("1. Registrar alumno")
    print("2. Registrar notas")
    print("3. Mostrar estado académico")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")

    elif opcion == "2":
        if nombre == "":
            print("Debe registrar un alumno primero.")
        else:
            print(f"Registrando las tres notas para {nombre}:")
            nota1 = validar_nota()
            nota2 = validar_nota()
            nota3 = validar_nota()

    elif opcion == "3":
        if nombre == "":
            print("No hay ningún alumno registrado.")
        else:
            promedio = calcular_promedio(nota1, nota2, nota3)
            estado = determinar_estado(promedio)
            print(f"Nombre del estudiante: {nombre}")
            print(f"Nota 1: {nota1}")
            print(f"Nota 2: {nota2}")
            print(f"Nota 3: {nota3}")
            print(f"Promedio: {promedio:.2f}")
            print(f"Estado académico: {estado}")

    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida.")
        
        if promedio >= 6.0: 
            print("¡Felicitaciones extraordinarias! Alumno destacado en el cuadro de honor.")
        elif promedio < 4.0:
            print("Atención: Se sugiere inscribir al alumno en los talleres de reforzamiento académico.")