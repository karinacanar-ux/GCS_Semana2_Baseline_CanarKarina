"""Pruebas básicas de la aplicación de cobranzas."""

import unittest

from src.app import determinar_prioridad


class TestDeterminarPrioridad(unittest.TestCase):

    def test_prioridad_alta(self):
        self.assertEqual(determinar_prioridad(60, 400.00), "ALTA")

    def test_prioridad_media(self):
        self.assertEqual(determinar_prioridad(30, 300.00), "MEDIA")

    def test_prioridad_baja(self):
        self.assertEqual(determinar_prioridad(10, 200.00), "BAJA")


if __name__ == "__main__":
    unittest.main()