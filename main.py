PATH_LENGTH_ERROR_MSG = "Длина маршрута должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина маршрута"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""


def get_triangle_path_count(length: int) -> int:
    """Вычисляет количество замкнутых маршрутов заданной длины между тремя
    вершинами треугольника A, B и C. Маршруты начинаются и оканчиваются в
    вершине A vertex. Допустимыми являются все пути между различными вершинами.
    :param length: Длина маршрута.
    :raise ValueError: Если длина маршрута не является целым положительным
    числом.
    :return: Количество маршрутов.
    """
    # Проверка входных значений 
    if not isinstance(length, int) or isinstance(length, bool): 
        raise ValueError(PATH_LENGTH_ERROR_MSG) 
    if length < 1: 
        raise ValueError(PATH_LENGTH_ERROR_MSG) 
 
    def a(n): 
        if n == 1: 
            return 0 
        else: 
            return b(n - 1) + c(n - 1) 
 
    def b(n): 
        if n == 1: 
            return 1 
        else: 
            return a(n - 1) + c(n - 1) 
 
    def c(n): 
        if n == 1: 
            return 1 
        else: 
            return a(n - 1) + b(n - 1) 
 
    return a(length)


def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """
    # Проверка входных значений 
    if not isinstance(n, int) or not isinstance(k, int): 
        raise ValueError(NOT_INT_VALUE_TEMPL.format("n" if not isinstance(n, int) else "k")) 
    if n < 0 or k < 0: 
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("n" if n < 0 else "k")) 
    if n < k: 
        raise ValueError(N_LESS_THAN_K_ERROR_MSG) 
     
    # Рекурсивная реализация 
    if use_rec: 
        if k == 0 or k == n: 
            return 1 
        return binomial_coefficient(n - 1, k - 1, use_rec=True) + binomial_coefficient(n - 1, k, use_rec=True) 
     
    # Итеративная реализация 
    mtx = [[0] * (k + 1) for i in range(n + 1)] 
    for i in range(n + 1): 
        mtx[i][0] = 1 
        for j in range(1, min(i, k) + 1): 
            mtx[i][j] = mtx[i - 1][j - 1] + mtx[i - 1][j] 
     
    return mtx[n][k]


def main():
    n = 10
    print(f"Количество маршрутов длиной {n} = {get_triangle_path_count(n)}")

    n = 30
    k = 20
    print(
        f"Биномиальный коэффициент (итеративно) при n, k ({n}, {k}) = ",
        binomial_coefficient(n, k),
    )
    print(
        f"Биномиальный коэффициент (рекурсивно) при n, k ({n}, {k}) = ",
        binomial_coefficient(n, k, use_rec=True),
    )


if __name__ == "__main__":
    main()
