import pytest
import tateti

def test_quien_comienza():
    assert type(tateti.quien_comienza()) is bool 

def test_posicion_invalida():
    assert type(tateti.posicion_invalida('a')) is not None

def test_posicion_invalida_type():
    assert type(tateti.posicion_invalida("5")) is bool

def test_posicion_invalida_numeros_correctos(): 
    assert tateti.posicion_invalida("5") is True

def test_posicion_invalida_numeros_incorrectos(): 
    assert tateti.posicion_invalida("11") is False

def test_posicion_invalida_letras(): 
    assert tateti.posicion_invalida("a") is False

def test_posicion_invalida_caracteres_especiales(): 
    assert tateti.posicion_invalida("%?") is False

def test_tablero_lleno():
    assert tateti.tablero_lleno([""]) is not None

def test_tablero_lleno_type():
    assert type(tateti.tablero_lleno([""])) is bool

def test_tablero_lleno_ocupado():
    assert tateti.tablero_lleno(["5"]) is True
