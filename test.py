import unittest

from main import generate_permutations


class TestPermutation(unittest.TestCase):
    """Класс для проверки генерации перестановок множества"""

    def test_incorrect_inputs(self):
        """Проверка выброса TypeError исключения при передаче
        в параметр некорректного значения"""
        incorrect_inputs = (None, "string", 1.1, {1, 2, 3}, (1, 2, 3))
        for val in incorrect_inputs:
            self.assertRaisesRegex(
                TypeError,
                "Параметр items не является списком",
                generate_permutations,
                val,
            )

    def test_duplicates(self):
        """Проверка выброса ValueError исключения при передаче
        в параметр списка с дубликатами"""
        self.assertRaisesRegex(
            ValueError,
            "Список элементов содержит дубликаты",
            generate_permutations,
            [1, 1, 2, 3],
        )

    def test_empty(self):
        """Проверка генерации перестановок для пустого множества"""
        self.assertCountEqual([], generate_permutations([]))

    def test_single_num(self):
        """Проверка генерации перестановок для множества из одного числа"""
        self.assertCountEqual([[1]], generate_permutations([1]))

    def test_double_num(self):
        """Проверка генерации перестановок для множества из двух чисел"""
        self.assertCountEqual([[1, 2], [2, 1]], generate_permutations([1, 2]))

    def test_double_bool(self):
        """Проверка генерации перестановок для множества из двух логических
        значений"""
        self.assertCountEqual(
            [[True, False], [False, True]],
            generate_permutations([True, False]),
        )

    def test_triple_num(self):
        """Проверка генерации перестановок для множества из трех чисел"""
        self.assertCountEqual(
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
            generate_permutations([1, 2, 3]),
        )

    def test_triple_char(self):
        """Проверка генерации перестановок для множества из трех символов"""
        self.assertCountEqual(
            [
                ["a", "b", "c"],
                ["a", "c", "b"],
                ["b", "a", "c"],
                ["b", "c", "a"],
                ["c", "a", "b"],
                ["c", "b", "a"],
            ],
            generate_permutations(["a", "b", "c"]),
        )

    def test_quadruple_num(self):
        """Проверка генерации перестановок для множества из четырех чисел"""
        self.assertCountEqual(
            [
                [1, 2, 3, 4],
                [1, 2, 4, 3],
                [1, 3, 2, 4],
                [1, 3, 4, 2],
                [1, 4, 2, 3],
                [1, 4, 3, 2],
                [2, 1, 3, 4],
                [2, 1, 4, 3],
                [2, 3, 1, 4],
                [2, 3, 4, 1],
                [2, 4, 1, 3],
                [2, 4, 3, 1],
                [3, 1, 2, 4],
                [3, 1, 4, 2],
                [3, 2, 1, 4],
                [3, 2, 4, 1],
                [3, 4, 1, 2],
                [3, 4, 2, 1],
                [4, 1, 2, 3],
                [4, 1, 3, 2],
                [4, 2, 1, 3],
                [4, 2, 3, 1],
                [4, 3, 1, 2],
                [4, 3, 2, 1],
            ],
            generate_permutations([1, 2, 3, 4]),
        )


if __name__ == "__main__":
    unittest.main()
