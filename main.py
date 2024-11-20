def rabbits(n: int, lifetime: int) -> int:
    p = [1] + [0] * (lifetime-1)
    for j in range(1, n):
        new=sum(p[1:])
        p[1:]=p[:-1]
        p[0]=new
        if len(p)>lifetime:
            p.pop()
    return sum(p)


def main():
    n = 35
    lifetime = 5
    print(f"\nВычисление числа пар кроликов по состоянию на {n} месяц")
    print(f"при продолжительности жизни кролика {lifetime} месяцев")
    print("количество пар кроликов составит:", rabbits(n, lifetime))


if __name__ == "__main__":
    main()
