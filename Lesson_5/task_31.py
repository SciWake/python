"""Последовательностью Фибоначчи называется последовательность 
чисел a0, a1, ..., an, ..., где 
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи"""

# -----------------
# Решение с использованием for
def fib_for(n):
    a, b = 0, 1
    for _ in range(n):  # _ - так как переменная не используется
        a, b = b, a + b  # Обмен значениями
    return a


print(fib_for(1))


# -----------------
# Решение рекурсии с проблемами
def f(n):  # Плохое имя
    if n == 0 or n == 1:  # А если передать 0?
        return 1 # Получаем 1, тогда нужно считать что последовательность начинается с 1
    return f(n - 1) + f(n - 2)


n = int(input())
print(f(n - 2))


# -----------------
# Решение через рекурсию без проблем, но 50 элемент найти не сможем)
def fib_recursion(n):
    if n <= 1:
        return n
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)

print(fib_recursion(1))


# -----------------
# Добавим кэширование - решает проблему повторных вызовов рекурсии
cahce = {}
def fib_rec_cache(n):
    if n not in cahce:
        cahce[n] = n if n <= 1 else fib_rec_cache(n - 1) + fib_rec_cache(n - 2)
    return cahce[n]


print(fib_rec_cache(1))
