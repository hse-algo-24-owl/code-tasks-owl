import random

import numpy as np

MATRIX = "matrix"
DET = "determinant"

def div(x):
    """
    Вычисляет и возвращает список всех делителей заданного целого числа.

    :param x: Целое число, для которого нужно найти делители.
    :type x: int
    :return: Список делителей числа x.
    :rtype: list
    """
    lst = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            lst.append(i)
            lst.append(x // i)
    return lst

def muliplier_search(current_mulplication, dividers, det, order, current_iteration):
    """
    Ищет подходящий множитель для построения матрицы с заданным определителем.

    Эта функция итеративно выбирает множитель из списка делителей, который удовлетворяет
    определенным условиям, основанным на текущем произведении, целевом определителе и порядке матрицы.

    :param current_mulplication: Текущее произведение ранее выбранных множителей.
    :type current_mulplication: int
    :param dividers: Список возможных делителей для выбора.
    :type dividers: list
    :param det: Целевое значение определителя.
    :type det: int
    :param order: Порядок (размер) строящейся матрицы.
    :type order: int
    :param current_iteration: Текущая итерация в процессе построения матрицы.
    :type current_iteration: int

    :return: Кортеж, содержащий выбранный множитель и обновленный список делителей.
    :rtype: tuple(int, list)
    """
    if current_mulplication != det:
            new_multiplier = random.choice(dividers)
    else:
        new_multiplier = 1

    while det / (current_mulplication * new_multiplier) != det // (current_mulplication * new_multiplier):
        new_multiplier = random.choice(dividers)

    while current_mulplication * new_multiplier > det:
        dividers.remove(new_multiplier)
        new_multiplier = random.choice(dividers)

    while current_iteration == order - 1 and current_mulplication * new_multiplier != det :
        dividers.remove(new_multiplier)
        new_multiplier = random.choice(dividers)

    return new_multiplier, dividers

def get_random_matrix_and_det(order, det):
    """Генерирует случайную квадратную целочисленную матрицу с заранее
    известным значением определителя.

    :param order: порядок матрицы
    :type order: int
    :raise Exception: если порядок матрицы не является целым числом и порядок
    меньше 1
    :return: словарь с ключами matrix, det
    :rtype: dict
    """

    if not isinstance(order, int):
        raise Exception("Порядок матрицы не является целым числом")

    if order < 1:
        raise Exception("Порядок матрицы не может быть меньше 1")

    matrix = [[0] * order for _ in range(order)]

    dividers = div(abs(det))
    current_mulplication = 1

    # Заполнение диагонали матрицы множителями
    for i in range(order):
        new_multiplier, dividers = muliplier_search(current_mulplication, dividers, abs(det), order, i)
        matrix[i][i] = new_multiplier
        current_mulplication *= new_multiplier

    # Случайное умножение на единицу (чтобы добавить случайности)
    for i in range(order):
        if i == order - 1:
            if current_mulplication != det:
                j = random.randint(0, order - 1)
                matrix[j][j] *= -1
                current_mulplication *= -1
            break

        if random.choice([-1, 1]) == -1:
            matrix[i][i] *= -1
            current_mulplication *= -1

    # Случайное заполнение правой части матрицы
    for i in range(order):
        for j in range(i + 1, order):
            matrix[i][j] = round(random.random() * det * random.choice([-1, 1]))

    # Массивы для работы со строками
    avaliable_row_indexes = [i for i in range(1, order)]
    pasted_row_indexes = [0]

    # Массивы для работы со столбцами
    avaliable_column_indexes = [i for i in range(0, order - 1)]
    pasted_column_indexes = [order - 1]

    # Заполнение матрицы путём сложения столбцов и строк. ()
    while avaliable_row_indexes or avaliable_column_indexes:

        # Случайно выбирается что сложить друг с другом – столбцы или строки
        add_row = random.choice([True, False])

        if add_row and avaliable_row_indexes:                       # Сложение строк
            row_to_add = random.choice(pasted_row_indexes)          # Уже заполненная строка
            row_index = random.choice(avaliable_row_indexes)        # Ещё не заполненная строка
            pasted_row_indexes.append(row_index)

            operation = random.choice([True, False])
            if operation:
                temp_row_array = [i + j for i, j in zip(matrix[row_index], matrix[row_to_add])]
            else:
                temp_row_array = [i - j for i, j in zip(matrix[row_index], matrix[row_to_add])]
            i += 1
            for g in range(order):
                matrix[row_index][g] = temp_row_array[g]
            avaliable_row_indexes.remove(row_index)

        elif avaliable_column_indexes:                               # Сложение столбцов
            column_to_add = random.choice(pasted_column_indexes)     # Уже заполненный столбец
            column_index = random.choice(avaliable_column_indexes)   # Ещё заполненный столбе
            pasted_column_indexes.append(column_index)

            operation = random.choice([True, False])
            if operation:
                temp_column_array = [i + j for i, j in zip([matrix[g][column_index] for g in range(order)], [matrix[k][column_to_add] for k in range(order)])]
            else:
                temp_column_array = [i - j for i, j in zip([matrix[g][column_index] for g in range(order)], [matrix[k][column_to_add] for k in range(order)])]

            for index, element in enumerate(temp_column_array):

                matrix[index][column_index] = element
            avaliable_column_indexes.remove(column_index)

    return {MATRIX: matrix, DET: det}
 


def main():
    
    n, det = 10, 50

    print(f"Генерация матрицы порядка {n}")
    result = get_random_matrix_and_det(n, det)
    print("\nОпределитель сгенерированной матрицы равен", result[DET])
    print("\n".join(["\t".join([str(cell) for cell in row]) for row in result[MATRIX]]))
    print(
        "\nОпределитель, рассчитанный numpy, равен",
        round(np.linalg.det(np.array(result[MATRIX]))),
    )


if __name__ == "__main__":
    main()

