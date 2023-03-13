"""17. Дан список чисел. Определите,
сколько в нем встречается различных чисел."""

numbers = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]

# Вариант 1
result = []
for num in numbers:
    if num not in result:
        result.append(num)
print(len(result))

# Вариант 2
result = []
for num in numbers:
    if result.count(num) == 0:
        result.append(num)
print(len(result))

# Вариант 3 - Изменяем исходный список
for num in numbers.copy():
    while numbers.count(num) != 1:
        numbers.remove(num)
print(len(numbers))


# Вариант 4 - так как исходный список поменял, создадим его ещё раз
numbers = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
print(len(set(numbers)))
