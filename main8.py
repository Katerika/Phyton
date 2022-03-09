numb = int(input('Введите число: '))
a = int(input('Какое число вы хотите посчитать? '))

s = 0
while numb > 0:
  if numb % 10 == a:
    s += 1
  numb = numb // 10

print(s)