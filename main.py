#from profilehooks import profile
from functools import lru_cache
import time

@lru_cache(maxsize=None)

def fibonacci_rec(n: int) -> int:
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)


def fibonacci_iter(n: int) -> int:
    if n <= 1:
        return n
    else:
        s = list([1, 1])
        for i in range(2, n):
            s.append(s[i-1] + s[i - 2])
        return s[-1]


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    a = b = res = 1
    for i in range(2, n):
        res = a+b
        a = b
        b = res
    return res


def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci(n))


if __name__ == "__main__":
    main()
