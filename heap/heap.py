from enum import Enum

ERR_INCOMPARABLE_EMBEDDED_TYPES = "Переданы несравнимые экземпляры классов '{}' и '{}'"
ERR_INCORRECT_HEAP_TYPE = "Тип кучи не является экземпляром класса HeapType"


class HeapType(Enum):
    MIN = "min"
    MAX = "max"


class Heap:
    """
    Универсальная структура данных "Куча".

    Куча представляет собой частично упорядоченную структуру данных, которая
    позволяет эффективно получать минимальный или максимальный элемент (в зависимости от типа).
    Эта реализация поддерживает минимальную и максимальную кучу, определяемую через параметр `HeapType`.

    Основные операции:
    - `push(item)`: добавляет элемент в кучу.
    - `pop()`: удаляет и возвращает минимальный/максимальный элемент.
    - `top()`: возвращает минимальный/максимальный элемент без удаления.

    Параметры:
    - `heap_type` (`HeapType`): определяет тип кучи (минимальная или максимальная).
    """

    pass


if __name__ == "__main__":
    print("Пример: минимальная куча")
    min_heap = Heap(heap_type=HeapType.MIN)
    min_heap.push(3)
    min_heap.push(1)
    min_heap.push(6)
    min_heap.push(5)
    min_heap.push(2)
    min_heap.push(4)

    print("Куча:", min_heap)
    print("Минимальный элемент:", min_heap.pop())
    print("Куча после удаления минимального элемента:", min_heap)

    print("\nПример: максимальная куча")
    max_heap = Heap(heap_type=HeapType.MAX)
    max_heap.push(3)
    max_heap.push(1)
    max_heap.push(6)
    max_heap.push(5)
    max_heap.push(2)
    max_heap.push(4)

    print("Куча:", max_heap)
    print("Максимальный элемент:", max_heap.pop())
    print("Куча после удаления максимального элемента:", max_heap)
