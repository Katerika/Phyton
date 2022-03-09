num = int(input('Введите число: '))
a = 0
b = 0
while num > 0:
  if num % 10 % 2:
    a += 1
  else:
    b += 1
  num = num//10

print(f'Количетсво нечетных чисел: {a}')
print(f'Количетсво четных чисел: {b}')