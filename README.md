# Proyecto-Sistema-de-Gesti-n-de-Estudiantes
# Proyecto de Programación I basado en un sistema de gestión de estudiantes usando los conocimientos adquiridos hasta ahora 

# Definimos variables para almacenar la informacion de los estudiantes
# Datos de los estudiantes
matricula1 = "221461768"
nombre1 = "Samanta Julieth"
apellido1 = "Torres Rodríguez"
notas1 = 97.13
edad1 = 18
carrera1 = "Tecnologías Biomédicas"

matricula2 = "083208848"
nombre2 = "Martha Alicia"
apellido2 = "Rivera Santos"
notas2 = 98.5
edad2 = 56
carrera2 = "Tecnologías Biomédicas"

matricula3 = "209550194"
nombre3 = "Erika Janeth"
apellido3 = "Correa Rodríguez"
notas3 = 94
edad3 = 30
carrera3 = "Tecnologías Biomédicas"

matricula4 = "221463876"
nombre4 = "Valeria Carolina"
apellido4 = "Luna Silva"
notas4 = 97.33
edad4 = 18
carrera4 = "Tecnologías Biomédicas"

matricula5 = "221226637"
nombre5 = "Carlos Alberto"
apellido5 = "Gil Martínez"
notas5 = 86
edad5 = 19
carrera5 = "Tecnologías Biomédicas"

matricula6 = "221930172"
nombre6 = "Reyna Esmeralda"
apellido6 = "Aguilera Galán"
notas6 = 93
edad6 = 20
carrera6 = "Tecnologías Biomédicas"

matricula7 = "221461407"
nombre7 = "Edna Naomi"
apellido7 = "Martín Gallardo"
notas7 = 95.5
edad7 = 18
carrera7 = "Tecnologías Biomédicas"

matricula8 = "221049972"
nombre8 = "Yahir"
apellido8 = "Mejía Vázquez"
notas8 = 98
edad8 = 18
carrera8 = "Tecnologías Biomédicas"

matricula9 = "221773743"
nombre9 = "Jacob"
apellido9 = "Ávila Núñez"
notas9 = 92.33
edad9 = 19
carrera9 = "Tecnologías Biomédicas"

matricula10 = "221579726"
nombre10 = "Quehat Merari Uziel"
apellido10 = "Martínez Castro"
notas10 = 90
edad10 = 18
carrera10 = "Tecnologías Biomédicas"

matricula11 = "224164501"
nombre11 = "Yael"
apellido11 = "Gómez Gómez"
notas11 = 95.5
edad11 = 19
carrera11 = "Tecnologías Biomédicas"

matricula12 = "207593732"
nombre12 = "Eddy Armando"
apellido12 = "De la Cruz Huezo"
notas12 = 90.6
edad12 = 32
carrera12 = "Tecnologías Biomédicas"

matricula13 = "221594946"
nombre13 = "Angel Antonio"
apellido13 = "Torres Bermúdez"
notas13 = 93
edad13 = 18
carrera13 = "Tecnologías Biomédicas"


# Le pedimos al usuario que elija una opcion 
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

    opcion = input("Seleccione una opción: ")
    
    # Creamos las condicionales
    if opcion == 1:
        matricula = input("Ingrese la matricula: ")
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = input("Ingrese la edad: ")
        carrera = input("Ingrese la carrera")
        
