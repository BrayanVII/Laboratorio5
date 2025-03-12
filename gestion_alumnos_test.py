import unittest  # Importa el módulo unittest

# Función que busca un alumno por su nombre en una lista de alumnos.
def buscar_alumno(alumnos, nombre):
    for alumno in alumnos:
        if alumno["nombre"] == nombre:  
            return alumno  
    return None 

# Clase que hereda de unittest.TestCase
class TestGestionAlumnos(unittest.TestCase):

    def setUp(self):
        # Define una lista de alumnos con información de nombre, edad y carrera.
        self.alumnos = [
            {"nombre": "Ana", "edad": 20, "carrera": "Ingeniería"},
            {"nombre": "Luis", "edad": 22, "carrera": "Matemáticas"},
            {"nombre": "María", "edad": 21, "carrera": "Física"}
        ]

    # Prueba para verificar que la función buscar_alumno devuelve el alumno correcto cuando existe.
    def test_buscar_alumno_existente(self):
        resultado = buscar_alumno(self.alumnos, "Ana")  
        self.assertIsNotNone(resultado) 
        self.assertEqual(resultado["nombre"], "Ana")  

    # Prueba para verificar que la función buscar_alumno devuelve None cuando el alumno no existe.
    def test_buscar_alumno_inexistente(self):
        resultado = buscar_alumno(self.alumnos, "Carlos") 
        self.assertIsNone(resultado) 

# Código que ejecuta las pruebas
if __name__ == "__main__":
    unittest.main()  # Ejecuta todas las pruebas definidas en la clase TestGestionAlumnos.
