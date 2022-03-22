for i in range(2,10):
  res = []
  for j in range(2,100):
    if j % i == 0:
      res.append(j)
  print(f'{i} - {len(res)}')
    