# Sistema de gestión de estudiantes
estudiantes = {}

def inicializar_estudiantes():
    # Datos iniciales de estudiantes
    datos_iniciales = [
        ("221461768", "Samanta Julieth", "Torres Rodríguez", 18, "Tecnologías Biomédicas", 97.13),
        ("083208848", "Martha Alicia", "Rivera Santos", 56, "Tecnologías Biomédicas", 98.5),
        ("209550194", "Erika Janeth", "Correa Rodríguez", 30, "Tecnologías Biomédicas", 94),
        ("221463876", "Valeria Carolina", "Luna Silva", 18, "Tecnologías Biomédicas", 97.33),
        ("221226637", "Carlos Alberto", "Gil Martínez", 19, "Tecnologías Biomédicas", 86),
        ("221930172", "Reyna Esmeralda", "Aguilera Galán", 20, "Tecnologías Biomédicas", 93),
        ("221461407", "Edna Naomi", "Martín Gallardo", 18, "Tecnologías Biomédicas", 95.5),
        ("221049972", "Yahir", "Mejía Vázquez", 18, "Tecnologías Biomédicas", 98),
        ("221773743", "Jacob", "Ávila Núñez", 19, "Tecnologías Biomédicas", 92.33),
        ("221579726", "Quehat Merari Uziel", "Martínez Castro", 18, "Tecnologías Biomédicas", 90),
        ("224164501", "Yael", "Gómez Gómez", 19, "Tecnologías Biomédicas", 95.5),
        ("207593732", "Eddy Armando", "De la Cruz Huezo", 32, "Tecnologías Biomédicas", 90.6),
        ("221594946", "Angel Antonio", "Torres Bermúdez", 18, "Tecnologías Biomédicas", 93)
    ]
    
    for matricula, nombre, apellido, edad, carrera, nota in datos_iniciales:
        estudiantes[matricula] = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "carrera": carrera,
            "notas": {"Promedio General": nota},
            "asistencia": 0
        }
    print("Sistema inicializado con datos de estudiantes exitosamente.")

def agregar_estudiante():
    matricula = input("Ingrese el número de matrícula: ")
    if matricula in estudiantes:
        print("Este estudiante ya está registrado.")
    else:
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = int(input("Ingrese la edad: "))
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
    criterio = input("Buscar por (1-Matrícula, 2-Nombre, 3-Apellido): ")
    busqueda = input("Ingrese el término de búsqueda: ").lower()
    encontrados = []
    
    for matricula, datos in estudiantes.items():
        if (criterio == "1" and busqueda in matricula.lower()) or \
           (criterio == "2" and busqueda in datos['nombre'].lower()) or \
           (criterio == "3" and busqueda in datos['apellido'].lower()):
            encontrados.append((matricula, datos))
    
    if encontrados:
        print("\nEstudiantes encontrados:")
        for matricula, datos in encontrados:
            print(f"Matrícula: {matricula}")
            print(f"Nombre: {datos['nombre']} {datos['apellido']}")
            print(f"Edad: {datos['edad']}")
            print(f"Carrera: {datos['carrera']}")
            print("------------------------")
    else:
        print("No se encontraron estudiantes con ese criterio.")

def eliminar_estudiante():
    matricula = input("Ingrese la matrícula del estudiante a eliminar: ")
    if matricula in estudiantes:
        confirmacion = input(f"¿Está seguro de eliminar a {estudiantes[matricula]['nombre']} {estudiantes[matricula]['apellido']}? (s/n): ")
        if confirmacion.lower() == 's':
            del estudiantes[matricula]
            print("Estudiante eliminado.")
        else:
            print("Operación cancelada.")
    else:
        print("No se encontró el estudiante.")

def modificar_estudiante():
    matricula = input("Ingrese la matrícula del estudiante a modificar: ")
    if matricula in estudiantes:
        print("Datos actuales:", estudiantes[matricula])
        print("\nDeje en blanco si no desea modificar el campo")
        
        nombre = input("Nuevo nombre: ")
        apellido = input("Nuevo apellido: ")
        edad = input("Nueva edad: ")
        carrera = input("Nueva carrera: ")
        
        if nombre: estudiantes[matricula]["nombre"] = nombre
        if apellido: estudiantes[matricula]["apellido"] = apellido
        if edad: estudiantes[matricula]["edad"] = int(edad)
        if carrera: estudiantes[matricula]["carrera"] = carrera
        
        print("Datos actualizados correctamente.")
    else:
        print("Estudiante no encontrado.")

def listar_estudiantes():
    if estudiantes:
        print("\nLista de estudiantes registrados:")
        print("--------------------------------")
        for matricula, datos in estudiantes.items():
            print(f"Matrícula: {matricula}")
            print(f"Nombre: {datos['nombre']} {datos['apellido']}")
            print(f"Edad: {datos['edad']}")
            print(f"Carrera: {datos['carrera']}")
            print("--------------------------------")
    else:
        print("No hay estudiantes registrados.")

def agregar_notas():
    matricula = input("Ingrese la matrícula del estudiante: ")
    if matricula in estudiantes:
        asignatura = input("Ingrese el nombre de la asignatura: ")
        try:
            nota = float(input("Ingrese la nota obtenida: "))
            if 0 <= nota <= 100:
                estudiantes[matricula]["notas"][asignatura] = nota
                print("Nota registrada.")
            else:
                print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    else:
        print("Estudiante no encontrado.")

def calcular_promedio():
    matricula = input("Ingrese la matrícula del estudiante: ")
    if matricula in estudiantes and estudiantes[matricula]["notas"]:
        notas = list(estudiantes[matricula]["notas"].values())
        promedio = sum(notas) / len(notas)
        print(f"El promedio de {estudiantes[matricula]['nombre']} {estudiantes[matricula]['apellido']} es: {promedio:.2f}")
    else:
        print("No hay notas registradas para este estudiante.")

def registrar_asistencia():
    matricula = input("Ingrese la matrícula del estudiante: ")
    if matricula in estudiantes:
        estudiantes[matricula]["asistencia"] += 1
        print(f"Asistencia registrada para {estudiantes[matricula]['nombre']} {estudiantes[matricula]['apellido']}")
        print(f"Total de asistencias: {estudiantes[matricula]['asistencia']}")
    else:
        print("Estudiante no encontrado.")

def mostrar_reporte():
    matricula = input("Ingrese la matrícula del estudiante: ")
    if matricula in estudiantes:
        datos = estudiantes[matricula]
        print("\n=== REPORTE DE ESTUDIANTE ===")
        print(f"Matrícula: {matricula}")
        print(f"Nombre completo: {datos['nombre']} {datos['apellido']}")
        print(f"Edad: {datos['edad']}")
        print(f"Carrera: {datos['carrera']}")
        print("\nNotas:")
        if datos["notas"]:
            for asignatura, nota in datos["notas"].items():
                print(f"- {asignatura}: {nota}")
        else:
            print("No hay notas registradas")
        print(f"\nTotal de asistencias: {datos['asistencia']}")
        print("============================")
    else:
        print("Estudiante no encontrado.")

# Inicializar el sistema con los estudiantes
inicializar_estudiantes()

# Bucle principal del menú
while True:
    print("\n=== Sistema de Gestión de Estudiantes ===")
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
    print("=====================================")

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
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida, intente de nuevo.")
