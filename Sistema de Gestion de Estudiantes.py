Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Creamos un diccionario para poder acceder a los estudiantes desde su matricula 
... estudiantes = {}
... 
... # Lista de materias que todos los estudiantes deben tener
... materias = [
...     "Fisica Biomedica I",
...     "Quimica General y Organica",
...     "Programacion I",
...     "Ciencias Biologicas I"
... ]
... 
... # Creamos la lista de los estudiantes con sus calificaciones
... datos_iniciales = [ 
...         ("221461768", "Samanta Julieth", "Torres Rodríguez", 18, "Tecnologías Biomédicas", 
...          {"Fisica Biomedica I": 95.5, "Quimica General y Organica": 97.2, "Programacion I": 98.0, "Ciencias Biologicas I": 97.8}),
...         ("083208848", "Martha Alicia", "Rivera Santos", 56, "Tecnologías Biomédicas",
...          {"Fisica Biomedica I": 98.0, "Quimica General y Organica": 99.0, "Programacion I": 97.5, "Ciencias Biologicas I": 99.5}),
...         ("209550194", "Erika Janeth", "Correa Rodríguez", 30, "Tecnologías Biomédicas",
...          {"Fisica Biomedica I": 94.0, "Quimica General y Organica": 93.5, "Programacion I": 95.0, "Ciencias Biologicas I": 93.5}),
...         ("221463876", "Valeria Carolina", "Luna Silva", 18, "Tecnologías Biomédicas",
...          {"Fisica Biomedica I": 97.0, "Quimica General y Organica": 98.0, "Programacion I": 96.8, "Ciencias Biologicas I": 97.5}),
...         ("221226637", "Carlos Alberto", "Gil Martínez", 19, "Tecnologías Biomédicas",
...          {"Fisica Biomedica I": 85.5, "Quimica General y Organica": 86.0, "Programacion I": 87.0, "Ciencias Biologicas I": 85.5}),
...         ("221930172", "Reyna Esmeralda", "Aguilera Galán", 20, "Tecnologías Biomédicas",
...          {"Fisica Biomedica I": 92.5, "Quimica General y Organica": 93.0, "Programacion I": 94.0, "Ciencias Biologicas I": 92.5}),
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
