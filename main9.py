n = int(input('Введите число: '))
max_n = 0
max_s = 0

while n != 0:
  i = n
  s = 0
  while n > 0:
    s += n % 10
    n = n // 10
  if s > max_s:
    max_n = i
    max_s = s
  print(f'Наибольшее число по сумме цифр {max_n}, его сумма {max_s}')
  n = int(input('Введите число (для выхода нажмите 0): '))
  