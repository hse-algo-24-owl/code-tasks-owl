from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
    формуле вычисления последовательности.
    """
    if (n == 1) or (n == 2):
        return 1
    else:
      return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
    pass


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.
    """
    if (n <= 0):
        return 0
    elif (n == 1 or n == 2):
        return 1

    fib = [0] * n
    fib[0] = 1
    fib[1] = 1

    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n - 1]
    pass


def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if (n <= 0):
        return 0
    elif (n == 1 or n == 2):
        return 1
    fibMinus2 = 1
    fibMinus1 = 1
    fibN = 0
    
    for i in range (2, n):
        fibN = fibMinus2 + fibMinus1
        fibMinus2 = fibMinus1
        fibMinus1 = fibN
    return fibN
    pass


def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci_iter(n))


if __name__ == "__main__":
    main()
