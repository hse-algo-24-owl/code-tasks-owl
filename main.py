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

    rows = len(profit_matrix)
    column = len(profit_matrix[0])
    if column == 0:
        raise ValueError(PARAM_ERR_MSG)
    
    for i in range(rows):
        if len(profit_matrix[i]) != column:
            raise ValueError(PARAM_ERR_MSG)
        for j in range(column):
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
    
    rows = len(profit_matrix)
    column = len(profit_matrix[0])
    
    dp = [[0] * (rows + 1) for _ in range(column)]
    distribution = [[[0] * column for _ in range(rows + 1)] for _ in range(column)]

    for j in range(column):
        for i in range(1, rows + 1):
            for k in range(i + 1):
                profit = profit_matrix[k-1][j] if k > 0 else 0
                remain_invest = i - k
                total_profit = profit + dp[j-1][remain_invest] if j > 0 else profit
                if total_profit > dp[j][i]:
                    dp[j][i] = total_profit
                    if j > 0:
                        distribution[j][i] = distribution[j-1][remain_invest][:]
                    distribution[j][i][j] = k

    max_profit = dp[column - 1][rows]
    best_distribution = distribution[column - 1][rows]
    
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
