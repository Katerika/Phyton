M = 4
N = 4
a = []

for i in range(N):
  b = []
  for j in range(M):
    b.append(int(input()))
  b.append(sum(b))
  a.append(b)
  
for i in a:
  print(('{:>4d}' * 5).format(*i))