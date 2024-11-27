def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
    isInputCorrect(matrix)
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        determinant = 0
        for j in range (len(matrix[0])):
            minor_matrix = calculate_minor(matrix, j)
            determinant += matrix[0][j] * (-1)**( 0+1 + j+1) * calculate_determinant(minor_matrix)
        return determinant

def calculate_minor(matrix: list[list[int]], column) -> list[list[int]]:
    """Вычисляет минор матрицы
    :param matrix: исходная матрица
    :param column: Номер столбца, который нужно удалить
    :return: Минор матрицы
    """
    minor_matrix = [row[:column] + row[column+1:] for row in matrix[1:]]
    return minor_matrix

def isInputCorrect(matrix: list[list[int]]) -> None:
    """Проверяет что матрица квадратная и целочисленная
    :param matrix: исходная матрица
    :return: None
    """
    for i in range (len(matrix)):
        if len(matrix) != len(matrix[i]):
            raise Exception()
        for j in range (len(matrix[i])):
            if isinstance(matrix[i][j], int) == False:
                raise Exception()

def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
