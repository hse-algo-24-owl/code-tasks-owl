import unittest

from main import hello


class TestHello(unittest.TestCase):
    """Класс для тестирования функции hello"""

    def test_hello(self):
        """Тест для функции hello, проверяет, что функция возвращает
        строку Hello world!"""
        self.assertEqual(hello(), "Hello world!")


if __name__ == "__main__":
    unittest.main()
