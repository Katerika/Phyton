import random

M = 5
N = 4
a = []

for i in range(N):
  b = []
  for j in range(M):
    b.append(int(random.randint(0,100)))
  a.append(b)
  
for i in a:
  print(('{:>4d}' * 5).format(*i))

max = -1
for j in range(M):
  min = 100
  for i in range(N):
    if a[i][j] < min:
      min = a[i][j]
  if min > max:
    max = min
print(f'Максимальный элемент среди минимальных: {max}')