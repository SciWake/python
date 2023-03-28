"""Фильтрация данных через функции."""


def my_filter(numbers: list) -> list:
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


numbers = [1, 2, 3, 4, 5, 4, 16, 2, 24]
print(my_filter(numbers))


# А что если мы хотим выбрать другие числа?
# Например, все числа больше 10?
# Давайте будем передовать вторым параметром функцию.


def my_filter(numbers: list, function) -> int:
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result


# ФИЛТР 1
# Создадим фильтр для проверки на чётность
# def is_even(number: int) -> bool:
#     if number % 2 == 0:
#         return True
#     return False

def is_even(number: int) -> bool:
    return number % 2 == 0


numbers = [1, 2, 3, 4, 5, 4, 16, 2, 24]
print(my_filter(numbers, is_even))


# ФИЛТР 2
# Создадим фильтр для проверки чисел больше 10
def more_than_10(number: str) -> int:
    if numbers >= 10:
        return True
    elif numbers <= 10:
        False


# Упростим функцию выше
def more_than_10(number: int) -> bool:
    return number >= 10


# Посставим этот фильтр внуть функции фильтрации
print(my_filter(numbers, more_than_10))

# Напишем фильтр через lambda и подставим внуть функции фильтрации
print(my_filter(numbers, lambda number: number >= 10))
