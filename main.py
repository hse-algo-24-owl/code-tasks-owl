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



def validation(profit_matrix: list[list[int]]) -> None:
    """Проверяет корректность введенных данных."""
    if isinstance(profit_matrix, list) == False:
        raise ValueError(PARAM_ERR_MSG)
    
    if len(profit_matrix) == 0:
        raise ValueError(PARAM_ERR_MSG)

    for project in range (len(profit_matrix)):
        if isinstance(profit_matrix[project], list) == False:
            raise ValueError(PARAM_ERR_MSG)
        
        if len(profit_matrix[project]) == 0:
            raise ValueError(PARAM_ERR_MSG)

        for row in range (len(profit_matrix[project])):
            if isinstance(profit_matrix[project][row], int) == False:
                raise ValueError(PARAM_ERR_MSG)
    
    for project in range (len(profit_matrix)):
        for row in range (len(profit_matrix[project])):
            if profit_matrix[project][row] < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, row, project)

    for project in range(len(profit_matrix[0])):
        for row in range(1, len(profit_matrix)):
            if profit_matrix[row][project] < profit_matrix[row - 1][project]:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, project, row)


def get_invest_distributions(
    profit_matrix: list[list[int]],
) -> dict[str:int, str : list[list[int]]]:
    """Рассчитывает максимально возможную прибыль и распределение инвестиций
    между несколькими проектами.
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
    проектами, обеспечивающими максимальную прибыль."""

    validation(profit_matrix)
    level_cnt = len(profit_matrix) 
    proj_cnt = len(profit_matrix[0])

    # Матрица для хранения максимальной прибыли
    max_profit_matrix = [[0] * (proj_cnt + 1) for _ in range(level_cnt + 1)]

    for proj_idx in range(1, proj_cnt + 1):
        for level in range(1, level_cnt + 1):
            max_profit = 0
            for part_for_prev in range(level + 1):
                part_for_curr = level - part_for_prev
                profit_from_prev = max_profit_matrix[part_for_prev][proj_idx - 1]
                profit_from_curr = profit_matrix[part_for_curr - 1][proj_idx - 1] if part_for_curr > 0 else 0
                max_profit = max(max_profit, profit_from_prev + profit_from_curr)
            max_profit_matrix[level][proj_idx] = max_profit


    def restore_paths(level, proj_idx):
        """Восстанавливает все пути, которые приводят к максимальной прибыли."""
        if proj_idx == 0:
            return [[]]

        paths = []
        for part_for_prev in range(level + 1):
            part_for_curr = level - part_for_prev
            profit_from_prev = max_profit_matrix[part_for_prev][proj_idx - 1]
            profit_from_curr = profit_matrix[part_for_curr - 1][proj_idx - 1] if part_for_curr > 0 else 0

            if max_profit_matrix[level][proj_idx] == profit_from_prev + profit_from_curr:
                for path in restore_paths(part_for_prev, proj_idx - 1):
                    paths.append(path + [part_for_curr])
        return paths

    distributions = restore_paths(level_cnt, proj_cnt)
    max_profit = max_profit_matrix[-1][-1]
    return {PROFIT: max_profit, DISTRIBUTIONS: distributions}


def main():
    profit_matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    print(get_invest_distributions(profit_matrix))


if __name__ == "__main__":
    main()
