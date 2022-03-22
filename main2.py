import random

mas = [random.randint(0, 100) for _ in range(10)]
print(f'Первый массив: {mas}')

ind = []
for i in mas:
  if i % 2 == 0:
    ind.append(mas.index(i))

print(f'Второй массив: {ind}')