import unittest

from main import get_tridiagonal_determinant


class TestTridiagonalDeterminant(unittest.TestCase):
    def test_none(self):
        """Проверяет выброс исключения при передаче в параметре None"""
        self.assertRaisesRegex(
            Exception,
            "Параметр не является трехдиагональной матрицей",
            get_tridiagonal_determinant,
            None,
        )

    def test_empty_matrix(self):
        """Проверяет выброс исключения при передаче в параметре пустого списка"""
        self.assertRaisesRegex(
            Exception,
            "Параметр не является трехдиагональной матрицей",
            get_tridiagonal_determinant,
            [],
        )

    def test_not_square_rectangle(self):
        """Проверяет выброс исключения при передаче в параметре прямоугольной матрицы"""
        matrix = [[1, 2, 0, 0], [3, 1, 2, 0], [0, 3, 1, 2]]
        self.assertRaisesRegex(
            Exception,
            "Параметр не является трехдиагональной матрицей",
            get_tridiagonal_determinant,
            matrix,
        )

    def test_not_square_jag(self):
        """Проверяет выброс исключения при передаче в параметре ступенчатой матрицы"""
        matrix = [[1, 2, 0, 0], [3, 1, 2, 0], [0, 3, 1], [0, 0, 3, 1]]
        self.assertRaisesRegex(
            Exception,
            "Параметр не является трехдиагональной матрицей",
            get_tridiagonal_determinant,
            matrix,
        )

    def test_not_tridiag_replace_zero(self):
        """Проверяет выброс исключения при передаче в параметре матрицы с не нулевым
        значением вне диагонали"""
        matrix = [[1, 2, 0, 7], [3, 1, 2, 0], [0, 3, 1, 2], [0, 0, 3, 1]]
        self.assertRaisesRegex(
            Exception,
            "Параметр не является трехдиагональной матрицей",
            get_tridiagonal_determinant,
            matrix,
        )

    def test_wrong_main_diag(self):
        """Проверяет выброс исключения при передаче в параметре матрицы с
        неверным значением на главной диагонали"""
        matrix = [[1, 2, 0, 0], [3, 7, 2, 0], [0, 3, 1, 2], [0, 0, 3, 1]]
        self.assertRaisesRegex(
            Exception,
            "Параметр не является трехдиагональной матрицей",
            get_tridiagonal_determinant,
            matrix,
        )

    def test_wrong_up_diag(self):
        """Проверяет выброс исключения при передаче в параметре матрицы с
        неверным значением на верхней диагонали"""
        matrix = [[1, 7, 0, 0], [3, 1, 2, 0], [0, 3, 1, 2], [0, 0, 3, 1]]
        self.assertRaisesRegex(
            Exception,
            "Параметр не является трехдиагональной матрицей",
            get_tridiagonal_determinant,
            matrix,
        )

    def test_wrong_low_diag(self):
        """Проверяет выброс исключения при передаче в параметре матрицы с
        неверным значением на нижней диагонали"""
        matrix = [[1, 2, 0, 0], [3, 1, 2, 0], [0, 3, 1, 2], [0, 0, 7, 1]]
        self.assertRaisesRegex(
            Exception,
            "Параметр не является трехдиагональной матрицей",
            get_tridiagonal_determinant,
            matrix,
        )

    def test_first_order(self):
        """Проверяет вычисление определителя для матрицы первого порядка"""
        matrix = [[1]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 1)

    def test_second_order(self):
        """Проверяет вычисление определителя для матрицы второго порядка"""
        matrix = [[1, 2], [2, 1]]
        self.assertEqual(get_tridiagonal_determinant(matrix), -3)

    def test_third_order(self):
        """Проверяет вычисление определителя для матрицы третьего порядка"""
        matrix = [[1, -2, 0], [-4, 1, -2], [0, -4, 1]]
        self.assertEqual(get_tridiagonal_determinant(matrix), -15)

    def test_fourth_order(self):
        """Проверяет вычисление определителя для матрицы четвертого порядка"""
        matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 421)

    def test_large(self):
        """Проверяет вычисление определителя для матрицы десятого порядка"""
        matrix = [
            [1, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 1, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 3, 1, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 1, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 3, 1, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 1, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 1, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 3, 1, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 3, 1, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
        ]
        self.assertEqual(get_tridiagonal_determinant(matrix), 5059)


if __name__ == "__main__":
    unittest.main()
