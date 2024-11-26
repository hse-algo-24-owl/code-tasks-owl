def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.

    :return: значение определителя.
    """
    check(matrix)
    n = len(matrix)
    a = matrix[0][0]
    if n == 1:
        return a
    b = matrix[0][1]
    c = matrix[1][0]
    det1 = a
    det2 = a**2 - b*c
    if n == 2:
        return det2
    det_n = 0
    for _ in range(2, n):
        det_n = a*det2 - b*c*det1
        det1 = det2
        det2 = det_n
    return det_n


def check(matrix):
    """Тест 1 и 2"""
    """Проверяет, является ли матрица трехдиагональной."""
    if not matrix:
        raise Exception("Параметр не является трехдиагональной матрицей")
    """Тест 3 и 4"""
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise Exception("Параметр не является трехдиагональной матрицей")
    """Тест 5"""
    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1 and matrix[i][j] != 0:
                raise Exception("Параметр не является трехдиагональной матрицей")
    """Тест 6"""
    main_elem = matrix[0][0]
    for i in range(1, n):
        j = i
        if matrix[i][j] != main_elem:
            raise Exception("Параметр не является трехдиагональной матрицей")
    """Тест 7"""
    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1 and matrix[i][j] != 0:
                raise Exception("Параметр не является трехдиагональной матрицей")
    """Тест 8"""
    for i in range(1,n):
        for j in range(1,n):
            if matrix[i-1][j-1] != matrix[i][j]:
                raise Exception("Параметр не является трехдиагональной матрицей")

def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
