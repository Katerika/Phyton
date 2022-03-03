import string as st

x, y = [i for i in input('Введите две буквы: ').split(' ')]

a = st.ascii_lowercase
x_numb = a.index(x) + 1
y_numb = a.index(y) + 1
dist = abs(y_numb - x_numb) - 1

print(f'Позици первой буквы: {x_numb}')
print(f'Позиция второй буквы: {y_numb}')
print(f'Количество букв между позицией {x_numb} и {y_numb}: {dist}')