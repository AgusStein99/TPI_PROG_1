import manager

def mostrar_paises(paises):
    if not paises:
        print("No se encontraron países con esos criterios.")
        return
    for p in paises:
        print(f"- {p['nombre']}: Población {p['poblacion']}, Superficie {p['superficie']} km2, {p['continente']}")

def ejecutar_agregar():
    nombre = input("Ingrese el nombre del país: ").strip()
    if not nombre: return print("El nombre no puede estar vacío.")
    try:
        pob = int(input("Ingrese la población: "))
        sup = int(input("Ingrese la superficie en km2: "))
    except ValueError: return print("Error: Deben ser números enteros.")
    cont = input("Ingrese el continente: ").strip()
    if not cont: return print("El continente no puede estar vacío.")
    
    manager.insertar_pais(nombre, pob, sup, cont)
    print("País agregado exitosamente.")

def ejecutar_actualizar():
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()
    try:
        nueva_pob = int(input("Nueva población: "))
        nueva_sup = int(input("Nueva superficie: "))
    except ValueError: return print("Error: Valores numéricos inválidos.")
    
    if manager.modificar_pais(nombre, nueva_pob, nueva_sup):
        print("Datos actualizados correctamente.")
    else:
        print("País no encontrado.")

def ejecutar_buscar():
    termino = input("Ingrese el nombre del país a buscar: ").strip()
    resultados = manager.filtrar_paises(termino)
    mostrar_paises(resultados)

def ejecutar_filtrar_continente():
    continente = input("Ingrese el continente a filtrar: ").strip()
    if not continente: return print("El continente no puede estar vacío.")
    resultados = manager.filtrar_por_continente(continente)
    mostrar_paises(resultados)

def ejecutar_filtrar_poblacion():
    try:
        minimo = int(input("Población mínima: "))
        maximo = int(input("Población máxima: "))
    except ValueError: return print("Error: Deben ser números enteros.")
    if minimo > maximo: return print("Error: el mínimo no puede ser mayor que el máximo.")
    resultados = manager.filtrar_por_rango_poblacion(minimo, maximo)
    mostrar_paises(resultados)

def ejecutar_filtrar_superficie():
    try:
        minimo = int(input("Superficie mínima (km2): "))
        maximo = int(input("Superficie máxima (km2): "))
    except ValueError: return print("Error: Deben ser números enteros.")
    if minimo > maximo: return print("Error: el mínimo no puede ser mayor que el máximo.")
    resultados = manager.filtrar_por_rango_superficie(minimo, maximo)
    mostrar_paises(resultados)

def ejecutar_ordenar():
    print("Ordenar por: 1. Nombre  2. Población  3. Superficie")
    campo_opcion = input("Seleccione una opción: ").strip()
    campos = {'1': 'nombre', '2': 'poblacion', '3': 'superficie'}
    campo = campos.get(campo_opcion)
    if not campo: return print("Opción inválida.")

    orden = input("¿Ascendente o descendente? (A/D): ").strip().lower()
    if orden not in ('a', 'd'): return print("Opción inválida.")
    descendente = orden == 'd'

    resultados = manager.ordenar_paises(campo, descendente)
    mostrar_paises(resultados)

def ejecutar_estadisticas():
    est = manager.calcular_estadisticas()
    if not est: return print("No hay datos para calcular estadísticas.")
    print("\n--- Estadísticas ---")
    print(f"Mayor población: {est['mayor_pob']['nombre']} ({est['mayor_pob']['poblacion']})")
    print(f"Menor población: {est['menor_pob']['nombre']} ({est['menor_pob']['poblacion']})")
    print(f"Promedio de población: {est['prom_pob']:.2f}")
    print(f"Promedio de superficie: {est['prom_sup']:.2f} km2")
    print("Cantidad por continente:")
    for cont, cant in est['continentes'].items():
        print(f"  - {cont}: {cant}")
