import random

lst = [random.randint(0,100) for _ in range(10)]
print(lst)
min = lst[0]
max = lst[0]
s = 0

for i in lst:
  if i > max:
    max = i
  elif i < min:
    min = i
min_id = lst.index(min)
max_id = lst.index(max)

if min_id < max_id:
  for i in lst[(lst.index(min)+1):lst.index(max)]:
    s += i
  print(f'Сумма между минимальным {min} и максимальным {max} элементами равна {s}')  
else:
  for i in lst[(lst.index(max)+1):lst.index(min)]:
    s += i
  print(f'Сумма между максимальным {max} и минимальным {min} элементами равна {s}')

