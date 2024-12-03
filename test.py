import unittest

from main import (
    get_invest_distributions,
    PROFIT,
    DISTRIBUTIONS,
    PARAM_ERR_MSG,
    ProfitValueError,
    NEG_PROFIT_ERR_MSG,
    DECR_PROFIT_ERR_MSG,
)


class TestDistribution(unittest.TestCase):
    def __check_distribution(self, matrix, profit_to_check, distributions):
        """Проверяет соответствие суммы прибыли указанному распределению
        инвестиций между проектами"""
        for distribution in distributions:
            sum_profit = 0
            if len(distribution) != len(matrix[0]):
                return False
            for project_idx in range(len(distribution)):
                if (distribution[project_idx]) != 0:
                    sum_profit += (matrix)[distribution[project_idx] - 1][project_idx]
            return sum_profit == profit_to_check

    def test_none(self):
        """Проверяет выброс исключения при передаче None в качестве параметра"""
        self.assertRaisesRegex(
            ValueError, PARAM_ERR_MSG, get_invest_distributions, None
        )

    def test_empty(self):
        """Проверяет выброс исключения при передаче пустого списка в
        качестве параметра"""
        self.assertRaisesRegex(ValueError, PARAM_ERR_MSG, get_invest_distributions, [])

    def test_empty_row(self):
        """Проверяет выброс исключения при передаче списка с пустым списком в
        качестве параметра"""
        self.assertRaisesRegex(
            ValueError, PARAM_ERR_MSG, get_invest_distributions, [[]]
        )

    def test_incorrect_values(self):
        """Проверяет выброс исключения при наличии в матрице некорректных
        значений"""
        incorrect_values = [None, "str", []]
        for value in incorrect_values:
            self.assertRaisesRegex(
                ValueError, PARAM_ERR_MSG, get_invest_distributions, [[1, value]]
            )

    def test_jag(self):
        """Проверяет выброс исключения при наличии в матрице строк разной
        длины"""
        matrix = [[1.0, 2.0, 3.0], [1.0, 2.0]]
        self.assertRaisesRegex(
            ValueError, PARAM_ERR_MSG, get_invest_distributions, matrix
        )

    def test_negative_profit(self):
        """Проверяет выброс исключения при наличии в матрице отрицательных
        значений"""
        with self.assertRaises(ProfitValueError) as error:
            get_invest_distributions([[1, -1]])
        self.assertEqual(NEG_PROFIT_ERR_MSG, str(error.exception))
        self.assertEqual(1, error.exception.project_idx)
        self.assertEqual(0, error.exception.row_idx)

    def test_non_decreasing_sequence(self):
        """Проверяет выброс исключения при наличии в матрице убывающей прибыли
        для какого-либо проекта"""
        matrix = [[1, 1, 1], [2, 3, 2], [2, 2, 3]]
        with self.assertRaises(ProfitValueError) as error:
            get_invest_distributions(matrix)
        self.assertEqual(DECR_PROFIT_ERR_MSG, str(error.exception))
        self.assertEqual(1, error.exception.project_idx)
        self.assertEqual(2, error.exception.row_idx)

    def test_single_value(self):
        """Проверяет распределение инвестиций при наличии одного проекта и
        одного уровня"""
        matrix = [[1]]
        result = get_invest_distributions(matrix)
        self.assertEqual(result[PROFIT], 1)
        self.assertEqual(len(result[DISTRIBUTIONS]), 1)
        self.assertTrue(
            self.__check_distribution(matrix, result[PROFIT], result[DISTRIBUTIONS])
        )

    def test_single_level(self):
        """Проверяет распределение инвестиций при наличии одного уровня и
        двух проектов"""
        matrix = [[1, 2]]
        result = get_invest_distributions(matrix)
        self.assertEqual(result[PROFIT], 2)
        self.assertEqual(len(result[DISTRIBUTIONS]), 1)
        self.assertTrue(
            self.__check_distribution(matrix, result[PROFIT], result[DISTRIBUTIONS])
        )

    def test_double_level(self):
        """Проверяет распределение инвестиций при наличии двух уровней и
        двух проектов"""
        matrix = [[1, 2], [3, 5]]
        result = get_invest_distributions(matrix)
        self.assertEqual(result[PROFIT], 5)
        self.assertEqual(len(result[DISTRIBUTIONS]), 1)
        self.assertTrue(
            self.__check_distribution(matrix, result[PROFIT], result[DISTRIBUTIONS])
        )

    def test_multi_level(self):
        """Проверяет распределение инвестиций при наличии трех уровней и
        трех проектов, пример распределения: [3, 0, 0] или [0, 2, 1]"""
        matrix = [[1, 2, 2], [3, 5, 4], [7, 6, 5]]
        result = get_invest_distributions(matrix)
        self.assertEqual(result[PROFIT], 7)
        self.assertEqual(len(result[DISTRIBUTIONS]), 2)
        self.assertTrue(
            self.__check_distribution(matrix, result[PROFIT], result[DISTRIBUTIONS])
        )

    def test_multi_distribution(self):
        """Проверяет распределение инвестиций при большом количестве вариантов
        распределения"""
        matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        result = get_invest_distributions(matrix)
        self.assertEqual(result[PROFIT], 3)
        self.assertEqual(len(result[DISTRIBUTIONS]), 10)
        self.assertTrue(
            self.__check_distribution(matrix, result[PROFIT], result[DISTRIBUTIONS])
        )

    def test_1(self):
        """Проверяет распределение инвестиций,
        пример распределения: [1, 1, 2, 1]"""
        matrix = [
            [15, 18, 16, 17],
            [20, 22, 23, 19],
            [26, 28, 27, 25],
            [34, 33, 29, 31],
            [40, 39, 41, 37],
        ]
        result = get_invest_distributions(matrix)
        self.assertEqual(result[PROFIT], 73)
        self.assertEqual(len(result[DISTRIBUTIONS]), 1)
        self.assertTrue(
            self.__check_distribution(matrix, result[PROFIT], result[DISTRIBUTIONS])
        )

    def test_2(self):
        """Проверяет распределение инвестиций,
        пример распределения: [2, 1, 0, 2]"""
        matrix = [
            [5, 7, 2, 10],
            [9, 8, 4, 15],
            [11, 10, 5, 16],
            [12, 12, 8, 17],
            [14, 15, 9, 18],
        ]
        result = get_invest_distributions(matrix)
        self.assertEqual(result[PROFIT], 31)
        self.assertEqual(len(result[DISTRIBUTIONS]), 1)
        self.assertTrue(
            self.__check_distribution(matrix, result[PROFIT], result[DISTRIBUTIONS])
        )

    def test_3(self):
        """Проверяет распределение инвестиций,
        пример распределения: [0, 0, 0, 5], [5, 0, 0, 0]"""
        matrix = [
            [5, 3, 7, 6],
            [9, 10, 11, 12],
            [17, 21, 23, 16],
            [28, 35, 32, 29],
            [43, 41, 40, 43],
        ]
        result = get_invest_distributions(matrix)
        self.assertEqual(result[PROFIT], 43)
        self.assertEqual(len(result[DISTRIBUTIONS]), 2)
        self.assertTrue(
            self.__check_distribution(matrix, result[PROFIT], result[DISTRIBUTIONS])
        )

    def test_4(self):
        """Проверяет распределение инвестиций,
        пример распределения: [0, 1, 3, 1, 0, 0]"""
        matrix = [
            [3, 5, 4, 7, 1, 2],
            [7, 10, 8, 9, 8, 6],
            [9, 12, 14, 10, 9, 8],
            [13, 15, 16, 14, 11, 17],
            [16, 18, 19, 15, 15, 21],
        ]
        result = get_invest_distributions(matrix)
        self.assertEqual(result[PROFIT], 26)
        self.assertEqual(len(result[DISTRIBUTIONS]), 1)
        self.assertTrue(
            self.__check_distribution(matrix, result[PROFIT], result[DISTRIBUTIONS])
        )


if __name__ == "__main__":
    unittest.main()
