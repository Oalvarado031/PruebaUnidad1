#Hecho Oscar Alvarado y Oscar Arnuero

class Estudiante:
    def __init__(self, nombre: str, edad: int, carrera: str):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []

    def agregar_calificacion(self, nota: float):
        """Agrega una calificación al estudiante si está entre 0 y 100."""
        if 0 <= nota <= 100:
            self.calificaciones.append(nota)
            print(f"Calificación {nota} agregada correctamente.")
        else:
            print("Error: La nota debe estar entre 0 y 100.")

    def promedio(self) -> float:
        """Calcula y devuelve el promedio de las calificaciones del estudiante."""
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        return 0.0

    def mostrar_info(self):
        """Muestra la información completa del estudiante, incluyendo el promedio."""
        prom = self.promedio()
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {prom:.2f}")


def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\nMenú de opciones:")
    print("1. Registrar nuevo estudiante")
    print("2. Agregar calificación a un estudiante")
    print("3. Mostrar información de un estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir del programa")
    opcion = input("Seleccione una opción (1-5): ")
    return opcion


def validar_entero_positivo(valor: str) -> int:
    try:   #Valida que el valor ingresado sea un entero positivo. Retorna el entero si es válido, o None si no lo es.
        numero = int(valor)
        if numero > 0:
            return numero
        else:
            return None
    except ValueError:
        return None


def buscar_estudiante(estudiantes: list, nombre: str) -> Estudiante:
    """
    Busca un estudiante por nombre en la lista de estudiantes.
    Retorna el objeto Estudiante si lo encuentra o None si no existe.
    """
    for estudiante in estudiantes:
        if estudiante.nombre.lower() == nombre.lower():
            return estudiante
    return None


def main():
    estudiantes = []  # Lista para almacenar los objetos Estudiante

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            # Registrar nuevo estudiante

            while True:    
                nombre = input("Ingrese el nombre del estudiante: ")

                if nombre.replace(" ", "").isalpha():  #Replace reemplza los espacios para juntar las cadenas y la validación sirva
                    break
                else:
                    print("El nombre solo debe contener letras.")
                            
            edad_input = input("Ingrese la edad del estudiante: ")

            edad = validar_entero_positivo(edad_input)
            if edad is None:
                print("Edad inválida. Debe ser un número entero positivo.")
                continue
            carrera = input("Ingrese la carrera del estudiante: ")
            
            nuevo_estudiante = Estudiante(nombre, edad, carrera)
            estudiantes.append(nuevo_estudiante)
            print("Estudiante registrado exitosamente.")

        elif opcion == "2":
            # Agregar calificación a un estudiante
            nombre = input("Ingrese el nombre del estudiante al que desea agregar una calificación: ")
            estudiante = buscar_estudiante(estudiantes, nombre)
            if estudiante:
                try:
                    nota = float(input("Ingrese la calificación (0-100): "))
                    estudiante.agregar_calificacion(nota)
                except ValueError:
                    print("La calificación debe ser un número.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "3":
            # Mostrar información de un estudiante
            nombre = input("Ingrese el nombre del estudiante: ")
            estudiante = buscar_estudiante(estudiantes, nombre)
            if estudiante:
                estudiante.mostrar_info()
            else:
                print("Estudiante no encontrado.")

        elif opcion == "4":
            # Mostrar todos los estudiantes registrados
            if estudiantes:
                print("\nListado de Estudiantes:")
                for idx, estudiante in enumerate(estudiantes, start=1):
                    print(f"\nEstudiante {idx}:")
                    estudiante.mostrar_info()
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")


if __name__ == "__main__":
    main()
