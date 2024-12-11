PROFIT = "profit"
DISTRIBUTION = "distribution"
DISTRIBUTIONS = "distributions"
PARAM_ERR_MSG = (
    "Таблица прибыли от проектов не является прямоугольной "
    "матрицей с числовыми значениями"
)
NEG_PROFIT_ERR_MSG = "Значение прибыли не может быть отрицательно"
DECR_PROFIT_ERR_MSG = "Значение прибыли не может убывать с ростом инвестиций"


class ProfitValueError(Exception):
    def __init__(self, message, project_idx, row_idx):
        self.project_idx = project_idx
        self.row_idx = row_idx
        super().__init__(message)


def get_invest_distributions(
    profit_matrix: list[list[int]],
) -> dict[str:int, str : list[list[int]]]:
    """Рассчитывает максимально возможную прибыль и распределение инвестиций
    между несколькими проектами. Инвестиции распределяются кратными частями.
    :param profit_matrix: Таблица с распределением прибыли от проектов в
    зависимости от уровня инвестиций. Проекты указаны в столбцах, уровни
    инвестиций в строках.
    :raise ValueError: Если таблица прибыли от проектов не является
    прямоугольной матрицей с числовыми значениями.
    :raise ProfitValueError: Если значение прибыли отрицательно или убывает
    с ростом инвестиций.
    :return: Словарь с ключами:
    profit - максимально возможная прибыль от инвестиций,
    distributions - списком со всеми вариантами распределения инвестиций между
    проектами, обеспечивающими максимальную прибыль.
    """
    # Проверка входных данных

    # Проверка на то, что введена непустая прямоугольная матрица
    if not profit_matrix or not all(
        isinstance(row, list) and row for row in profit_matrix
    ):
        raise ValueError(PARAM_ERR_MSG)

    # Проверка на то, что длина всех строк матрицы одинакова
    rows = len(profit_matrix)
    cols = len(profit_matrix[0])
    if not all(len(row) == cols for row in profit_matrix):
        raise ValueError(PARAM_ERR_MSG)

    # Проверка, что матрица не пуста, состоит только из непустых списков.
    if not profit_matrix or not all(
        isinstance(row, list) and row for row in profit_matrix
    ):
        raise ValueError(PARAM_ERR_MSG)

    for row_idx, row in enumerate(profit_matrix):
        for project_idx, value in enumerate(row):
            if value is None or not isinstance(value, (int, float)):
                raise ValueError(PARAM_ERR_MSG)  # Проверка на то, что элементы числовые
            if value < 0:
                raise ProfitValueError(
                    NEG_PROFIT_ERR_MSG, project_idx, row_idx
                )  # Проверка на то, что значения прибыли не отрицательные.
            if row_idx > 0 and value < profit_matrix[row_idx - 1][project_idx]:
                raise ProfitValueError(
                    DECR_PROFIT_ERR_MSG, project_idx, row_idx
                )  # Проверка на то, что прибыль не убывает с ростом инвестиций.

    # Инициализация DP
    max_profit_table = [
        [0] * (cols + 1) for _ in range(rows + 1)
    ]  # Таблица для хранения максимальной прибыли для каждого уровня инвестиций
    paths = [
        [[] for _ in range(cols + 1)] for _ in range(rows + 1)
    ]  # Таблица для хранения вариантов распределения инвестиций.
    paths[0][0] = [[]]  # Нулевые инвестиции

    for level in range(
        rows + 1
    ):  # Перебор всех возможных сумм инвестиций и фиксация, сколько всего денег доступно для распределения между проектами
        for proj in range(1, cols + 1):  # Перебор проектов
            for invest in range(
                level + 1
            ):  # Цикл отвечает за выбор, сколько конкретно инвестиций выделить текущему проекту
                prev_profit = max_profit_table[level - invest][
                    proj - 1
                ]  # Прибыли от предыдущих проектов при оставшихся инвестициях
                current_profit = (
                    profit_matrix[invest - 1][proj - 1] if invest > 0 else 0
                )  # Прибыль от текущего уровня инвестиций в текущий проект
                total_profit = (
                    prev_profit + current_profit
                )  # Общая прибыль от текущей комбинации

                if (
                    total_profit > max_profit_table[level][proj]
                ):  # Обновление максимальной прибыли и путей, если найден лучший результат.
                    max_profit_table[level][proj] = total_profit
                    paths[level][proj] = [
                        path + [invest] for path in paths[level - invest][proj - 1]
                    ]
                elif (
                    total_profit == max_profit_table[level][proj]
                ):  # Сохранение пути, если прибыль совпадает с текущей максимальной.
                    paths[level][proj] += [
                        path + [invest] for path in paths[level - invest][proj - 1]
                    ]

    max_profit = max_profit_table[rows][cols]
    distributions = paths[rows][cols]
    return {PROFIT: max_profit, DISTRIBUTIONS: distributions}


def main():
    profit_matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    print(get_invest_distributions(profit_matrix))


if __name__ == "__main__":
    main()
