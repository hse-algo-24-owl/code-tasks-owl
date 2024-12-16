from typing import Generator
import unittest

from main import ErrorMessages, generate_permutations


class TestPermutation(unittest.TestCase):
    """Класс для проверки генерации перестановок множества"""

    def test_incorrect_inputs(self):
        """Проверка выброса TypeError исключения при передаче
        в параметр некорректного значения"""
        incorrect_inputs = (None, "string", 1.1, {1, 2, 3}, (1, 2, 3))
        for val in incorrect_inputs:
            with self.assertRaises(TypeError) as ctx:
                for perm in generate_permutations(val):
                    ...
            self.assertEqual(ErrorMessages.ERROR_ITEMS_NOT_IS_LIST, str(ctx.exception))

    def test_duplicates(self):
        """Проверка выброса ValueError исключения при передаче
        в параметр списка с дубликатами"""
        with self.assertRaises(ValueError) as ctx:
            for perm in generate_permutations([1, 1, 2, 3]):
                ...
        self.assertEqual(ErrorMessages.ERROR_DUPLICATE_ITEMS, str(ctx.exception))

    def test_is_generator(self):
        """Проверка того, что функция возвращает генератор"""
        self.assertIsInstance(generate_permutations([]), Generator)

    def test_empty(self):
        """Проверка генерации перестановок для пустого множества"""
        self.assertCountEqual([[]], generate_permutations([]))

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
            generate_permutations([3, 2, 1]),
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
