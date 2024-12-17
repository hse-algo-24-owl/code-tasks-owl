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
        print(1)
        raise Exception(ValueError)
    for project in range (len(profit_matrix)):
        if isinstance(profit_matrix[project], list) == False:
            print(2)
            raise Exception(ValueError)
        if len(profit_matrix) != len(profit_matrix[project]):
            print(3)
            raise Exception(ValueError)
        for profit in range (len(profit_matrix[project])):
            if isinstance(profit_matrix[project][profit], int) == False:
                print(4)
                raise Exception(ValueError)
            
    for project in range (len(profit_matrix)):
        if profit_matrix[project][0] < 0:
            raise Exception(ProfitValueError)
        for profit in range (len(profit_matrix[project])-1):
            if profit_matrix[project][profit] > profit_matrix[project][profit+1] or profit_matrix[project][profit+1] < 0:
                raise Exception(ProfitValueError)
            
    

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
    profit_matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    print(get_invest_distributions(profit_matrix))


if __name__ == "__main__":
    main()
