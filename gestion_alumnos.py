import json  # Importa el módulo json

# Función para carga los datos de los alumnos desde un archivo JSON.
def cargar_alumnos(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)  # Devuelve el contenido del archivo convertido en un objeto de Python

# Función que busca un alumno por su nombre
def buscar_alumno(alumnos, nombre):
    for alumno in alumnos:
        if alumno['nombre'].lower() == nombre.lower():
            return alumno  # Si encuentra el alumno, retorna al alumno.
    return None  # Si no encuentra al alumno, retorna None.

if __name__ == "__main__":
    # Define la ruta del archivo JSON que contiene la lista de alumnos.
    ruta = "laboratorio5/alumnos.json"
    alumnos = cargar_alumnos(ruta)
    # Solicita al usuario que ingrese el nombre del alumno que desea buscar.
    nombre_buscar = input("Ingrese el nombre del alumno a buscar: ")
    resultado = buscar_alumno(alumnos, nombre_buscar)
    # Verifica si el alumno fue encontrado.
    if resultado:
        print(f"Alumno encontrado: {resultado}")
    else:
        print("Alumno no encontrado.")


