while True:
  a, b = [int(i) for i in input('Введите два числа: ').split()]
  c = input('Введите операцию (если хотите закончить введите 0): ')
  if c == '+':
    print(a+b)
  elif c == '-':
    print(a-b)
  elif c == '*':
    print(a*b)
  elif c == '/':
    if b == 0:
      b = int(input('Делить на ноль нельзя! Введите другое число: '))
      print(a/b)
  elif c == '0':
    break
  else:
    print('Значения введены неверно!')