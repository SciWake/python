#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Если таких чисел нет - выдать внятное диагностическое сообщение
from random import randint
n_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(n_set)
m_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(m_set)
s_set = sorted(n_set.intersection(m_set))
print(*s_set)