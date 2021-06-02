from main import Tateti


class TestTateti:
    def test_matriz(self):
        assert(Tateti.Letra_ABC(0) == "A")

    def test_jugador_1_gana_columna_1(self, capsys):
        t = Tateti("test")
        t.inicializar_tablero()
        t.input_jugador("1", "A1")
        t.input_jugador("2", "A2")
        t.input_jugador("1", "B1")
        t.input_jugador("2", "B2")
        t.input_jugador("1", "C1")
        captured = capsys.readouterr()
        assert("GANO EL JUGADOR 1 [X]" in captured.out)
        assert ("GANO EL JUGADOR 2 [0]" not in captured.out)

    def test_bug_2021(self, capsys):
        t = Tateti("test")
        t.inicializar_tablero()
        t.input_jugador("1", "A1")
        t.input_jugador("2", "A2")
        t.input_jugador("1", "B1")
        t.input_jugador("2", "A3")
        t.input_jugador("1", "B3")
        t.input_jugador("2", "B2")
        t.input_jugador("1", "C1")

        captured = capsys.readouterr()

        assert ("GANO EL JUGADOR 1 [X]" in captured.out)
        assert ("GANO EL JUGADOR 2 [0]" not in captured.out)
