# Creamos un diccionario para poder acceder a los estudiantes desde su matricula 
estudiantes = {}

# Lista de materias que todos los estudiantes deben tener
materias = [
    "Fisica Biomedica I",
    "Quimica General y Organica",
    "Programacion I",
    "Ciencias Biologicas I"
]

# Creamos la lista de los estudiantes con sus calificaciones
datos_iniciales = [ 
        ("221461768", "Samanta Julieth", "Torres Rodríguez", 18, "Tecnologías Biomédicas", 
         {"Fisica Biomedica I": 95.5, "Quimica General y Organica": 97.2, "Programacion I": 98.0, "Ciencias Biologicas I": 97.8}),
        ("083208848", "Martha Alicia", "Rivera Santos", 56, "Tecnologías Biomédicas",
         {"Fisica Biomedica I": 98.0, "Quimica General y Organica": 99.0, "Programacion I": 97.5, "Ciencias Biologicas I": 99.5}),
        ("209550194", "Erika Janeth", "Correa Rodríguez", 30, "Tecnologías Biomédicas",
         {"Fisica Biomedica I": 94.0, "Quimica General y Organica": 93.5, "Programacion I": 95.0, "Ciencias Biologicas I": 93.5}),
        ("221463876", "Valeria Carolina", "Luna Silva", 18, "Tecnologías Biomédicas",
         {"Fisica Biomedica I": 97.0, "Quimica General y Organica": 98.0, "Programacion I": 96.8, "Ciencias Biologicas I": 97.5}),
        ("221226637", "Carlos Alberto", "Gil Martínez", 19, "Tecnologías Biomédicas",
         {"Fisica Biomedica I": 85.5, "Quimica General y Organica": 86.0, "Programacion I": 87.0, "Ciencias Biologicas I": 85.5}),
        ("221930172", "Reyna Esmeralda", "Aguilera Galán", 20, "Tecnologías Biomédicas",
         {"Fisica Biomedica I": 92.5, "Quimica General y Organica": 93.0, "Programacion I": 94.0, "Ciencias Biologicas I": 92.5}),
        ("221461407", "Edna Naomi", "Martín Gallardo", 18, "Tecnologías Biomédicas",
         {"Fisica Biomedica I": 95.0, "Quimica General y Organica": 96.0, "Programacion I": 95.5, "Ciencias Biologicas I": 95.5}),
        ("221049972", "Yahir", "Mejía Vázquez", 18, "Tecnologías Biomédicas",
         {"Fisica Biomedica I": 98.0, "Quimica General y Organica": 97.5, "Programacion I": 98.5, "Ciencias Biologicas I": 98.0}),
        ("221773743", "Jacob", "Ávila Núñez", 19, "Tecnologías Biomédicas",
         {"Fisica Biomedica I": 92.0, "Quimica General y Organica": 93.0, "Programacion I": 91.8, "Ciencias Biologicas I": 92.5}),
        ("221579726", "Quehat Merari Uziel", "Martínez Castro", 18, "Tecnologías Biomédicas",
         {"Fisica Biomedica I": 90.0, "Quimica General y Organica": 89.5, "Programacion I": 90.5, "Ciencias Biologicas I": 90.0}),
        ("224164501", "Yael", "Gómez Gómez", 19, "Tecnologías Biomédicas",
         {"Fisica Biomedica I": 95.0, "Quimica General y Organica": 96.0, "Programacion I": 95.5, "Ciencias Biologicas I": 95.5}),
        ("207593732", "Eddy Armando", "De la Cruz Huezo", 32, "Tecnologías Biomédicas",
         {"Fisica Biomedica I": 90.5, "Quimica General y Organica": 91.0, "Programacion I": 90.0, "Ciencias Biologicas I": 91.0}),
        ("221594946", "Angel Antonio", "Torres Bermúdez", 18, "Tecnologías Biomédicas",
         {"Fisica Biomedica I": 93.0, "Quimica General y Organica": 92.5, "Programacion I": 93.5, "Ciencias Biologicas I": 93.0})
]

# Ahora guardamos los datos en el diccionario de estudiantes
for matricula, nombre, apellido, edad, carrera, notas in datos_iniciales:
    estudiantes[matricula] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "carrera": carrera,
        "notas": notas,
        "asistencia": 0
    }

while True:
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

    opcion = int(input("Seleccione una opción (1-10): "))
    
    # Agregar estudiante
    if opcion == 1:
    

        matricula = input("Ingrese el numero de matricula: ")
        if matricula in estudiantes:
            print("Este estudiante ya esta registrado")
        else:
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            edad = input("Ingrese la edad: ")
            carrera = input("Ingrerse la carrera: ")
            estudiantes[matricula]: {
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "carrera": carrera,
                "nota": {"Promedio": nota},
                "asistencia": 0
           }
            print("El estudiante se agrego correctamente")

    elif opcion == 2:
        matricula = input("Ingrese la matrícula del estudiante: ")
    
        if matricula in estudiantes:
            datos = estudiantes[matricula]
            print("\nEstudiante encontrado:")
            print(f"Matrícula: {matricula}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Apellido: {datos['apellido']}")
            print(f"Edad: {datos['edad']}")
            print(f"Carrera: {datos['carrera']}")
        else:
            print("No se encontro al estudiante")
                
    # Modificar estudiante
    elif opcion == 3:
        matricula = input("Ingrese la matrícula del estudiante a modificar: ")
        if matricula in estudiantes:
            print("Deje en blanco si no quiere modificar el dato")
            nombre = input("Nuevo nombre: ")
            apellido = input("Nuevo apellido: ")
            edad = input("Nueva edad: ")
            carrera = input("Nueva carrera: ")
            
            if nombre:
                estudiantes[matricula]["nombre"] = nombre
            if apellido:
                estudiantes[matricula]["apellido"] = apellido
            if edad:
                estudiantes[matricula]["edad"] = int(edad)
            if carrera:
                estudiantes[matricula]["carrera"] = carrera
            print("Datos modificados correctamente")
        else:
            print("Estudiante no encontrado")

    # Eliminar estudiante
    elif opcion == 4:
        matricula = input("Ingrese la matrícula del estudiante a eliminar: ")
        if matricula in estudiantes:
            del estudiantes[matricula]
            print("Estudiante eliminado correctamente")
        else:
            print("Estudiante no encontrado")

    # Listar estudiantes
    elif opcion == 5:
        print("\nLista de estudiantes:")
        for matricula, e in estudiantes.items():
            print(f"\nMatrícula: {matricula}")
            print(f"Nombre: {e['nombre']} {e['apellido']}")
            print(f"Carrera: {e['carrera']}")

    # Agregar notas
    elif opcion == 6:
        matricula = input("Ingrese la matrícula del estudiante: ")
        if matricula in estudiantes:
            print("\nMaterias disponibles:")
            for i, materia in enumerate(materias, 1):
                print(f"{i}. {materia}")
            
            materia_num = int(input("Seleccione el número de la materia: ")) - 1
            if 0 <= materia_num < len(materias):
                materia = list(materias.keys())[materia_num]
                nota = float(input(f"Ingrese la nota para {materia}: "))
                estudiantes[matricula]["notas"][materia] = nota
                print("Nota agregada correctamente")
            else:
                print("Número de materia inválido")
        else:
            print("Estudiante no encontrado")

    # Calcular promedio
    elif opcion == 7:
        matricula = input("Ingrese la matrícula del estudiante: ")
        if matricula in estudiantes:
            notas = estudiantes[matricula]["notas"].values()
            promedio = sum(notas) / len(notas)
            print(f"El promedio es: {promedio:.2f}")
        else:
            print("Estudiante no encontrado")

    # Registrar asistencia
    elif opcion == 8:
        matricula = input("Ingrese la matrícula del estudiante: ")
        if matricula in estudiantes:
            estudiantes[matricula]["asistencia"] += 1
            print(f"Asistencia registrada. Total: {estudiantes[matricula]['asistencia']}")
        else:
            print("Estudiante no encontrado")

    # Mostrar reporte
    elif opcion == 9:
        matricula = input("Ingrese la matrícula del estudiante: ")
        if matricula in estudiantes:
            e = estudiantes[matricula]
            print("\n--- REPORTE DEL ESTUDIANTE ---")
            print(f"Nombre: {e['nombre']} {e['apellido']}")
            print(f"Matrícula: {matricula}")
            print(f"Edad: {e['edad']}")
            print(f"Carrera: {e['carrera']}")
            print("\nNotas:")
            for materia, nota in e["notas"].items():
                print(f"{materia}: {nota}")
            print(f"\nAsistencias totales: {e['asistencia']}")
        else:
            print("Estudiante no encontrado")

    # Salir
    elif opcion == 10:
        print("¡Gracias por usar el sistema!")
        break

    else:
        print("Opción no válida")
