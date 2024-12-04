STR_LENGTH_ERROR_MSG = "Длина строки должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина строки"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""

#Валидация параметра длины для генерации строк
def validate_strings(length: int):
    if not type(length) == int:                                                 
        raise ValueError(STR_LENGTH_ERROR_MSG)                      #Проверка на тип строки и длину строки меньше 1
    if length < 1:
        raise ValueError(STR_LENGTH_ERROR_MSG)

def strings_ending_with_one(n):                                                                                     #Генерация строк заканчивающихся на 1
    if n == 1:
        return ["1"]                                                                                                #Если длина равна 1 - возвращаем 1                                                       
    return [s + "1" for s in strings_ending_with_one(n - 1)] + [s + "1" for s in strings_ending_with_zero(n - 1)]   #Рекурсивно генерим все строки длиной n-1 и добавляем к каждой 1

def strings_ending_with_zero(n):                                    #Генерация строк заканчивающихся на 0
    if n == 1:
        return ["0"]                                                #Если длина равна 1 - возвращаем 0
    return [s + "0" for s in strings_ending_with_one(n - 1)]        #Генерим строки, заканчивающиеся на 1 для длины n-1 и на 0, для заданной длины

#Основная функция
def generate_strings(length: int) -> list[str]:
    validate_strings(length)                                                    #Валидируем входящий параметр
    return strings_ending_with_one(length) + strings_ending_with_zero(length)   

#Валидация параметров для вычисления биномиального коэффициента
def validate_coef(n: int, k: int):
    if not isinstance(n, int):                                      #Проверка на целое число
        raise ValueError(NOT_INT_VALUE_TEMPL.format("n")) 
    if not isinstance(k, int):                                      #Проверка на целое число
        raise ValueError(NOT_INT_VALUE_TEMPL.format("k")) 
    if n < 0:                                                       #Проверка на отрицательные значения
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("n"))
    if k < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("k"))   
    if n < k:                                                       #Проверка на n < k
        raise ValueError(N_LESS_THAN_K_ERROR_MSG) 

#Основная функция
def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    validate_coef(n, k)                                             #Валидируем входящие параметры
    if use_rec:                                                     #Если истинно, то используется рекурсия
        if k == 0 or n == k:
            return 1
        return binomial_coefficient(n - 1, k - 1, use_rec=True) + binomial_coefficient(n - 1, k, use_rec=True)  #Рекурсивное вычисление суммы двух предыдущих значений биномиальных коэффициентов
    else:                                                           #Итерация
        C = [0] * (k + 1)                                           #Создание списка для хранения
        C[0] = 1                                                    #Инициализация первого элемента
        for i in range(1, n + 1):
            j = min(i, k)                                           #Ограничение j значением k
            while j > 0:
                C[j] = C[j] + C[j - 1]                              #Обновление элементов списка
                j -= 1
        return C[k]           
    
def main():
    n = 10
    print(f"Строки длиной {n}:\n{generate_strings(n)}")

    n = 30
    k = 20
    print(
        f"Биномиальный коэффициент (итеративно) при n, k ({n}, {k}) = ",
        binomial_coefficient(n, k),
    )
    print(
        f"Биномиальный коэффициент (рекурсивно) при n, k ({n}, {k}) = ",
        binomial_coefficient(n, k, use_rec=True),
    )

if __name__ == "__main__":
    main()
