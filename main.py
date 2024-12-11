INF = float("inf")
COST = "cost"
PATH = "path"
PARAM_ERR_MSG = (
    "Таблица цен не является прямоугольной матрицей с " "числовыми значениями"
)

# Возвращение пути минимальной стоимости 
def get_min_cost_path(
    price_table: list[list[float | int | None]],
) -> dict[str : float | None, str : list[tuple[int, int]] | None]:
    """Возвращает путь минимальной стоимости в таблице из левого верхнего угла
    в правый нижний. Каждая ячейка в таблице имеет цену посещения. Некоторые
    ячейки запрещены к посещению, вместо цены посещения значение None.
    Перемещение из ячейки в ячейку можно производить только по горизонтали
    вправо или по вертикали вниз.
    :param price_table: Таблица с ценой посещения для каждой ячейки.
    :raise ValueError: Если таблица цен не является прямоугольной матрицей с
    числовыми значениями.
    :return: Словарь с ключами:
    cost - стоимость минимального пути или None если пути не существует,
    path - путь, список кортежей с индексами ячеек, или None если пути
    не существует.
    """
    validate_price_table(price_table)

    cost_matrix, path_matrix = initialize_cost_and_path_matrices(price_table)
    fill_cost_and_path_matrices(price_table, cost_matrix, path_matrix)

    min_cost = cost_matrix[-1][-1]
    if min_cost == INF:
        return {COST: None, PATH: None}

    path = recover_path(path_matrix, len(price_table) - 1, len(price_table[0]) - 1)
    return {COST: min_cost, PATH: path}

# Валидация входных данных
def validate_price_table(price_table: list[list[float | int | None]]) -> None: 
    if price_table is None or not isinstance(price_table, list) or len(price_table) == 0:
        raise ValueError(PARAM_ERR_MSG)

    num_rows = len(price_table)
    if num_rows == 0 or all(len(row) == 0 for row in price_table):
        raise ValueError(PARAM_ERR_MSG)

    num_cols = len(price_table[0]) if num_rows > 0 else 0
    for row in price_table:
        if not isinstance(row, list) or len(row) != num_cols or not all(isinstance(x, (int, float)) or x is None for x in row):
            raise ValueError(PARAM_ERR_MSG)

# Инициализация матриц стоимости и путей
def initialize_cost_and_path_matrices(price_table: list[list[float | int | None]]) -> tuple[list[list[float]], list[list[tuple[int, int]]]]: 
    num_rows, num_cols = len(price_table), len(price_table[0])
    cost_matrix = [[INF] * num_cols for i in range(num_rows)]
    path_matrix = [[None] * num_cols for i in range(num_rows)]

    if price_table[0][0] is not None:
        cost_matrix[0][0] = price_table[0][0]

    return cost_matrix, path_matrix

# Заполнение матриц стоимости и путей
def fill_cost_and_path_matrices(price_table: list[list[float | int | None]], cost_matrix: list[list[float]], path_matrix: list[list[tuple[int, int]]]) -> None:
    for row in range(len(price_table)):
        for col in range(len(price_table[row])):
            if price_table[row][col] is None:
                continue
            
            if row > 0 and cost_matrix[row-1][col] != INF:
                new_cost = cost_matrix[row-1][col] + price_table[row][col]
                if cost_matrix[row][col] > new_cost:
                    cost_matrix[row][col] = new_cost
                    path_matrix[row][col] = (row-1, col)

            if col > 0 and cost_matrix[row][col-1] != INF:
                new_cost = cost_matrix[row][col-1] + price_table[row][col]
                if cost_matrix[row][col] > new_cost:
                    cost_matrix[row][col] = new_cost
                    path_matrix[row][col] = (row, col-1)

# Восстановление пути
def recover_path(path_matrix: list[list[tuple[int, int]]], start_row: int, start_col: int) -> list[tuple[int, int]]:
    path = []
    current_position = (start_row, start_col)

    while current_position is not None:
        path.append(current_position)
        current_position = path_matrix[current_position[0]][current_position[1]]

    path.reverse()  # Установление правильного порядка
    return path

def main():
    table = [[1, 2, 2], [3, None, 2], [None, 1, 2]]
    print(get_min_cost_path(table))

if __name__ == "__main__":
    main()