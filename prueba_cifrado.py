def test_crear_cifradores():

    cesar3 = CrearCifrador(3)
    assert cesar3("A")  == "D"
    assert cesar3("Z")  == "B"