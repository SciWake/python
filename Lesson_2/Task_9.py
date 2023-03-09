"""9. По данному целому неотрицательному n вычислите значение n!.
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
Решить задачу используя цикл while"""
# from time import sleep

# ВАРИАНТ 1
# n = int(input("n = "))
# i = 1
# sum = 1

# while i <= n:
#     sum *= i
#     i += 1

# print(f'{n}! = {sum}')


# ВАРИАНТ 2
n = int(input("n = "))
i = 1
while n > 1:
    i *= n
    n -= 1
print(i)