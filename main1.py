import random as rn

def bubble_short(list):
  n = 1
  while n < len(list):
    for i in range(len(list) - 1):
      if list[i] > list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
    n += 1

lst = [rn.randint(-100,100) for _ in range(10)]
print('Массив до сортировки: ', lst, sep='\n')

bubble_short(lst)
lst.reverse()
print('Массив после сортировки в порядке убывания: ', lst, sep='\n')