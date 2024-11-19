def rabbits(target_month: int, rabbit_lifetime: int) -> int:
    """Возвращает количество пар кроликов в популяции на заданный месяц.
    В начальный момент времени имеется одна пара кроликов. Начиная со второго
    месяца после рождения пара кроликов производит новую пару каждый месяц.
    После достижения предельного возраста кролики умирают.

    :param target_month: месяц, на который нужно рассчитать количество пар кроликов.
    :param rabbit_lifetime: продолжительность жизни каждого кролика, не менее 2 месяцев.
    :return: количество пар кроликов
    """
    rabbits = [1, 1]
    counter = 0
    for i in range(2, target_month):
        if i >= rabbit_lifetime:
            rabbits.append(rabbits[i - counter - 1] + rabbits[i - counter - 2] - rabbits[i - counter - rabbit_lifetime])
            rabbits.pop(0)
            counter += 1
        else:
            rabbits.append(rabbits[i - counter - 1] + rabbits[i - counter - 2])
    
    return rabbits[-1]


def main():
    n = 35
    lifetime = 5
    print(f"\nВычисление числа пар кроликов по состоянию на {n} месяц")
    print(f"при продолжительности жизни кролика {lifetime} месяцев")
    print("количество пар кроликов составит:", rabbits(n, lifetime))


if __name__ == "__main__":
    main()
