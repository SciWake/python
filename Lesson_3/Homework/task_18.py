"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
к заданному числу X. Пользователь в первой строке вводит натуральное число N – 
количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5"""
    
    
# Вариант 1
n = int(input())
list_1 = list()
for i in range(n):
    x = int(input())
    list_1.append(x)

k = int(input())
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)


# Вариант 2
n = int(input("Введите количество элементов в массиве: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
x = int(input("Введите число, чтобы найти ближайшее число в массиве: "))

closest = arr[0]
dist = abs(arr[0] - x)

for i in range(1, n):
    if abs(arr[i] - x) < dist:
        closest = arr[i]
        dist = abs(arr[i] - x)

print("Ближайшим элементом массива к числу", x, "является", closest)
