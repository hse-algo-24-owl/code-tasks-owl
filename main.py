from typing import TypeVar

from heap.heap import Heap, HeapType

T = TypeVar("T")


def heap_sort(items: list[T]) -> list[T]:
    """Сортирует элементы списка.

    :param items: Список элементов для сортировки.
    :return: Список отсортированных элементов.
    """
    pass


def main():
    items = [5, 8, 1, 4, -7, 6, 12, 19, -6]
    print(heap_sort(items))


if __name__ == "__main__":
    main()
