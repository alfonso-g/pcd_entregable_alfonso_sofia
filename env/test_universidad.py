import pytest
from Gestion_universidad import *


@pytest.fixture
def asignaturas_ejemplo():
    asignatura1 = Asignatura("Matemáticas", "MAT101")
    asignatura2 = Asignatura("Física", "FIS102")
    return [asignatura1, asignatura2]


@pytest.fixture
def estudiante_ejemplo(asignaturas_ejemplo):
    return Estudiante("Juan", "123456789", "Calle Falsa 123", ESexo.V, asignaturas_ejemplo)


@pytest.fixture
def profesor_ejemplo(asignaturas_ejemplo):
    return Profesor("Dr. Smith", "987654321", "Av. Principal 456", ESexo.M, EDepartamento.DIIC, asignaturas_ejemplo)


def test_asignatura_agregar_estudiante():
    asignatura = Asignatura("Matemáticas", "MAT101")
    estudiante = Estudiante("Juan", "123456789", "Calle Falsa 123", ESexo.V, [])
    asignatura.agregar_estudiante(estudiante)
    assert len(asignatura.estudiantes) == 1


def test_asignatura_agregar_profesor():
    asignatura = Asignatura("Matemáticas", "MAT101")
    profesor = Profesor("Dr. Smith", "987654321", "Av. Principal 456", ESexo.M, EDepartamento.DIIC, [])
    asignatura.agregar_profesor(profesor)
    assert len(asignatura.profesores) == 1


def test_administrador_añadir_estudiante():
    admin = Administrador()
    estudiante = Estudiante("Juan", "123456789", "Calle Falsa 123", ESexo.V, [])
    admin.añadir_estudiante(estudiante)
    assert len(admin.estudiantes) == 1


def test_administrador_añadir_miembro_departamento():
    admin = Administrador()
    profesor = Profesor("Dr. Smith", "987654321", "Av. Principal 456", ESexo.M, EDepartamento.DIIC, [])
    admin.añadir_miembro_departamento(profesor)
    assert len(admin.miembros_departamento) == 1


if __name__ == "__main__":
    pytest.main()
