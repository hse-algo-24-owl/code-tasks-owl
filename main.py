def validate_matrix(matrix):
  """Проверяет трехдиагональную матрицу и выкидывает исключения"""
  if matrix is None or not isinstance(matrix, list) or not matrix:
    raise Exception("Параметр не является трехдиагональной матрицей")
  n = len(matrix)
  if any(not isinstance(row, list) or len(row) != n for row in matrix):
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
    validate_matrix(matrix)
    n = len(matrix)
    
    a = matrix[0][0] 
    if n == 1:
        return a
    b = matrix[0][1] 
    c = matrix[1][0] 
    
    det_previous = a
    det_second = a * matrix[1][1] - b * c
    
    for i in range(2, n):
        det_next = a * det_second - b * c * det_previous
        det_previous = det_second
        det_second = det_next

    return det_second
  
def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
