from database import cargar_datos, guardar_datos

def obtener_todos():
    return cargar_datos()

def insertar_pais(nombre, poblacion, superficie, continente):
    paises = cargar_datos()
    paises.append({
        'nombre': nombre, 
        'poblacion': poblacion, 
        'superficie': superficie, 
        'continente': continente
    })
    guardar_datos(paises)

def modificar_pais(nombre_buscar, nueva_pob, nueva_sup):
    paises = cargar_datos()
    for pais in paises:
        if pais['nombre'].lower() == nombre_buscar.lower():
            pais['poblacion'] = nueva_pob
            pais['superficie'] = nueva_sup
            guardar_datos(paises)
            return True
    return False

def filtrar_paises(termino):
    paises = cargar_datos()
    return [p for p in paises if termino.lower() in p['nombre'].lower()]

def filtrar_por_continente(continente):
    paises = cargar_datos()
    return [p for p in paises if p['continente'].lower() == continente.lower()]

def filtrar_por_rango_poblacion(minimo, maximo):
    paises = cargar_datos()
    return [p for p in paises if minimo <= p['poblacion'] <= maximo]

def filtrar_por_rango_superficie(minimo, maximo):
    paises = cargar_datos()
    return [p for p in paises if minimo <= p['superficie'] <= maximo]

def ordenar_paises(campo, descendente=False):
    paises = cargar_datos()
    if campo not in ('nombre', 'poblacion', 'superficie'):
        return []
    if campo == 'nombre':
        clave = lambda p: p['nombre'].lower()
    else:
        clave = lambda p: p[campo]
    return sorted(paises, key=clave, reverse=descendente)

def calcular_estadisticas():
    paises = cargar_datos()
    if not paises:
        return None
        
    conteo_continentes = {}
    for p in paises:
        cont = p['continente']
        conteo_continentes[cont] = conteo_continentes.get(cont, 0) + 1

    return {
        'mayor_pob': max(paises, key=lambda x: x['poblacion']),
        'menor_pob': min(paises, key=lambda x: x['poblacion']),
        'prom_pob': sum(p['poblacion'] for p in paises) / len(paises),
        'prom_sup': sum(p['superficie'] for p in paises) / len(paises),
        'continentes': conteo_continentes
    }
