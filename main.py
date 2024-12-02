STR_LENGTH_ERROR_MSG = "Длина строки должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина строки"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""


def generate_strings(length: int) -> list[str]:
    """Возвращает строки заданной длины, состоящие из 0 и 1, где никакие
    два нуля не стоят рядом.

    :param length: Длина строки.
    :raise ValueError: Если длина строки не является целым положительным
    числом.
    :return: Список строк.
    """
    if not isinstance(length, int) or length <= 0:
        raise ValueError(STR_LENGTH_ERROR_MSG)
    if length == 1:
        return ['1']

    strings = []
    curr_string = ""
    add_one_to_str(curr_string, strings, length)
    add_zero_to_str(curr_string, strings, length)
    return strings


def add_one_to_str(curr_str, strings, length):
    if len(curr_str) == length:
        if curr_str not in strings:
            strings.append(curr_str)
        return

    add_one_to_str(curr_str + '1', strings, length)
    add_zero_to_str(curr_str + '1', strings, length)


def add_zero_to_str(curr_str, strings, length):
    if len(curr_str) == length:
        if curr_str not in strings:
            strings.append(curr_str)
        return

    if not curr_str or curr_str[-1] != '0':
        add_one_to_str(curr_str + '0', strings, length)


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
        raise ValueError(NOT_INT_VALUE_TEMPL.format("n", n))
    if not isinstance(k, int):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("k", k))
    if n < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("n", n))
    if k < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("k", k))
    if n < k:
        raise ValueError(N_LESS_THAN_K_ERROR_MSG.format(n, k))
    
    if use_rec:
        if k == 0:
            return 1
        if k == n:
            return 1
        return binomial_coefficient(n - 1, k, use_rec=True) + binomial_coefficient(n - 1, k - 1, use_rec=True)
    else:
        result = 1
        for i in range(0, k):
            result = result * (n - i) // (i + 1)
        return result


def main():
    n = 5
    print(f"Строки длиной {n}:\n{generate_strings(n)}")

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
