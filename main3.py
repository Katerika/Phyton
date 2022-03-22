import random

lst = [random.randint(0,100) for _ in range(10)]
print(f'Первый массив: {lst}')
max = lst[0]
min = lst[0]
for i in lst:
  if i > max:
    max = i
  elif i < min:
    min = i

print(f'Максимальное значение: {max}')
print(f'Минимальное значение: {min}')

max_ind = lst.index(max)
min_ind = lst.index(min)
lst[max_ind], lst[min_ind] = lst[min_ind], lst[max_ind]

print(f'Второй массив: {lst}')

    