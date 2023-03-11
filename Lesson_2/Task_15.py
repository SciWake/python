"""15. Иван Васильевич пришел на рынок и решил 
купить два арбуза: один для себя, а другой для тещи. 
Понятно, что для себя нужно выбрать арбуз 
потяжелей, а для тещи полегче. Но вот незадача: 
арбузов слишком много и он не знает как же выбрать 
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
"""

N = int(input('Ко-во арбузов: '))
min = float('inf')
max = float('-inf')

for _ in range(N):
    x = int(input('Вес арбуза: '))
    if x > max:
        max = x
    elif x < min:
        min = x

print(f'Т - {min}, И - {max}')
