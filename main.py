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

def input_check(profit_matrix):
    if profit_matrix is None or not profit_matrix or not profit_matrix[0]:
        raise ValueError(PARAM_ERR_MSG)

    for row_idx, row in enumerate(profit_matrix):
        if len(row) != len(profit_matrix[0]):
            raise ValueError(PARAM_ERR_MSG)
        
        for project_idx, value in enumerate(row):
            if not isinstance(value, int):
                raise ValueError(PARAM_ERR_MSG)
            if value < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, project_idx, row_idx)

    for project_idx in range(len(profit_matrix[0])):
        for row_idx in range(1, len(profit_matrix)):
            if profit_matrix[row_idx][project_idx] < profit_matrix[row_idx - 1][project_idx]:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, project_idx, row_idx)


def get_invest_distributions(
    profit_matrix: list[list[int]],
) -> dict[str:int, str : list[list[int]]]:
    """
    Рассчитывает максимально возможную прибыль и распределение инвестиций
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

    input_check(profit_matrix)

    profits = [[0] * (len(profit_matrix[0]) + 1) for _ in range(len(profit_matrix) + 1)]
    paths = [[[[]] for _ in range(len(profit_matrix[0]) + 1)] for _ in range(len(profit_matrix) + 1)]


    for profit_table_row in range(len(profit_matrix) + 1):
        for project in range(1, len(profit_matrix[0]) + 1):
            for project_depth in range(profit_table_row + 1):
                # Рассчёт прибыли
                if project_depth == 0:
                    profit = profits[profit_table_row - project_depth][project - 1]
                else:
                    profit = profits[profit_table_row - project_depth][project - 1] + profit_matrix[project_depth - 1][project - 1]

                # Обработка путей
                if profit > profits[profit_table_row][project]:
                    profits[profit_table_row][project] = profit
                    paths[profit_table_row][project] = [path + [project_depth] for path in paths[profit_table_row - project_depth][project - 1]]
                elif profit == profits[profit_table_row][project]:
                    paths[profit_table_row][project] += [path + [project_depth] for path in paths[profit_table_row - project_depth][project - 1]]

    return {PROFIT: profits[len(profit_matrix)][len(profit_matrix[0])], DISTRIBUTIONS: [path for path in paths[len(profit_matrix)][len(profit_matrix[0])] if len(path) == len(profit_matrix[0])]}


def main():
    profit_matrix = [[1, 1, 1],
                     [2, 2, 2],
                     [3, 3, 3]]
    print(get_invest_distributions(profit_matrix))


if __name__ == "__main__":
    main()
