"""Использование встроенного map."""

numbers = [1, 2, 3, 4, 5, 4, 16, 2, 24]


# Напишем функцию обработки чисел
def preproc_numbers(x):
    if x > 2:
        return str(x)
    else:
        return float(x)


# Обработка этой фукнцией через map
print(list(map(preproc_numbers, numbers)))

# Используем lambda, так лучше
print(list(map(lambda x: str(x) if x > 2 else float(x), numbers)))
