PROFIT = "profit"
DISTRIBUTION = "distribution"
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

def validate(profit_matrix):
    if profit_matrix is None or len(profit_matrix) == 0:
        raise ValueError(PARAM_ERR_MSG)

    number_of_investment_levels = len(profit_matrix)
    number_of_projects = len(profit_matrix[0])
    if number_of_projects == 0:
        raise ValueError(PARAM_ERR_MSG)
    
    for i in range(number_of_investment_levels):
        if len(profit_matrix[i]) != number_of_projects:
            raise ValueError(PARAM_ERR_MSG)
        for j in range(number_of_projects):
            if not isinstance(profit_matrix[i][j], int):
                raise ValueError(PARAM_ERR_MSG)
            if profit_matrix[i][j] < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, j, i)
            if i > 0 and profit_matrix[i][j] < profit_matrix[i-1][j]:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, j, i)


def get_invest_distribution(
    profit_matrix: list[list[int]],
) -> dict[str:int, str : list[int]]:
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
    distribution - распределение инвестиций между проектами.
    """
    validate(profit_matrix)
    if profit_matrix is None or len(profit_matrix) == 0 :
        return {PROFIT: 0, DISTRIBUTION: []}
    
    number_of_investment_levels = len(profit_matrix)
    number_of_projects = len(profit_matrix[0])

    max_profits = [[0] * (number_of_investment_levels + 1) for _ in range(number_of_projects)]
    distributions = [[[0] * number_of_projects for _ in range(number_of_investment_levels + 1)] for _ in range(number_of_projects)]

    for project_index in range(number_of_projects):
        for investment_level in range(1, number_of_investment_levels + 1):
            for previous_investment_level in range(investment_level + 1):
                current_project_profit = profit_matrix[previous_investment_level -1][project_index] if previous_investment_level > 0 else 0
                remain_invest = investment_level - previous_investment_level
                total_profit = current_project_profit + (max_profits[project_index - 1][remain_invest] if project_index > 0 else 0)
                if total_profit > max_profits[project_index][investment_level]:
                    max_profits[project_index][investment_level] = total_profit
                    if project_index > 0:
                        distributions[project_index][investment_level] = distributions[project_index - 1][remain_invest][:]
                    distributions[project_index][investment_level][project_index] = previous_investment_level

    max_profit = max_profits[number_of_projects - 1][number_of_investment_levels]
    best_distribution = distributions[number_of_projects - 1][number_of_investment_levels]

    return {PROFIT: max_profit, DISTRIBUTION: best_distribution}


def main():
    profit_matrix = [
        [15, 18, 16, 17],
        [20, 22, 23, 19],
        [26, 28, 27, 25],
        [34, 33, 29, 31],
        [40, 39, 41, 37],
    ]
    print(get_invest_distribution(profit_matrix))


if __name__ == "__main__":
    main()
