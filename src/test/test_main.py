from main import validar_longitud

def test_longitud_valida():
    #estamos validando que nuestra cadena "Hola" "Python" y "12345678"
    assert validar_longitud("Hola") == True
    assert validar_longitud("Python") == True
    assert validar_longitud("12345678") == True

#estamos validando que nuestra cadena "" "Hola, mundo" y "12345678"
def test_longitud_invalida():
    assert validar_longitud("") == False
    assert validar_longitud("Hola, mundo") == False
    assert validar_longitud("1234567890") == False