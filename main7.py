import random

lst = [random.randint(0,100) for _ in range(10)]
print(lst)

min_1 = lst[0]
for i in lst:
  if i < min_1:
    min_1 = i
lst.remove(min_1)

min_2 = lst[0]
for i in lst:
  if i < min_2:
    min_2 = i
    
print(f'Минимальные числа из массива: {min_1} и {min_2}')
