"""Использованиие sorted."""

# Набор чисел
numbers = [4, 1, 5, 1, 2, 3, 9, 7]

# Сортируем по возрастанию
print(sorted(numbers))

# Сортируем по убыванию
print(sorted(numbers, reverse=True))

# -------------------------
# Набор строк
names = ["Дмитрий", "Алексей", "Елена", "Антон", "Андрей"]
print(sorted(names))

# -------------------------
# Имя и возраст
names = [("Дмитрий", 28), ("Алексей", 21), ("Елена", 17), ("Антон", 24), ("Андрей", 23)]
print(sorted(names))


# Сортировка по возрасту
def key_age(user):
    return user[1]


print(sorted(names, key=key_age, reverse=True))

# Или через Lambda можно записать
lambda user: user[1]

# Используем Lambda
print(sorted(names, key=lambda x: x[1], reverse=True))
