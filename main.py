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
    """ Проверяет корректность введенных данных
    """
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
    
    for project in range (len(profit_matrix)):
        for row in range (len(profit_matrix[project])-1):
            if profit_matrix[project][row] > profit_matrix[project][row+1]:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, project, row+1)
    

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
    validation(profit_matrix)
    pass


def main():
    profit_matrix = [[1, -1]]
    print(get_invest_distributions(profit_matrix))


if __name__ == "__main__":
    main()
