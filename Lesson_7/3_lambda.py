"""Анонимные функции (lambda)."""


# Функция, которая возвращает квадрат числа
def square(number: int) -> int:
    return number ** 2


print(square(110))

# Использование Lambda функции
# lambda параметр: результат
square_l = lambda number: number ** 2
print(square_l(11))
# Или мы можем вызвать lambda без сохранения, вот так:
print((lambda number: number ** 2)(11))


# --------------------------
# Ещё пример
def return_true() -> bool:
    return True


# Эквивалент функции выше, только через lambda:
return_true_l = lambda: True
print(return_true_l())
# Или без сохранения
print((lambda: True)())
