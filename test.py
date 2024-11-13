import unittest

from main import fibonacci, fibonacci_iter, fibonacci_rec


class TestFibonacci(unittest.TestCase):
    """Тесты для проверки функций вычисления числа Фибоначчи"""

    fibonacci_numbers = [
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
        6765,
        10946,
        17711,
    ]

    def test_fibonacci_rec(self):
        """Проверка работы рекурсивной функции вычисления числа Фибоначчи"""

        for index, fact_number in enumerate(self.fibonacci_numbers):
            expected_number = fibonacci_rec(index + 1)
            self.assertEqual(expected_number, fact_number)

    def test_fibonacci_iter(self):
        """Проверка работы итеративной функции вычисления числа Фибоначчи"""

        for index, fact_number in enumerate(self.fibonacci_numbers):
            expected_number = fibonacci_iter(index + 1)
            self.assertEqual(expected_number, fact_number)

    def test_fibonacci(self):
        """Проверка работы итеративной функции вычисления числа Фибоначчи
        без использования массива"""

        for index, fact_number in enumerate(self.fibonacci_numbers):
            expected_number = fibonacci(index + 1)
            self.assertEqual(expected_number, fact_number)


if __name__ == "__main__":
    unittest.main()
