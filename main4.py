def sum(k, a):
  if k <= 1:
    return a
  return sum(k-1, a / -2) + a

k = int(input('Введите количество элементов: '))
a = int(input('Введите значение первого элемента: '))

print(sum(k, a))
  
#k = int(input('Введите количество элементов: '))
#a = 1
#s = 0

#for i in range(k):
#  s += a
#  a /= -2

#print(round(s, 3))


