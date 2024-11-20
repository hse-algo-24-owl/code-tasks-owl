import unittest

from main import rabbits

MONTH = "month"
LIFETIME = "lifetime"
RABBITS = "rabbits"
IS_RABBIT_IMPLEMENTED = bool(rabbits(1, 2))


class TestRabbits(unittest.TestCase):
    """Тесты для проверки функций вычисления количества пар кроликов"""

    def test_rabbits(self):
        """Проверка работы функции расчета количества пар кроликов с
        установленной продолжительностью жизни"""

        test_data = [
            {MONTH: 1, LIFETIME: 2, RABBITS: 1},
            {MONTH: 2, LIFETIME: 2, RABBITS: 1},
            {MONTH: 3, LIFETIME: 7, RABBITS: 2},
            {MONTH: 3, LIFETIME: 8, RABBITS: 2},
            {MONTH: 4, LIFETIME: 8, RABBITS: 3},
            {MONTH: 5, LIFETIME: 6, RABBITS: 5},
            {MONTH: 6, LIFETIME: 8, RABBITS: 8},
            {MONTH: 7, LIFETIME: 9, RABBITS: 13},
            {MONTH: 8, LIFETIME: 7, RABBITS: 20},
            {MONTH: 9, LIFETIME: 9, RABBITS: 34},
            {MONTH: 35, LIFETIME: 5, RABBITS: 504355},
            {MONTH: 50, LIFETIME: 5, RABBITS: 155898016},
        ]
        for data in test_data:
            self.assertEqual(data[RABBITS], rabbits(data[MONTH], data[LIFETIME]))


if __name__ == "__main__":
    unittest.main()
