import sys

# #1 Урок 1 задание 5
import string as st

#x, y = [i for i in input('Введите две буквы: ').split(' ')]
x, y = 'd', 'g'

a = st.ascii_lowercase
x_numb = a.index(x) + 1
y_numb = a.index(y) + 1
dist = abs(y_numb - x_numb) - 1

#print(f'Позици первой буквы: {x_numb}')
#print(f'Позиция второй буквы: {y_numb}')
#print(f'Количество букв между позицией {x_numb} и {y_numb}: {dist}')

#print(f'Под переменную x было выделено памяти: {sys.getsizeof(x)}')
#print(f'Под переменную y было выделено памяти: {sys.getsizeof(y)}')
#print(f'Под переменную a было выделено памяти: {sys.getsizeof(a)}')
#print(f'Под переменную x_numb было выделено памяти: {sys.getsizeof(x_numb)}')
#print(f'Под переменную y_numb было выделено памяти: {sys.getsizeof(y_numb)}')
#print(f'Под переменную dist было выделено памяти: {sys.getsizeof(dist)}')
#print(f'Суммарное количество выделенной памяти: {sys.getsizeof(x) + sys.getsizeof(y)+sys.getsizeof(a)+sys.getsizeof(x_numb)+sys.getsizeof(y_numb)+sys.getsizeof(dist)}')

#Под переменную x было выделено памяти: 50
#Под переменную y было выделено памяти: 50
#Под переменную a было выделено памяти: 75
#Под переменную x_numb было выделено памяти: 28
#Под переменную y_numb было выделено памяти: 28
#Под переменную dist было выделено памяти: 28
#Суммарное количество выделенной памяти: 259

# №2 Урок 2 задание 8
#numb = int(input('Введите число: '))
numb = 45688423568423457887654
#a = int(input('Какое число вы хотите посчитать? '))
a = 8

s = 0
while numb > 0:
  if numb % 10 == a:
    s += 1
  numb = numb // 10

#print(s)

#print(f'Под переменную numb было выделено памяти: {sys.getsizeof(numb)}')
#print(f'Под переменную a было выделено памяти: {sys.getsizeof(a)}')
#print(f'Под переменную s было выделено памяти: {sys.getsizeof(s)}')
#print(f'Суммарное количество выделенной памяти: {sys.getsizeof(numb) + sys.getsizeof(s)}')

#Под переменную numb было выделено памяти: 24
#Под переменную a было выделено памяти: 28
#Под переменную s было выделено памяти: 28
#Суммарное количество выделенной памяти: 80

# №3 Урок 3 задание 3
#import random

lst = [8, 5, 74, 3, 82, 42, 81, 2, 72, 67]
#print(f'Первый массив: {lst}')
max = lst[0]
min = lst[0]
for i in lst:
  if i > max:
    max = i
  elif i < min:
    min = i

#print(f'Максимальное значение: {max}')
#print(f'Минимальное значение: {min}')

max_ind = lst.index(max)
min_ind = lst.index(min)
lst[max_ind], lst[min_ind] = lst[min_ind], lst[max_ind]

#print(f'Второй массив: {lst}')

#print(sys.getrefcount(lst))
#print(f'Под переменную lst было выделено памяти: {sys.getsizeof(lst)}')
#print(f'Под переменную max было выделено памяти: {sys.getsizeof(max)}')
#print(f'Под переменную min было выделено памяти: {sys.getsizeof(min)}')
#print(f'Под переменную max_ind было выделено памяти: {sys.getsizeof(max_ind)}')
#print(f'Под переменную min_ind было выделено памяти: {sys.getsizeof(min_ind)}')
#print(f'Суммарное количество выделенной памяти: {sys.getsizeof(lst) + sys.getsizeof(max)+sys.getsizeof(min)+sys.getsizeof(max_ind)+sys.getsizeof(min_ind)}')

#2
#Под переменную lst было выделено памяти: 136
#Под переменную max было выделено памяти: 28
#Под переменную min было выделено памяти: 28
#Под переменную max_ind было выделено памяти: 28
#Под переменную min_ind было выделено памяти: 28
#Суммарное количество выделенной памяти: 248
