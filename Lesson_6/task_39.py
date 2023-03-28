"""39. Даны два массива чисел. Требуется вывести те элементы 
первого массива (в том порядке, в каком они идут в первом массиве), 
которых нет во втором массиве. Пользователь вводит число N - 
количество элементов в первом массиве, затем N чисел - 
элементы массива. Затем число M - количество элементов 
во втором массиве. Затем элементы второго массива"""

first_numbers = [3, 1, 3, 4, 2, 4, 12]
second_numbers = [4, 15, 43, 1, 15, 1]

# Вариант 1.0
count = 0
for i in range(len(first_numbers)):
    for j in range(len(second_numbers)):
        if first_numbers[i] == second_numbers[j]:
            count += 1
    if count == 0:
        print(first_numbers[i])
    count = 0


# 3 3 2 12

print("-" * 20)
# Вариант 1.1
count = 0
for first_num in first_numbers:
    for second_num in second_numbers:
        if first_num == second_num:
            count += 1
    if count == 0:
        print(first_num)
    count = 0

# Вариант 2.0
print("-" * 20)
for i in range(len(first_numbers)):
    if first_numbers[i] not in second_numbers:
        print(first_numbers[i], end=' ')


# Вариант 2.1
print()
print("-" * 20)
for num in first_numbers:
    if num not in second_numbers:
        print(num, end=' ')

"""А можете ещё раз объяснить чем отличается проход по списку/массиву 
for i in list_1 от for i in range(len(list_1))? 
В каком случае какой способ лучше использовать?"""

first_numbers = [3, 1, 3, 4, 2, 4, 12]
for i in range(len(first_numbers)):
    if first_numbers[i] % 2 == 0:
       first_numbers[i] = 'Чет'
print(first_numbers)


first_numbers = [3, 1, 3, 4, 2, 4, 12]
i = 0
for num in first_numbers:
    if num % 2 == 0:
        first_numbers[i] = 'Чет'
    i += 1
print(first_numbers)


first_numbers = [3, 1, 3, 4, 2, 4, 12]
# i = 0
for i, num in enumerate(first_numbers):
    if num % 2 == 0:
        first_numbers[i] = 'Чет'
    # i += 1
print(first_numbers)
