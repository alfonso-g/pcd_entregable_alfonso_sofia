import pytest
from Gestion_universidad import Persona, MiembroDepartamento, Investigador, Profesor, ProfesorTitular, ProfesorAsociado, Estudiante, Departamento, Administrador

def test_persona():
    persona = Persona("Juan", "12345678Z", "Calle Falsa 123", "V")
    assert persona.nombre == "Juan"
    assert persona.dni == "12345678Z"
    assert persona.direccion == "Calle Falsa 123"
    assert persona.sexo == "V"

def test_miembro_departamento():
    miembro = MiembroDepartamento("Ana", "87654321A", "Calle Verdadera 321", "M", Departamento.DIIC)
    assert miembro.nombre == "Ana"
    assert miembro.departamento == Departamento.DIIC

def test_investigador():
    investigador = Investigador("Pedro", "23456789B", "Avenida Siempre Viva 456", "V", Departamento.DITEC, "Inteligencia Artificial")
    assert investigador.area_investigacion == "Inteligencia Artificial"

def test_profesor():
    profesor = Profesor("Maria", "98765432C", "Plaza Mayor 789", "M", Departamento.DIS, ["Matemáticas", "Física"])
    assert profesor.asignaturas == ["Matemáticas", "Física"]

def test_profesor_titular():
    titular = ProfesorTitular("Carlos", "34567890D", "Paseo de la Castellana 012", "V", Departamento.DIIC, ["Química"], "Química Cuántica")
    assert titular.area_investigacion == "Química Cuántica"
    assert titular.asignaturas == ["Química"]

def test_profesor_asociado():
    asociado = ProfesorAsociado("Laura", "09876543E", "Gran Vía 345", "M", Departamento.DITEC, ["Biología"])
    assert asociado.asignaturas == ["Biología"]

def test_estudiante():
    estudiante = Estudiante("Pablo", "45678901F", "Calle del Prado 678", "V", ["Historia", "Geografía"])
    assert estudiante.asignaturas_matriculadas == ["Historia", "Geografía"]

def test_administrador():
    admin = Administrador()
    estudiante = Estudiante("Pablo", "45678901F", "Calle del Prado 678", "V", ["Historia", "Geografía"])
    admin.añadir_estudiante(estudiante)
    assert estudiante in admin.estudiantes
    admin.eliminar_estudiante(estudiante)
    assert estudiante not in admin.estudiantes
