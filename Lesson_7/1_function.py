"""Вспоминаем функции."""


def get_number_string(num: int) -> str:
    """Функция возвращает строку с числом.

    Args:
        num (int): Число, которое необходимо вывести.

    Returns:
        str: Строка с числом.
    """
    return f"Твоё число {num}"


# Вывод результата
num_string = get_number_string(1)
print(num_string)

# Можно записать и так
print(get_number_string(11))

# -----------------------------
# Будет ли тут ошибка?
# num_string = get_number_string()

# А что будет внутри переменной? Будет ошибка?
what = get_number_string
print(what)
print(type(what))

print(what(11010))


# Создадим функцию
def print_function_string(func: get_number_string) -> None:
    """Принимает функцию func и передаёт фиксированный аргумент внутрь func.

    Args:
        func (get_number_string): Некоторая функция.
    """
    print(func(11010))


new_test = print_function_string(what)
print(new_test)  # Функция ничего не возвращет, так renurn нет.
