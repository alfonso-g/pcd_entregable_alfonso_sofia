class Persona:
    def __init__(self, nombre, dni, direccion, sexo):
        if not nombre.isalpha():
            raise ValueError("El nombre solo puede contener letras")
        self.nombre = nombre
        if len(dni) != 9:
            raise ValueError("El DNI debe tener 9 caracteres")
        self.dni = dni
        self.direccion = direccion
        if sexo.upper() not in ["V", "M"]:
            raise ValueError("El sexo debe ser 'V' o 'M'")
        self.sexo = sexo.upper()


class MiembroDepartamento(Persona):
    def __init__(self, nombre, dni, direccion, sexo, departamento):
        super().__init__(nombre, dni, direccion, sexo)
        self.departamento = departamento

    def cambiar_departamento(self, nuevo_departamento):
        if not isinstance(nuevo_departamento, Departamento):
            raise ValueError("El nuevo departamento debe ser un objeto de la clase Departamento")
        self.departamento = nuevo_departamento


class Investigador(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        self.area_investigacion = area_investigacion

class Profesor(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, asignaturas):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        if not isinstance(asignaturas, list):
            raise ValueError("Las asignaturas deben ser proporcionadas como una lista")
        self.asignaturas = asignaturas



#Heredan de profesor

class ProfesorTitular(Profesor, Investigador):
    def __init__(self, nombre, dni, direccion, sexo, departamento, asignaturas, area_investigacion):
        Profesor.__init__(self, nombre, dni, direccion, sexo, departamento, asignaturas)
        Investigador.__init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion)


class ProfesorAsociado(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, departamento, asignaturas):
        super().__init__(nombre, dni, direccion, sexo, departamento, asignaturas)


class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo, asignaturas_matriculadas):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas_matriculadas = asignaturas_matriculadas

from enum import Enum
class Departamento(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3

