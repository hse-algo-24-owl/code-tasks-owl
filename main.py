from typing import Any


def generate_permutations(items: list[Any]) -> list[list[Any]]:
    """Генерирует все варианты перестановок элементов указанного множества
    :param items: список элементов
    :raise TypeError: если параметр items не является списком
    :raise ValueError: если список элементов содержит дубликаты
    :return: список перестановок, где каждая перестановка список элементов
    множества
    """
    pass


def main():
    items = [1, 2, 3]
    print(generate_permutations(items))


if __name__ == "__main__":
    main()
