INF = float("inf")
COST = "cost"
PATH = "path"
PARAM_ERR_MSG = (
    "Таблица цен не является прямоугольной матрицей с " "числовыми значениями"
)

"""Возвращает путь минимальной стоимости в таблице из левого верхнего угла
в правый нижний. Каждая ячейка в таблице имеет цену посещения. Перемещение
из ячейки в ячейку можно производить только по горизонтали вправо или по
вертикали вниз.
:param price_table: Таблица с ценой посещения для каждой ячейки.
:raise ValueError: Если таблица цен не является прямоугольной матрицей с
числовыми значениями.
:return: Словарь с ключами:
cost - стоимость минимального пути,
path - путь, список кортежей с индексами ячеек.
"""




def get_min_cost_path(price_table: list[list[float | int]]) -> dict[str, float | list[tuple[int, int]]]:
    if not price_table or not all(len(row) == len(price_table[0]) for row in price_table):
        raise ValueError(PARAM_ERR_MSG)
    if any(not row for row in price_table):
        raise ValueError(PARAM_ERR_MSG)
    if any(not isinstance(item, (int, float)) for row in price_table for item in row):
        raise ValueError(PARAM_ERR_MSG)


    rows, cols = len(price_table), len(price_table[0])
    cost = [[float('inf')] * cols for _ in range(rows)]
    path = [[None] * cols for _ in range(rows)]


    cost[0][0] = price_table[0][0]
    path[0][0] = (None, None)
    for i in range(1, rows):
        cost[i][0] = cost[i-1][0] + price_table[i][0]
        path[i][0] = (i-1, 0)
    for j in range(1, cols):
        cost[0][j] = cost[0][j-1] + price_table[0][j]
        path[0][j] = (0, j-1)

    for i in range(1, rows):
        for j in range(1, cols):
            if cost[i-1][j] < cost[i][j-1]:
                cost[i][j] = cost[i-1][j] + price_table[i][j]
                path[i][j] = (i-1, j)
            else:
                cost[i][j] = cost[i][j-1] + price_table[i][j]
                path[i][j] = (i, j-1)

    min_path = []
    x, y = rows - 1, cols - 1
    while x is not None and y is not None:
        min_path.append((x, y))
        x, y = path[x][y] if path[x][y] else (None, None)

    min_path.reverse()


    return {COST: cost[-1][-1], PATH: min_path}
    pass


def main():
    table = [[1, 2, 2], [3, 4, 2], [1, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == "__main__":
    main()
