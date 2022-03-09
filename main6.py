from random import randint

numb = randint(0,1000)

i = 1
while True:
  answ = int(input('Введите предполагаемое число от 1 до 1000: '))
  if answ < numb:
    print('Введите число больше')
  elif answ > numb:
    print('Введите число меньше')
  else:
    print(f'Вы угадали c {i} попытки! Это число {numb}')
    break
  i += 1
  if i > 10:
    print(f'Проиграл! Загаданное число {numb}')