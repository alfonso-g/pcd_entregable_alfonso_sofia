import pytest
from Gestion_universidad import Persona, Estudiante

def test_persona():
    persona = Persona("Juan", "12345678Z", "Calle Falsa 123", "V")
    assert persona.nombre == "Juan"
    assert persona.dni == "12345678Z"

def test_estudiante():
    estudiante = Estudiante("Pablo", "45678901F", "Calle del Prado 678", "V", ["Historia", "Geografía"])
    assert estudiante.asignaturas_matriculadas == ["Historia", "Geografía"]
