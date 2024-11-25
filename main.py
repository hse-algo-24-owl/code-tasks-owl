def validate_matrix(matrix, n):
  """Проверяет трехдиагональную матрицу и выкидывает исключения"""
  if not matrix:
    raise Exception("Параметр не является трехдиагональной матрицей")
  if not all(len(row) == n for row in matrix):
    raise Exception("Параметр не является трехдиагональной матрицей")
  for i in range(n):
    for j in range(n):
        if abs(i - j) > 1 and matrix[i][j] != 0:
            raise Exception("Параметр не является трехдиагональной матрицей")
        if i == j and matrix[i][j] == 0:
            raise Exception("Параметр не является трехдиагональной матрицей") 
        if (i == j + 1 or j == i + 1) and matrix[i][j] == 0:
            raise Exception("Параметр не является трехдиагональной матрицей")
  if n > 1: 
    main_elem = matrix[0][0]
    for i in range(1, n):
         if matrix[i][i] != main_elem:
            raise Exception("Параметр не является трехдиагональной матрицей")
    elem_up = matrix[0][1]
    for i in range(1, n -1):
         if matrix[i][i + 1] != elem_up:
            raise Exception("Параметр не является трехдиагональной матрицей")
    elem_low = matrix[1][0]
    for i in range(1, n):
         if matrix[i][i-1] != elem_low:
            raise Exception("Параметр не является трехдиагональной матрицей")
        
def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.

    :return: значение определителя.
    """
    if matrix is None:
        raise Exception("Параметр не является трехдиагональной матрицей")
    n = len(matrix)
    validate_matrix(matrix, n)
    
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]    
    
    det = [0] * (n + 1)
    det[0] = 1
    det[1] = matrix[0][0]
    
    for i in range(2, n + 1):
        a = matrix[i - 1][i - 1] 
        b = matrix[i - 1][i - 2] 
        c = matrix[i - 2][i - 1] 
        det[i] = a * det[i - 1] - b * c * det[i - 2]

    return det[n]

def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
