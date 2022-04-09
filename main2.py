import random as rn

def merge_sort(arr):
  if len(arr) < 2:
    return arr[:]
  else:
    middle = int(len(arr) / 2)
    fst = merge_sort(arr[:middle])
    snd = merge_sort(arr[middle:])
    return merge(fst, snd)

def merge(fst, snd):
  res = []
  i, j = 0, 0

  while i < len(fst) and j < len(snd):
    if fst[i] < snd[j]:
      res.append(fst[i])
      i += 1
    else:
      res.append(snd[j])
      j += 1
  while i < len(fst):
      res.append(fst[i])
      i += 1
  while j < len(snd):
      res.append(snd[j])
      j += 1
  return res

lst = [round(rn.uniform(0,50), 3) for _ in range(10)]
print('Массив до сортировки: ', lst, sep='\n')

print('Массив после сортировки в порядке возрастания: ', merge_sort(lst), sep='\n')