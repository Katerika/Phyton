import random

a = input('Что вы хотите сгенерировать? (1 - случайное целое число, 2 - случайное вещественное число, 3 - случайный символ) ')

if a == '1':
  x, y = map(int, input('Введитe диапазон целых чисел через пробел: ').split())
  z = random.randint(x, y)
  print(z)
elif a == '2':
  x, y = map(int, input('Введитe диапазон вещественных чисел через пробел: ').split())
  z = round(random.uniform(x, y), 3)
  print(z)
elif a == '3':
  x, y = input('Введитe диапазон латинских букв через пробел: ').split()
  z = chr(random.randint(ord(x), ord(y)))
  print(z)
else:
  print('Некорректно выбрано!')

