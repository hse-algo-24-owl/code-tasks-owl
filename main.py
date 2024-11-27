def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
     # Проверяем, что матрица квадратная
    if len(matrix) != len(matrix[0]):
        raise Exception("Матрица должна быть квадратной")
    
    # Проверка, что все элементы матрицы целые числа
    for row in matrix:
        if not all(isinstance(x, int) for x in row):
            raise Exception("Матрица должна содержать только целые числа")

    # Базовый случай: если матрица 1x1, возвращаем единственный элемент
    if len(matrix) == 1:
        return matrix[0][0]

    # Базовый случай: если матрица 2x2, возвращаем определитель по формуле
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    # Рекурсивное разложение по первой строке
    for col in range(len(matrix)):
        # Создаем подматрицу, удаляя первую строку и текущий столбец
        submatrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        # Алгебраическое дополнение и рекурсивный вызов
        det += (-1) ** col * matrix[0][col] * calculate_determinant(submatrix)

    return det

    det = 0
    # Рекурсивное разложение по первой строке
    for col in range(len(matrix)):
        # Создаем подматрицу, удаляя первую строку и текущий столбец
        submatrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        # Алгебраическое дополнение и рекурсивный вызов
        det += (-1) ** col * matrix[0][col] * calculate_determinant(submatrix)

    return det

def is_square_matrix_with_integers(matrix):
    if not matrix:  
        # Проверяем, что матрица не пустая
        raise Exception("Матрица пуста.")
    num_rows = len(matrix)
    for row in matrix:
        if len(row) != num_rows:  
            # Проверяем, что матрица квадратная
            raise Exception("Матрица не является квадратной.")
        if not all(isinstance(x, int) for x in row):  
            # Проверяем, что все элементы целые
            raise Exception("Матрица содержит нецелочисленные элементы.")
    return True

def main():
    matrix = [[1, 2], [3, 4]]
   
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
