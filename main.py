from profilehooks import profile

def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализовано рекурсивно согласно формуле вычисления последовательности.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)



def fibonacci_iter(n:int) -> int:     
    """Возвращает N-E число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.
    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n == 0 or n == 1:
        return n

    fib = [0]*(n+1)
    fib[1] = 1

    for i in range(2,n+1):
        fib[i] = fib[i-1]+fib[i-2]
    
    return fib[n]


def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n == 0 or n == 1:
        return n
    else:
        fn_1 = 1
        fn_2 = 0
        fib = 0
        for i in range(n - 1):
            fib = fn_1 + fn_2
            fn_2 = fn_1
            fn_1 = fib
        return fib

@profile
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
