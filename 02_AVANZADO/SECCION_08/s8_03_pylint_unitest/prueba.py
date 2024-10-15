import unittest
import s08_03_02_unitest


class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = s08_03_02_unitest.todo_mayusculas(palabra)
        self.assertEqual(resultado, "BUEN DIA")


if __name__ == "__main__":
    unittest.main()
