# Gestión de Datos de Países en Python

Trabajo Práctico Integrador (TPI) — Tecnicatura Universitaria en Programación a Distancia.

## Descripción

Aplicación de consola desarrollada en Python 3 que permite gestionar información de países (nombre, población, superficie y continente) almacenada en un archivo CSV. El sistema permite agregar, actualizar, buscar, filtrar y ordenar países, además de calcular estadísticas básicas sobre el conjunto de datos.

El proyecto está organizado en cuatro módulos, cada uno con una responsabilidad específica:

| Archivo       | Responsabilidad |
| --------------|-----------------|
| `main.py`     | Punto de entrada del programa y menú principal. |
| `ui.py`       | Interacción con el usuario (lectura de datos por consola, validaciones de entrada y presentación de resultados). |
| `manager.py`  | Lógica de negocio: filtrado, ordenamiento, actualización y cálculo de estadísticas. |
| `database.py` | Persistencia de datos: lectura y escritura del archivo `paises.csv`. |

## Requisitos

- Python 3.10 o superior (no requiere librerías externas).

## Instalación y ejecución

```bash
git clone <https://github.com/AgusStein99/TPI_PROG_1>
cd <TPI_PROG_1>
python3 main.py
```

Al iniciar, el programa busca el archivo `data/paises.csv`. Si no existe, se crea automáticamente al agregar el primer país.

## Uso

Al ejecutar `main.py` se muestra el siguiente menú:

```
--- GESTIÓN DE PAÍSES ---
1. Agregar País
2. Actualizar País
3. Buscar País por nombre
4. Filtrar por Continente
5. Filtrar por rango de Población
6. Filtrar por rango de Superficie
7. Ordenar países
8. Mostrar Estadísticas
9. Salir
Seleccione una opción:
```

### Ejemplos de entrada y salida

**Agregar un país**
```
Seleccione una opción: 1
Ingrese el nombre del país: Chile
Ingrese la población: 19458310
Ingrese la superficie en km2: 756102
Ingrese el continente: America
País agregado exitosamente.
```

**Filtrar por continente**
```
Seleccione una opción: 4
Ingrese el continente a filtrar: America
- Argentina: Población 45376763, Superficie 2780400 km2, America
- Brasil: Población 213993437, Superficie 8515767 km2, America
```

**Ordenar por población (descendente)**
```
Seleccione una opción: 7
Ordenar por: 1. Nombre  2. Población  3. Superficie
Seleccione una opción: 2
¿Ascendente o descendente? (A/D): D
- Brasil: Población 213993437, Superficie 8515767 km2, America
- Japón: Población 125800000, Superficie 377975 km2, Asia
- Alemania: Población 83149300, Superficie 357022 km2, Europa
- Argentina: Población 45376763, Superficie 2780400 km2, America
```

**Estadísticas**
```
Seleccione una opción: 8

--- Estadísticas ---
Mayor población: Brasil (213993437)
Menor población: Argentina (45376763)
Promedio de población: 117079875.00
Promedio de superficie: 3007791.00 km2
Cantidad por continente:
  - America: 2
  - Asia: 1
  - Europa: 1
```

## Estructura del proyecto

```
├── data/
│   └── paises.csv
├── database.py
├── manager.py
├── ui.py
├── main.py
└── README.md
```

