import unittest

from heap import ERR_INCORRECT_HEAP_TYPE, Heap, HeapType


class TestHeap(unittest.TestCase):
    def setUp(self):
        """Инициализация минимальной и максимальной кучи перед каждым тестом."""
        self.min_heap = Heap(heap_type=HeapType.MIN)
        self.max_heap = Heap(heap_type=HeapType.MAX)

    def test_incomparable_embedded_types(self):
        """Проверяет выброс исключения при некорректной инициализации."""
        with self.assertRaises(TypeError) as err:
            Heap("not a HeapType")
        self.assertEqual(ERR_INCORRECT_HEAP_TYPE, str(err.exception))

    def test_push_and_top(self):
        """Проверяет корректность добавления элементов и извлечения верхнего элемента."""
        self.min_heap.push(3)
        self.min_heap.push(1)
        self.min_heap.push(2)
        self.assertEqual(self.min_heap.top(), 1)

        self.max_heap.push(3)
        self.max_heap.push(1)
        self.max_heap.push(2)
        self.assertEqual(self.max_heap.top(), 3)

    def test_pop(self):
        """Проверяет корректность удаления и возврата верхнего элемента."""
        self.min_heap.push(3)
        self.min_heap.push(1)
        self.min_heap.push(2)
        self.assertEqual(self.min_heap.pop(), 1)
        self.assertEqual(self.min_heap.pop(), 2)
        self.assertEqual(self.min_heap.pop(), 3)
        with self.assertRaises(IndexError):
            self.min_heap.pop()

        self.max_heap.push(3)
        self.max_heap.push(1)
        self.max_heap.push(2)
        self.assertEqual(self.max_heap.pop(), 3)
        self.assertEqual(self.max_heap.pop(), 2)
        self.assertEqual(self.max_heap.pop(), 1)
        with self.assertRaises(IndexError):
            self.max_heap.pop()

    def test_top_on_empty_heap(self):
        """Проверяет поведение метода top при обращении к пустой куче."""
        with self.assertRaises(IndexError):
            self.min_heap.top()
        with self.assertRaises(IndexError):
            self.max_heap.top()

    def test_len(self):
        """Проверяет корректность работы метода len."""
        self.assertEqual(len(self.min_heap), 0)
        self.min_heap.push(1)
        self.assertEqual(len(self.min_heap), 1)
        self.min_heap.push(2)
        self.assertEqual(len(self.min_heap), 2)
        self.min_heap.pop()
        self.assertEqual(len(self.min_heap), 1)

        self.assertEqual(len(self.max_heap), 0)
        self.max_heap.push(1)
        self.assertEqual(len(self.max_heap), 1)
        self.max_heap.push(2)
        self.assertEqual(len(self.max_heap), 2)
        self.max_heap.pop()
        self.assertEqual(len(self.max_heap), 1)

    def test_order(self):
        """Проверяет упорядочивание элементов при pop."""
        elements = [5, 1, 3, 4, 2]
        for elem in elements:
            self.min_heap.push(elem)
            self.max_heap.push(elem)

        self.assertEqual(
            [self.min_heap.pop() for _ in range(len(elements))], [1, 2, 3, 4, 5]
        )
        self.assertEqual(
            [self.max_heap.pop() for _ in range(len(elements))], [5, 4, 3, 2, 1]
        )

    def test_push_pop_interleaved(self):
        """Проверяет корректность поведения при смешанных операциях push и pop."""
        self.min_heap.push(10)
        self.min_heap.push(5)
        self.assertEqual(self.min_heap.pop(), 5)
        self.min_heap.push(1)
        self.assertEqual(self.min_heap.pop(), 1)
        self.assertEqual(self.min_heap.pop(), 10)
        with self.assertRaises(IndexError):
            self.min_heap.pop()

        self.max_heap.push(10)
        self.max_heap.push(20)
        self.assertEqual(self.max_heap.pop(), 20)
        self.max_heap.push(30)
        self.assertEqual(self.max_heap.pop(), 30)
        self.assertEqual(self.max_heap.pop(), 10)
        with self.assertRaises(IndexError):
            self.max_heap.pop()


if __name__ == "__main__":
    unittest.main()
