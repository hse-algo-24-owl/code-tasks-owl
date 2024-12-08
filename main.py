INF = float("inf")
COST = "cost"
PATH = "path"
PARAM_ERR_MSG = (
    "Таблица цен не является прямоугольной матрицей с " "числовыми значениями"
)


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
    # Проверка входных данных на корректность
    if price_table is None or not isinstance(price_table, list) or len(price_table) == 0:
        raise ValueError(PARAM_ERR_MSG)

    # Получение количества строк в таблице
    num_rows = len(price_table)
    if num_rows == 0 or all(len(row) == 0 for row in price_table):
        raise ValueError(PARAM_ERR_MSG)
    
    # Получение количества столбцов в таблице
    num_cols = len(price_table[0]) if num_rows > 0 else 0

    # Проверка на корректность каждой строки
    for row in price_table:
        if not isinstance(row, list):
            raise ValueError(PARAM_ERR_MSG)
        if len(row) != num_cols:
            raise ValueError(PARAM_ERR_MSG)
        if not all(isinstance(x, (int, float)) or x is None for x in row):
            raise ValueError(PARAM_ERR_MSG)

    # Обработка случая, когда таблица содержит только пустую строку или все значения None
    if num_rows == 1 and num_cols == 0:
        return {COST: None, PATH: None}

    # Инициализация матриц затрат и путей
    cost_matrix = [[INF] * num_cols for i in range(num_rows)]
    path_matrix = [[None] * num_cols for i in range(num_rows)]

    # Установление стоимости начала пути, если она есть
    if price_table[0][0] is not None:
        cost_matrix[0][0] = price_table[0][0]

    # Заполнение матриц стоимости и путей
    for row in range(num_rows):
        for col in range(num_cols):
            if price_table[row][col] is None:
                continue
            
            # Проверка ячейки сверху
            if row > 0 and cost_matrix[row-1][col] != INF:
                new_cost = cost_matrix[row-1][col] + price_table[row][col]
                if cost_matrix[row][col] > new_cost:
                    cost_matrix[row][col] = new_cost
                    path_matrix[row][col] = (row-1, col)

            # Проверка ячейки слева
            if col > 0 and cost_matrix[row][col-1] != INF:
                new_cost = cost_matrix[row][col-1] + price_table[row][col]
                if cost_matrix[row][col] > new_cost:
                    cost_matrix[row][col] = new_cost
                    path_matrix[row][col] = (row, col-1)

    # Получение результата
    min_cost = cost_matrix[num_rows - 1][num_cols - 1]
    if min_cost == INF:
        return {COST: None, PATH: None}

    # Восстановление пути
    path = []
    current_position = (num_rows - 1, num_cols - 1)

    while current_position is not None:
        path.append(current_position)
        current_position = path_matrix[current_position[0]][current_position[1]]

    path.reverse()  # Установление правильного порядка

    return {COST: min_cost, PATH: path}

def main():
    table = [[1, 2, 2], [3, None, 2], [None, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == "__main__":
    main()
