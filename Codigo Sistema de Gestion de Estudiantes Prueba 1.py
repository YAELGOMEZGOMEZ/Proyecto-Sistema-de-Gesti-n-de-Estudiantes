# Sistema de gestión de estudiantes
estudiantes = {}

def agregar_estudiante():
    matricula = input("Ingrese el número de matrícula: ")
    if matricula in estudiantes:
        print("Este estudiante ya está registrado.")
    else:
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = input("Ingrese la edad: ")
        carrera = input("Ingrese la carrera: ")
        estudiantes[matricula] = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "carrera": carrera,
            "notas": {},
            "asistencia": 0
        }
        print("Estudiante agregado correctamente.")

def buscar_estudiante():
    matricula = input("Ingrese la matrícula del estudiante a buscar: ")
    if matricula in estudiantes:
        print("Información del estudiante:", estudiantes[matricula])
    else:
        print("Estudiante no encontrado.")

def eliminar_estudiante():
    matricula = input("Ingrese la matrícula del estudiante a eliminar: ")
    if matricula in estudiantes:
        del estudiantes[matricula]
        print("Estudiante eliminado.")
    else:
        print("No se encontró el estudiante.")

def modificar_estudiante():
    matricula = input("Ingrese la matrícula del estudiante a modificar: ")
    if matricula in estudiantes:
        print("Datos actuales:", estudiantes[matricula])
        estudiantes[matricula]["nombre"] = input("Nuevo nombre: ")
        estudiantes[matricula]["apellido"] = input("Nuevo apellido: ")
        estudiantes[matricula]["edad"] = input("Nueva edad: ")
        estudiantes[matricula]["carrera"] = input("Nueva carrera: ")
        print("Datos actualizados correctamente.")
    else:
        print("Estudiante no encontrado.")

def listar_estudiantes():
    if estudiantes:
        for matricula, datos in estudiantes.items():
            print(f"Matrícula: {matricula}, Nombre: {datos['nombre']} {datos['apellido']}, Carrera: {datos['carrera']}")
    else:
        print("No hay estudiantes registrados.")

def agregar_notas():
    matricula = input("Ingrese la matrícula del estudiante: ")
    if matricula in estudiantes:
        asignatura = input("Ingrese el nombre de la asignatura: ")
        nota = float(input("Ingrese la nota obtenida: "))
        estudiantes[matricula]["notas"][asignatura] = nota
        print("Nota registrada.")
    else:
        print("Estudiante no encontrado.")

def calcular_promedio():
    matricula = input("Ingrese la matrícula del estudiante: ")
    if matricula in estudiantes and estudiantes[matricula]["notas"]:
        notas = list(estudiantes[matricula]["notas"].values())
        promedio = sum(notas) / len(notas)
        print(f"El promedio de {estudiantes[matricula]['nombre']} es: {promedio:.2f}")
    else:
        print("No hay notas registradas para este estudiante.")

def registrar_asistencia():
    matricula = input("Ingrese la matrícula del estudiante: ")
    if matricula in estudiantes:
        estudiantes[matricula]["asistencia"] += 1
        print(f"Asistencia de {estudiantes[matricula]['nombre']} registrada.")
    else:
        print("Estudiante no encontrado.")

def mostrar_reporte():
    matricula = input("Ingrese la matrícula del estudiante: ")
    if matricula in estudiantes:
        datos = estudiantes[matricula]
        print(f"\nReporte del estudiante {datos['nombre']} {datos['apellido']}:")
        print(f"Edad: {datos['edad']}, Carrera: {datos['carrera']}")
        print("Notas:", datos["notas"])
        print(f"Asistencia: {datos['asistencia']} sesiones")
    else:
        print("Estudiante no encontrado.")

# Bucle principal del menú
while True:
    print("\n--- Sistema de Gestión de Estudiantes ---")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Modificar estudiante")
    print("4. Eliminar estudiante")
    print("5. Listar estudiantes")
    print("6. Agregar notas")
    print("7. Calcular promedio de notas")
    print("8. Registrar asistencia")
    print("9. Mostrar reporte de estudiante")
    print("10. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        buscar_estudiante()
    elif opcion == "3":
        modificar_estudiante()
    elif opcion == "4":
        eliminar_estudiante()
    elif opcion == "5":
        listar_estudiantes()
    elif opcion == "6":
        agregar_notas()
    elif opcion == "7":
        calcular_promedio()
    elif opcion == "8":
        registrar_asistencia()
    elif opcion == "9":
        mostrar_reporte()
    elif opcion == "10":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida, intente de nuevo.")
