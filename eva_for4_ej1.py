def validar_temperatura(valor_temperatura):
    try:
        temperatura = float(valor_temperatura)
        return temperatura
    except ValueError:
        print("Error: La temperatura debe ser un número.")
        return None

def calcular_promedio(lista_temperaturas):
    if not lista_temperaturas:
        return 0
    return sum(lista_temperaturas) / len(lista_temperaturas)
    
def obtener_alerta(promedio_temperaturas):
    if promedio_temperaturas > 30:
        return "Alerta: Temperatura alta"
    elif promedio_temperaturas < 10:
        return "Alerta: Temperatura baja"
    else:
        return "Temperatura dentro del rango normal"
    
def main():
    temperaturas = []
    while len(temperaturas) < 5:
        entrada = input("Ingrese la temperatura (o 'salir' para terminar): ")
        temperatura = validar_temperatura(entrada)
        
        if entrada.lower() == 'salir':
            break
        temperatura = validar_temperatura(entrada)
        if temperatura is not None:
            temperaturas.append(temperatura)
    
    promedio = calcular_promedio(temperaturas)
    alerta = obtener_alerta(promedio)
    
    print(f"Promedio de temperaturas: {promedio:.2f}")
    print(alerta)

if __name__ == "__main__":
    main()

    if 'lista_temperaturas' in locals() and len(lista_temperaturas) > 0:
        print("----REPORTE ESTADÍSTICO DE TEMPERATURAS----")
        print(f"Temperatura promedio: {sum(lista_temperaturas) / len(lista_temperaturas):.1f}°C")
        print(f"Temperatura máxima registrada: {max(lista_temperaturas)}°C")
        print(f"Temperatura mínima registrada: {min(lista_temperaturas)}°C")
        
    else:
        print("No se registraron temperaturas para generar las estadísticas.")