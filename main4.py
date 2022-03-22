import random

lst = [random.randint(0, 100) for _ in range(10)]
print(lst)
numb = 0

for i in lst:
  if lst.count(i) > lst.count(numb):
    numb = i
    
if lst.count(numb) == 1:
  print('Каждое число встречается только один раз')
else:
  print(f'Число {numb} встречается чаще всего,{lst.count(numb)} раз')