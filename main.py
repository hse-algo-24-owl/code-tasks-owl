from typing import Any, Generator


class ErrorMessages:
    ERROR_ITEMS_NOT_IS_LIST = "Параметр items не является списком"
    ERROR_DUPLICATE_ITEMS = "Список элементов содержит дубликаты"


def generate_permutations(items: list[Any]) -> Generator[list[Any], None, None]:
    """
    Создает генератор перестановок элементов указанного множества в лексикографическом порядке.
    :param items: список элементов.
    :raise TypeError: если параметр items не является списком.
    :raise ValueError: если список элементов содержит дубликаты.
    :return: следующую перестановку элементов множества.
    """
    pass


def main():
    items = [3, 2, 1]
    for perm in generate_permutations(items):
        print(perm)


if __name__ == "__main__":
    main()
