import ui

def menu():
    opciones = {
        '1': ui.ejecutar_agregar,
        '2': ui.ejecutar_actualizar,
        '3': ui.ejecutar_buscar,
        '4': ui.ejecutar_filtrar_continente,
        '5': ui.ejecutar_filtrar_poblacion,
        '6': ui.ejecutar_filtrar_superficie,
        '7': ui.ejecutar_ordenar,
        '8': ui.ejecutar_estadisticas
    }
    while True:
        print("\n--- GESTIÓN DE PAÍSES ---")
        print("1. Agregar País")
        print("2. Actualizar País")
        print("3. Buscar País por nombre")
        print("4. Filtrar por Continente")
        print("5. Filtrar por rango de Población")
        print("6. Filtrar por rango de Superficie")
        print("7. Ordenar países")
        print("8. Mostrar Estadísticas")
        print("9. Salir")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '9':
            print("Saliendo del programa...")
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
