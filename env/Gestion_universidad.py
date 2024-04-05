from enum import Enum
class ESexo(Enum):
    V = 1
    M = 2

class Persona:
    def __init__(self, nombre, dni, direccion, sexo):
        if not nombre.isalpha():
            raise ValueError("El nombre solo puede contener letras")
        self.nombre = nombre

        if len(dni) != 9:
            raise ValueError("El DNI debe tener 9 caracteres")
        self.dni = dni

        self.direccion = direccion

        if not isinstance(sexo, ESexo):
            raise ValueError("El sexo debe ser una instancia de la clase Sexo (V o M)")
        self.sexo = sexo


class EDepartamento(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3

class MiembroDepartamento(Persona):
    def __init__(self, nombre, dni, direccion, sexo, departamento):
        super().__init__(nombre, dni, direccion, sexo)
        self.departamento = departamento

    def cambiar_departamento(self, nuevo_departamento):
        if not isinstance(nuevo_departamento, EDepartamento):
            raise ValueError("El nuevo departamento debe ser un objeto de la clase Departamento")
        self.departamento = nuevo_departamento


class Investigador(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        self.area_investigacion = area_investigacion


class Asignatura:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.estudiantes = []
        self.profesores = []


    def agregar_estudiante(self, estudiante):
        if isinstance(estudiante, Estudiante):
            self.estudiantes.append(estudiante)
        else:
            raise ValueError("El objeto proporcionado no es una instancia de la clase Estudiante")

    def agregar_profesor(self, profesor):
        if isinstance(profesor, Profesor):
            self.profesores.append(profesor)
        else:
            raise ValueError("El objeto proporcionado no es una instancia de la clase Profesor")
    def __str__(self):
        estudiantes = ", ".join([estudiante.nombre for estudiante in self.estudiantes])
        profesores = ", ".join([profesor.nombre for profesor in self.profesores])
        return f"Asignatura: {self.nombre}\nCódigo: {self.codigo}\nEstudiantes: {estudiantes}\nProfesores: {profesores}"


class Profesor(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, departamento, asignaturas):
        super().__init__(nombre, dni, direccion, sexo, departamento)
        
        for asignatura in asignaturas:
            if not isinstance(asignatura, Asignatura):
                raise ValueError("Las asignaturas deben ser proporcionadas como una lista de objetos de la clase Asignatura")
        
        self.asignaturas = asignaturas

    def listar_asignaturas(self):
        return [asignatura.nombre for asignatura in self.asignaturas]

#Heredan de profesor
#---------------------------------------------------------------------------------

class ProfesorTitular(Profesor, Investigador):
    def __init__(self, nombre, dni, direccion, sexo, departamento, asignaturas, area_investigacion):
        Profesor.__init__(self, nombre, dni, direccion, sexo, departamento, asignaturas)
        Investigador.__init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion)


class ProfesorAsociado(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, departamento, asignaturas):
        super().__init__(nombre, dni, direccion, sexo, departamento, asignaturas)

#---------------------------------------------------------------------------------


class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo, asignaturas_matriculadas):
        super().__init__(nombre, dni, direccion, sexo)
        
        for asignatura in asignaturas_matriculadas:
            if not isinstance(asignatura, Asignatura):
                raise ValueError("La lista de asignaturas matriculadas debe contener solo objetos de la clase Asignatura")
        
        self.asignaturas_matriculadas = asignaturas_matriculadas

     def listar_asignaturas(self):
        return [asignatura.nombre for asignatura in self.asignaturas_matriculadas]

class ErrorAdministrador(Exception):
    pass


class Administrador:
    def __init__(self):
        self.estudiantes = []
        self.miembros_departamento = []

    def añadir_estudiante(self, estudiante):
        if not isinstance(estudiante, Estudiante):
            raise ErrorAdministrador("El objeto no es un estudiante")
        self.estudiantes.append(estudiante)

    def eliminar_estudiante(self, estudiante):
        try:
            self.estudiantes.remove(estudiante)
        except ValueError:
            raise ErrorAdministrador("El estudiante no está en la lista")

    def añadir_miembro_departamento(self, miembro):
        if not isinstance(miembro, MiembroDepartamento):
            raise ErrorAdministrador("El objeto no es un miembro del departamento")
        self.miembros_departamento.append(miembro)

    def eliminar_miembro_departamento(self, miembro):
        try:
            self.miembros_departamento.remove(miembro)
        except ValueError:
            raise ErrorAdministrador("El miembro del departamento no está en la lista")