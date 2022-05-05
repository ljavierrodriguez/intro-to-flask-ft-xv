""" 

Abstraccion
Encapsulamiento
Polimorfismo
Herencia

"""

class Persona:
    nombre = ""
    apellido = ""
    edad = ""
    genero = ""

    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def comer(self):
        pass

    def correr(self):
        self.comer()


class Estudiante(Persona):
    facultad = ""
    def __init__(self, nombre, apellido, edad, genero, facultad):
        super().__init__(nombre, apellido, edad, genero)
        self.facultad = facultad


persona = Persona("Maria", "Herrera", 25, "Femenina")
print(persona.nombre)

est = Estudiante("Maria", "Herrera", 25, "Femenina", "Derecho")
print(est.nombre)