x1, y1 = [int(i) for i in input('Введите координаты первой точки: ').split(' ')]
x2, y2 = [int(i) for i in input('Введите координаты второй точки: ').split(' ')]

if x1 == x2:
  print(f'x = {x1}')
elif y1 == y2:
  print (f'y = {y1}')
else:
  if (y2 - y1) % (x2 - x1):
    k = (y2 - y1)/(x2 - x1)
  else:
    k = (y2 - y1)//(x2 - x1)
  b = y1 - k * x1
  if b < 0:
    b = abs(b)
    print(f'y = {k}x - {b}')
  else:
    print(f'y = {k}x + {b}')