def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.

    :return: значение определителя.
    """
    if matrix is None:
        raise Exception("Параметр не является трехдиагональной матрицей")
    
    n = len(matrix)

    # Проверка на пустую матрицу
    if n == 0:
        raise Exception("Параметр не является трехдиагональной матрицей")
    
    # Проверка на квадратность и корректность
    if any(len(row) != n for row in matrix):
        raise Exception("Параметр не является трехдиагональной матрицей")
    
    # Проверка на трехдиагональную структуру и наличие нулей
    for i in range(n):
        for j in range(n):
            if (j > i + 1 or j < i - 1) and matrix[i][j] != 0:
                raise Exception("Параметр не является трехдиагональной матрицей")
            if i == j and matrix[i][j] == 0:
                raise Exception("Параметр не является трехдиагональной матрицей")
            if (i == j - 1 or i == j + 1) and matrix[i][j] == 0:
                raise Exception("Параметр не является трехдиагональной матрицей")
            
    # Проверка, что элементы главной и побочных диагоналей одинаковые
    main_diag_value = matrix[0][0]
    for i in range(1, n):
        if matrix[i][i] != main_diag_value:
            raise Exception("Параметр не является трехдиагональной матрицей: элементы главной диагонали не одинаковые")

    upper_diag_value = matrix[0][1] if n > 1 else None
    for i in range(1, n - 1):
        if matrix[i][i + 1] != upper_diag_value:
            raise Exception("Параметр не является трехдиагональной матрицей: элементы верхней диагонали не одинаковые")

    lower_diag_value = matrix[1][0] if n > 1 else None
    for i in range(1, n - 1):
        if matrix[i + 1][i] != lower_diag_value:
            raise Exception("Параметр не является трехдиагональной матрицей: элементы нижней диагонали не одинаковые")

    if n == 1:
        return matrix[0][0]  # Определитель 1x1 матрицы
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]  # Определитель 2x2 матрицы

    # Инициализация массива для хранения определителей
    det_values = [0] * n
    det_values[0] = matrix[0][0]  
    det_values[1] = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]  

    # Вычисление определителя для n > 2
    for i in range(2, n):
        det_values[i] = (matrix[i][i] * det_values[i-1] - 
                matrix[i][i-1] * matrix[i-1][i] * det_values[i-2])

    return det_values[n-1]  # Определитель n x n матрицы


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
