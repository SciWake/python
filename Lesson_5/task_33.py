"""Хакер Василий получил доступ к классному журналу 
и хочет заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, но наоборот: 
все максимальные – на минимальные."""

# ---------------
# Вариант 1 - max and min
list_of_ratings = [2, 2, 4, 3, 2, 3, 3, 5, 5, 5, 5, 5]
max_number = max(list_of_ratings)
min_number = min(list_of_ratings)

for i in range(len(list_of_ratings)):
    if list_of_ratings[i] == max_number:
        list_of_ratings[i] = min_number
        
print(list_of_ratings)

      
# Реализацию выше, можно заменить на это
list_of_ratings = [2, 2, 4, 3, 2, 3, 3, 5, 5, 5, 5, 5]
max_number = max(list_of_ratings)
min_number = min(list_of_ratings)

for i, num in enumerate(list_of_ratings):  # enumerate - позволяет считать номер элемента
    if num == max_number:
        list_of_ratings[i] = min_number
        
print(list_of_ratings)


# ---------------
# Вариант 2 - Свой max, min + добавим в функцию
list_of_ratings = [2, 2, 4, 3, 2, 3, 3, 5, 5, 5, 5, 5]


def get_min_and_max(numbers):
    """Функция поиска минимального значения

    Args:
        numbers (list): Список оценок

    Returns:
        min_number: Минимальное значение в numbers
        max_number: Максимальное значение в numbers
    """
    min_number, max_number = float('inf'), float('-inf')
    for num in numbers:
        if num > max_number: 
            max_number = num  # Обновление максимумк
        elif num < min_number:
            min_number = num  # Обновление минимума
    return min_number, max_number

# Отдельный вызов функции
min_number, max_number = get_min_and_max(list_of_ratings)
print(f'Минимум - {min_number}, Максимум - {max_number}')


def replace_max_to_min(numbers):
    """Заменяет максимальные значения внутри списка, 
    на минимальные из этого же списка

    Args:
        numbers (list): Список оценок

    Returns:
        _type_: _description_
    """
    min_number, max_number = get_min_and_max(numbers)
    print(f'Минимум - {min_number}, Максимум - {max_number}')
    
    # enumerate - позволяет считать номер элемента
    for i, num in enumerate(numbers):  
        if num == max_number:
            numbers[i] = min_number  # Замена максимума на минимум
    return numbers   # Получаем результат

result = replace_max_to_min(list_of_ratings)
print(result)


