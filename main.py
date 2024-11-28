def validate(matrix: list[list[int]]):
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise Exception("Матрица пустая")
    for row in matrix:
        if not isinstance(row, list) or len(row) ==0:
            raise Exception("Строка матрицы пустая")
        elif len(matrix) != len(row):
            raise Exception("Матрица не квадратная")
    for item in row:
        if not isinstance(item, int):
            raise Exception("Матрица содержит не целочисленные значения")
         
def calculate_determinant(matrix: list[list[int]]) -> int:
    validate(matrix)        
    if len(matrix) == 1:
        return matrix[0][0]

    det = 0
    for col_idx, value in enumerate(matrix[0]):
        if value == 0:
            continue
        reduced_matrix = [[item for item in row] for str_idx, row in enumerate(matrix) if str_idx != 0]
        reduced_matrix = [[item for j, item in enumerate(row) if j != col_idx] for row in reduced_matrix]
        co_factor =  (-1)**col_idx * calculate_determinant(reduced_matrix)
        det += value*co_factor
    return det

def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()


