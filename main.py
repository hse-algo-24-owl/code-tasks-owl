import random

import numpy as np

MATRIX = "matrix"
DET = "determinant"


def get_random_matrix_and_det(order):
    """Генерирует случайную квадратную целочисленную матрицу с заранее
    известным значением определителя.

    :param order: порядок матрицы
    :raise Exception: если порядок матрицы не является целым числом и порядок
    меньше 1
    :return: словарь с ключами matrix, det
    """
    pass


def main():
    n = 10
    print(f"Генерация матрицы порядка {n}")
    result = get_random_matrix_and_det(n)
    print("\nОпределитель сгенерированной матрицы равен", result[DET])
    print("\n".join(["\t".join([str(cell) for cell in row]) for row in result[MATRIX]]))
    print(
        "\nОпределитель, рассчитанный numpy, равен",
        round(np.linalg.det(np.array(result[MATRIX]))),
    )


if __name__ == "__main__":
    main()
