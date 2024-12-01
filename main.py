from typing import Any
def validate(items: list[Any]) -> None:
    """Проверяет корректность входных данных."""
    if not isinstance(items, list):
        raise TypeError("Параметр items не является списком")
    if len(items) != len(set(items)): 
        raise ValueError("Список элементов содержит дубликаты")


def generate_permutations(items: list[Any]) -> list[list[Any]]:
    """Генерирует все варианты перестановок элементов указанного множества
    :param items: список элементов
    :raise TypeError: если параметр items не является списком
    :raise ValueError: если список элементов содержит дубликаты
    :return: список перестановок, где каждая перестановка список элементов
    множества
    """
    validate(items)
    n = len(items)
    if n == 0:
        return []
    if n == 1:
        return [items.copy()]

    permutations = [items.copy()]
    
    index_elem = list(range(n)) 

    while True:
        i = n - 2
        while i >= 0 and index_elem[i] >= index_elem[i + 1]:
            i -= 1
        if i < 0:
            break

        j = n - 1
        while index_elem[j] <= index_elem[i]:
            j -= 1
        
        index_elem[i], index_elem[j] = index_elem[j], index_elem[i]
        index_elem[i+1:] = index_elem[i+1:][::-1]

        new_permutation = [items[t] for t in index_elem]
        permutations.append(new_permutation)

    return permutations


def main():
    items = [1, 2, 3]
    print(generate_permutations(items))
    items = [True, False]
    print(generate_permutations(items))
    items = ['a','b', 'c']
    print(generate_permutations(items))

if __name__ == "__main__":
    main()
