# Creamos un diccionario para poder acceder a los estudiantes desde su matricula 
estudiantes = {}

# Creamos la lista de los estudiantes 
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

# Ahora creamos un bucle for que nos ayude a guardar cada dato de la lista en el diccionario de estudiantes con su valor correspondiente

for matricula, nombre, apellido, edad, carrera, nota in datos_iniciales:
    estudiantes[matricula] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "carrera": carrera,
        "nota": {"Promedio": nota},
        "asistencia": 0
}
        
# Le pedimos al usuario que elija una opcion 
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

    opcion = int(input("Seleccione una opción: "))
    
    # Creamos la condicional para agragar a un estudiante
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
            print("No se encontró ningún estudiante con esa matrícula.")


