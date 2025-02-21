# Creamos un diccionario para poder acceder a los estudiantes desde su matricula
estudiantes = {}

# Lista de materias que todos los estudiantes deben tener
materias = [
    "Fisica Biomedica I",    # Posicion 0
    "Quimica General y Organica",     # Posicion 1
    "Programacion I",     # Posicion 2
    "Ciencias Biologicas I" # Posicion 3
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
# Pedimos al usuario elegir un numero en un Bucle While
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

    opcion = input("Seleccione una opción del 1 al 10: ")

    # Agregar estudiante
    if opcion == "1":
        matricula = input("Ingrese el número de matrícula: ")
        if matricula in estudiantes:
            print("Este estudiante ya está registrado.")
        else:
            nombre = str(input("Ingrese el nombre: "))
            apellido = str(input("Ingrese el apellido: "))
            edad = int(input("Ingrese la edad: "))
            carrera = input("Ingrese la carrera: ")
            notas = {materia: 0.0 for materia in materias}  # Inicializa las notas con 0.0 de calificacion para todas las materias
            estudiantes[matricula] = {
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "carrera": carrera,
                "notas": notas,
                "asistencia": 0
            }
            print("El estudiante se agregó correctamente.")

    # Buscar estudiante
    elif opcion == "2":
        criterio = input("Ingrese el nombre, apellido o matrícula del estudiante: ")
        encontrado = False  # Variable para saber si se encontró al estudiante

    # Recorremos todos los estudiantes
        for matricula, datos in estudiantes.items():
        # Comparamos el criterio con el nombre, apellido o matrícula
            if (criterio.lower() == datos['nombre'].lower() or
                criterio.lower() == datos['apellido'].lower() or
                criterio == matricula):
            
                print("\nEstudiante encontrado:")
                print(f"Matrícula: {matricula}")
                print(f"Nombre: {datos['nombre']} {datos['apellido']}")
                print(f"Edad: {datos['edad']}")
                print(f"Carrera: {datos['carrera']}")
                encontrado = True  # Marcamos que se encontró al estudiante
            

    # Si no se encontró al estudiante, mostramos un mensaje
        if not encontrado:
            print("No se encontró al estudiante con ese nombre, apellido o matrícula.")

        # Modificar estudiante
    elif opcion == "3":
        matricula = input("Ingrese la matrícula del estudiante a modificar: ")
        if matricula in estudiantes:
            print("Deje en blanco si no quiere modificar el dato.")
            try:
                nombre = input("Nuevo nombre: ")
            except:
                print("No puedes escribir numeros, por favor usa solo letras.")
                continue
            try:
                apellido = input("Nuevo apellido: ")
            except:
                print("No puedes escribir numeros, por favor solo usa letras.")
                continue
            try:
                edad = int(input("Nueva edad: "))
            except:
                print("Tienes que poner un numero.")
                continue
            try:
                carrera = input("Nueva carrera: ")
            except:
                print("No puedes escribir numeros, por favor solo usa letras.")
                continue

            if nombre:
                estudiantes[matricula]["nombre"] = nombre
            if apellido:
                estudiantes[matricula]["apellido"] = apellido
            if edad:
                estudiantes[matricula]["edad"] = int(edad)
            if carrera:
                estudiantes[matricula]["carrera"] = carrera
            print("Datos modificados correctamente.")
        else:
            print("Estudiante no encontrado.")

    # Eliminar estudiante
    elif opcion == "4":
        matricula = input("Ingrese la matrícula del estudiante a eliminar: ")
        if matricula in estudiantes:
            del estudiantes[matricula]
            print("Estudiante eliminado correctamente.")
        else:
            print("Estudiante no encontrado.")

    # Listar estudiantes
    elif opcion == "5":
        print("\nLista de estudiantes:")
        for matricula, datos in estudiantes.items():
            print(f"\nMatrícula: {matricula}")
            print(f"Nombre: {datos['nombre']} {datos['apellido']}")
            print(f"Edad: {datos['edad']}")
            print(f"Carrera: {datos['carrera']}")

    # Agregar notas
    elif opcion == "6":
        matricula = input("Ingrese la matrícula del estudiante: ")
        
        # Verificar si el estudiante existe
        if matricula in estudiantes:
            print("\nMaterias disponibles:")
            
            # Mostrar las materias una por una con un número
            contador = 1
            for materia in materias:
                print(f"{contador}. {materia}")
                contador += 1
            
            # Pedir el número de la materia
            try:   
                materia_num = int(input("Seleccione el número de la materia: "))
            except:
                print("Tienes que poner un numero")
                continue
            # Verificar si el número de materia es válido
            if materia_num >= 1 and materia_num <= len(materias):
                # Obtener la materia seleccionada
                    materia_seleccionada = materias[materia_num - 1]
    
                # Pedir la nota
            try:
                nota = float(input(f"Ingrese la nota para {materia_seleccionada}: "))
            except:
                print("Tienes que escribir un numero")
                continue
                # Guardar la nota en el estudiante
                estudiantes[matricula]["notas"][materia_seleccionada] = nota
                print(f"Nota de {materia_seleccionada} agregada correctamente.")
            else:
                print("Número de materia inválido. Intente de nuevo.")
        else:
            print("Estudiante no encontrado. Verifique la matrícula.")

    # Calcular promedio
    elif opcion == "7":
        matricula = input("Ingrese la matrícula del estudiante: ")
        if matricula in estudiantes:
            notas = estudiantes[matricula]["notas"].values()
            promedio = sum(notas) / len(notas)
            print(f"El promedio es: {promedio}")
        else:
            print("Estudiante no encontrado.")

    # Registrar asistencia
    elif opcion == "8":
        matricula = input("Ingrese la matrícula del estudiante: ")
        if matricula in estudiantes:
            estudiantes[matricula]["asistencia"] += 1
            print(f"Asistencia registrada. Total: {estudiantes[matricula]['asistencia']}")
        else:
            print("Estudiante no encontrado.")

    # Mostrar reporte
    elif opcion == "9":
        matricula = input("Ingrese la matrícula del estudiante: ")
        if matricula in estudiantes:
            datos = estudiantes[matricula]
            print("\nReporte del estudiante.")
            print(f"Nombre: {datos['nombre']} {datos['apellido']}")
            print(f"Matrícula: {matricula}")
            print(f"Edad: {datos['edad']}")
            print(f"Carrera: {datos['carrera']}")
            print("\nNotas:")
            for materia, nota in datos["notas"].items():  # .items() entra al contenido de las materias
                print(f"{materia}: {nota}")
            print(f"\nAsistencias totales: {datos['asistencia']}")
        else:
            print("Estudiante no encontrado.")

    # Salir
    elif opcion == "10":
        print("¡Hasta Luego!")
        break

    else:
        print("Opción no válida.")
