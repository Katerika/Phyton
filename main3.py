def reverse(a):
  s = ''
  while a > 0:
    s = str(s) + str(a % 10)
    a //= 10
  return s

while True:
  a = int(input('Введите число: '))
  if a != 0:
    print(reverse(a))
  else:
    break
