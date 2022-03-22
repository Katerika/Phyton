import random

lst = [random.randint(-100,100) for _ in range(10)]
print(lst)
min = 0

for i in lst:
  if i < min:
    min = i
    
if min == 0:
  print('В массиве нет отрицательных чисел')
else:
  print(f'Максимальный отрицательный элемент: {min}, его индекс {lst.index(min)}')