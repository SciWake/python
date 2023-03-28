"""Функция zip() в Python создает итератор, который объединяет элементы 
из нескольких источников данных. Эта функция работает со списками, 
кортежами, множествами и словарями для создания списков или кортежей, 
включающих все эти данные."""

employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

zipped_values = zip(employee_names, employee_numbers)
zipped_list = list(zipped_values)

print(zipped_list)

# Вот пример использования zip() для итерации по массивам:
employee_numbers = [2, 9, 18, 28, 200]
employee_names = ["Дима", "Марина", "Андрей", "Никита", 'Саша']

for name, number in zip(employee_names, employee_numbers):
    print(name, number)

# Но как восстановить их прежнюю форму?
employees_zipped = [('Дима', 2), ('Марина', 9), ('Андрей', 18), ('Никита', 28)]
employee_names, employee_numbers = zip(*employees_zipped)
print(list(zip(*employees_zipped)))

print(employee_names)
print(employee_numbers)
