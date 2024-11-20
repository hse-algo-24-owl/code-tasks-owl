from memory_profiler import profile

def fibonacci_rec(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
    
def fibonacci_iter(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fibonacci(n: int) -> int:
    if n<=0:
        return 0
    elif n==1:
        return 1
    a, b = 0, 1
    for k in range (2, n+1):
        a, b = b, a + b
    return b

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
