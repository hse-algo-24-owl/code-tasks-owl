def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
    validate(matrix)
    order = len(matrix)
    if order == 1:
        return matrix[0][0]
    elif order == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for idx, value in enumerate(matrix[0]):
        if value == 0:
            continue
        minor = [row[:idx] + row[idx + 1 :] for row in matrix[1:]]
        co_factor = (-1) ** idx
        det += value * co_factor * calculate_determinant(minor)

    return det


def validate(matrix: list[list[int]]) -> None:
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise Exception("Матрица пуста или не является списком")
    for row in matrix:
        if not isinstance(row, list) or len(row) != len(matrix):
            raise Exception("Матрица не является квадратной")
        for item in row:
            if not isinstance(item, int):
                raise Exception("Не все элементы матрицы являются целыми числами")


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
