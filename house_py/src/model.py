from pyxll import xl_func, DataFrameFormatter
from sklearn import linear_model
from joblib import dump, load
import os
import pandas as pd


@xl_func
def print(a, b):
    """Возвращает строку двух чисел

    Args:
        a (float): Первое число
        b (float): Второе число

    Returns:
        str: Строка из двух чисел
    """
    return f"{a}, {b}"


@xl_func
def train_model(train_data, price):
    """Функция для обучения модели на данных

    Args:
        train_data (DataFrame): Набор столбцов для обучения модели
        price (DataFrame): Целевая переменная или же цена

    Returns:
        _type_: Путь, где была сохранена модель
    """
    reg = linear_model.LinearRegression()
    reg.fit(train_data, price)
    dump(reg, 'model.joblib')
    return os.getcwd()


df_formatter = DataFrameFormatter()


@xl_func("dataframe<index=False, columns=False>: dataframe<index=True>",
         auto_resize=True,
         formatter=df_formatter)
def predict(test_data):
    """Предсказание на обученных данных

    Args:
        test_data (DataFrame): Таблица на основании которой необходимо выдать прогноз

    Returns:
        DataFrame: Прогноз модели
    """
    reg = load('model.joblib')

    predicts = pd.DataFrame(reg.predict(test_data), columns=["predicts"])
    return predicts
