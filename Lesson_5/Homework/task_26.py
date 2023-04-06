"""Задача 26:  Напишите программу, которая на вход принимает два числа 
A и B, и возводит число А в целую степень B с помощью рекурсии."""


def my_pow(a, b):
    if b == 0:
        return 1
    return my_pow(a, b - 1) * a


def my_pow(a, b):
    return 1 if b == 0 else my_pow(a, b - 1) * a

print(my_pow(10, 1))

print(pow(0, 0))
