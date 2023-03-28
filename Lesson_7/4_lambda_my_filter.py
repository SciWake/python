# Вернёмся к 1_function.py -> print_function_string 
# и перепишем её через lambda


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

# -------------------
# Переписали на Lambda
get_number_string_1 = lambda num: f"Твоё число {num}"
print(get_number_string_1(101231231231231))

# Или без сохранения
print((lambda num: f"Твоё число {num}")(101231231231231))


# Создадим функцию
def print_function_string(func: get_number_string) -> None:
    """Принимает функцию func и передаёт фиксированный аргумент внутрь func.

    Args:
        func (get_number_string): Некоторая функция.
    """
    print(func(123123123123123123123123))


# Теперь мы можем заменить большую get_number_string на lambda,
# так как выше её научилиьс писать
print_function_string(lambda num: f"Твоё число {num}")
