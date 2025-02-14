# Proyecto-Sistema-de-Gesti-n-de-Estudiantes
# Proyecto de Programación I basado en un sistema de gestión de estudiantes usando los conocimientos adquiridos hasta ahora 

# Definimos variables para almacenar la informacion de los estudiantes
matricula1 = "221461768"
nombre1 = "Samanta Julieth"
apellido1 = "Torres Rodríguez"
notas1 = 97.13

matricula2 = "083208848"
nombre2 = "Martha Alicia"
apellido2 = "Rivera Santos"
notas2 = 98.5

matricula3 = "209550194"
nombre3 = "Erika Janeth"
apellido3 = "Correa Rodríguez"
notas3 = 94

matricula4 = "221463876"
nombre4 = "Valeria Carolina"
apellido4 = "Luna Silva"
notas4 = 97.33

matricula5 = "221226637"
nombre5 = "Carlos Alberto"
apellido5 = "Gil Martinez"
notas5 = 86

matricula6 = "221930172"
nombre6 = "Reyna Esmeralda"
apellido6 = "Aguilera Galan"
notas6 = 93

matricula7 = "221461407"
nombre7 = "Edna Naomi"
apellido7 = "Martín Gallardo"
notas7 = 95.5

matricula8 = "221049972"
nombre8 = "Yahir"
apellido8 = "Mejia Vazquez"
notas8 = 98

matricula9 = "221773743"
nombre9 = "Jacob"
apellido9 = "Avila Nuñez"
notas9 = 92.33

matricula10 = "221579726"
nombre10 = "Quehat Merari Uziel"
apellido10 = "Martínez Castro"
notas10 = 90

matricula11 = "224164501"
nombre11 = "Yael"
apellido11 = "Gomez Gomez"
notas11 = 95.5

# Le pedimos al usuario que elija una opcion 
while True:
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Modificar estudiante")
    print("5. Mostrar lista de estudiantes")
    print("6. Calcular el promedio del estudiante")
    print("7. Mostrar notas del estudiante")
    print("8. Generar un reporte de notas")
    print("9. Generar un reporte de asistencia")
    print("10. Salir")

    opcion = int(input("Elije una opcion del 1 al 10"))

    # Creamos las condicionales
    if opcion == 1:
        matricula = input("Ingrese la matricula: ")
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = input("Ingrese la edad: ")
        carrera = input("Ingrese la carrera")
        
