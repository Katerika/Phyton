def sum(n):
  if n <= 1:
   return n
  return n + sum(n-1)
  
#  s = 0
#  for i in range(1, n+1):
#    s += i
#  return s
    
n = int(input('Введите число: '))

a = sum(n)
b = n * (n + 1)//2

if a == b:
  print(f'Равенство выполняется: {a} = {b}')
else:
  print(f'Равенство не выполняется: {a} != {b}')