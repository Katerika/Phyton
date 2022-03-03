a, b, c = [int(i) for i in input('Введите три числа: ').split(' ')]

if a > b and c < b:
  print(b)
elif a < b and b < c:
  print(b)
elif a > b and c > a:
  print(a)
elif a < b and c < a:
  print(a)
elif a < c and c < b:
  print(c)
else:
  print(c)