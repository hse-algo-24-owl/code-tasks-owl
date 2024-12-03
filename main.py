import sys

sys.setrecursionlimit(1000000)

STR_LENGTH_ERROR_MSG = "Длина строки должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина строки"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""


def add_one(current: str, length: int, result: list[str]):
    """
    Рекурсивно добавляет символ '1' к текущей строке, обеспечивая, что никакие 
    два нуля не будут стоять рядом. Если длина строки достигает заданной, 
    добавляет строку в результат.

    :param current: Текущая строка, формируемая рекурсией
    :param length: Целевая длина строк
    :param result: Список для хранения строк, соответствующих условию
    """
    if len(current) == length:
        result.append(current)
        return
    add_one(current + '1', length, result)
    add_zero(current + '0', length, result)

def add_zero(current: str, length: int, result: list[str]):
    """
    Рекурсивно добавляет символ '0' к текущей строке, обеспечивая, что никакие 
    два нуля не будут стоять рядом. Если длина строки достигает заданной, 
    добавляет строку в результат

    :param current: Текущая строка, формируемая рекурсией
    :param length: Целевая длина строк
    :param result: Список для хранения строк, соответствующих условию.
    """
    if len(current) == length:
        result.append(current)
        return
    add_one(current + '1', length, result)

def generate_strings(length: int) -> list[str]:
    """Возвращает строки заданной длины, состоящие из 0 и 1, где никакие
    два нуля не стоят рядом.

    :param length: Длина строки.
    :raise ValueError: Если длина строки не является целым положительным
    числом.
    :return: Список строк.
    """

    if type(length) is not int or length <= 0:
        raise ValueError(STR_LENGTH_ERROR_MSG)

    result = []
    add_one('', length, result)
    return result


def binomial_coefficient_rec(n: int, k: int) -> int:
    """
    Вычисляет биномиальный коэффициент C(n, k) рекурсивно на основе формулы:
    C(n, k) = C(n-1, k-1) + C(n-1, k)

    :param n: Общее количество элементов для выбора (неотрицательное целое число)
    :param k: Количество выбираемых элементов (неотрицательное целое число)
    :return: Биномиальный коэффициент C(n,k) в виде целого числа
    """
    
    if k == 0 or k == n:
        return 1
    
    return binomial_coefficient_rec(n - 1, k - 1) + binomial_coefficient_rec(n - 1, k)

def binomial_coefficient_iter(n: int, k: int) -> int:
    """
    Итеративно вычисляет биномиальный коэффициент C(n,k) с использованием динамического программирования

    :param n: Общее количество элементов для выбора (неотрицательное целое число)
    :param k: Количество выбираемых элементов (неотрицательное целое число)
    :return: Биномиальный коэффициент C(n,k) в виде целого числа
    """

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1 
    for j in range(1, k + 1):
        dp[j][j] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

    return dp[n][k]

def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """

    if not isinstance(n, int):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("n"))
    
    if n < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("n"))

    if not isinstance(k, int):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("k"))
    
    if k < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("k"))
    
    if k > n:
        raise ValueError(N_LESS_THAN_K_ERROR_MSG)
    

    if use_rec:
        return binomial_coefficient_rec(n, k)
    
    return binomial_coefficient_iter(n, k)

    


def main():
    n = 3
    print(f"Строки длиной {n}:\n{generate_strings(n)}")

    n = 15
    k = 10
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
