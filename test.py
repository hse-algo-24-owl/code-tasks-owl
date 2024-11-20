import unittest

from main import calculate_determinant


class TestDeterminant(unittest.TestCase):
    """Набор тестов для проверки функции вычисления определителя
    целочисленной квадратной матрицы"""

    def test_none(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр значения None"""
        self.assertRaises(Exception, calculate_determinant, None)

    def test_empty_matrix(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр пустого списка"""
        self.assertRaises(Exception, calculate_determinant, [])

    def test_first_order(self):
        """Проверяет расчет определителя для матрицы порядка 1"""
        matrix = [[1]]
        self.assertEqual(calculate_determinant(matrix), 1)

    def test_second_order(self):
        """Проверяет расчет определителя для матрицы порядка 2"""
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(calculate_determinant(matrix), -2)

    def test_not_square_rectangle(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр прямоугольной матрицы"""
        matrix = [[3, -3, -5, 8], [-3, 2, 4, -6], [-4, 3, 5, -6]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_not_square_jag(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр матрицы с различной длиной строк"""
        matrix = [[3, -3, -5, 8], [-3, 2, 4, -6], [2, -5, -7], [-4, 3, 5, -6]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_third_order(self):
        """Проверяет расчет определителя для матрицы порядка 3"""
        matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        self.assertEqual(calculate_determinant(matrix), 0)

    def test_fourth_order(self):
        """Проверяет расчет определителя для матрицы порядка 4"""
        matrix = [[3, -3, -5, 8], [-3, 2, 4, -6], [2, -5, -7, 5], [-4, 3, 5, -6]]
        self.assertEqual(calculate_determinant(matrix), 18)

    def test_large(self):
        """Проверяет расчет определителя для матрицы порядка 10"""
        matrix = [
            [3, 7, -5, 1, 19, 5, 0, -2, 4, 10],
            [-2, 2, 4, -6, 1, 0, 3, 5, 7, 1],
            [5, -5, -7, 5, 8, 9, -1, 0, 2, 2],
            [-4, 3, 5, -6, 17, -1, 9, 0, 2, 3],
            [3, -3, -5, 8, -9, -1, 0, 2, 4, 7],
            [-3, 2, 4, -6, 1, 0, 3, 5, 7, 11],
            [2, -5, -7, 7, 8, 9, -1, 0, -2, 5],
            [-4, 3, 15, -6, 7, -1, 9, 1, 2, 13],
            [3, -3, -5, 8, 9, -1, 0, 2, 4, 17],
            [-13, 2, 4, -6, 1, 0, -3, 5, 7, 1],
        ]
        self.assertEqual(calculate_determinant(matrix), 4204289520)


if __name__ == "__main__":
    unittest.main()
