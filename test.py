from main import Tateti


def test_matriz():
    assert(Tateti.Letra_ABC(0) == "A")

def test_jugador_1():
    t = Tateti("test")
    t.inicializar_tablero()
    t.input_jugador("1", "A1")
    t.input_jugador("2", "A2")
    t.input_jugador("1", "B1")
    t.input_jugador("2", "B2")
    final = t.input_jugador("1", "C1")
    assert("GANO EL JUGADOR 1 [X]" in final)