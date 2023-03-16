"""25. Напишите программу, которая принимает на вход строку, 
и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n."""

stroka = 'a a a b c a a d c d d'
stroka = stroka.split()
result = {}
for i in stroka:
    if i in result:
        # print(f'{i}_{result[i]}', end=' ')
        pass
    else:
        # print(i, end=' ')
        pass
    result[i] = result.get(i, 0) + 1
