import csv
import os

# Buscamos la ruta relativa a la carpeta 'data' fuera de 'src'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVO_CSV = os.path.join(BASE_DIR, 'data', 'paises.csv')

def cargar_datos():
    paises = []
    if not os.path.exists(ARCHIVO_CSV):
        return paises
    try:
        with open(ARCHIVO_CSV, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    paises.append({
                        'nombre': row['nombre'],
                        'poblacion': int(row['poblacion']),
                        'superficie': int(row['superficie']),
                        'continente': row['continente']
                    })
                except ValueError:
                    continue  # Ignora filas corruptas
    except Exception as e:
        print(f"Error crítico al leer la base de datos: {e}")
    return paises

def guardar_datos(paises):
    os.makedirs(os.path.dirname(ARCHIVO_CSV), exist_ok=True)
    with open(ARCHIVO_CSV, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['nombre', 'poblacion', 'superficie', 'continente'])
        writer.writeheader()
        writer.writerows(paises)
