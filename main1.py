import random
import cProfile as cp

def matr(M, N):
#M = 5
#N = 4
  a = []
  
  for i in range(N):
    b = []
    for j in range(M):
      b.append(int(random.randint(0,100)))
    a.append(b)
    
  for i in a:
    print(('{:>4d}' * 5).format(*i))
  
  max = -1
  for j in range(M):
    min = 100
    for i in range(N):
      if a[i][j] < min:
        min = a[i][j]
    if min > max:
      max = min
  print(f'Максимальный элемент среди минимальных: {max}')

cp.run('matr(5, 4)')
cp.run('matr(50, 40)')
cp.run('matr(500, 400)')

#139 function calls in 0.000 seconds

 #  Ordered by: standard name

  # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    #    1    0.000    0.000    0.000    0.000 main.py:4(matr)
      #20    0.000    0.000    0.000    0.000 random.py:200(randrange)
      #20    0.000    0.000    0.000    0.000 random.py:244(randint)
      #20    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
      #1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      #5    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      #24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      #20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
      #1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      #4    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
      #22    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


#12672 function calls in 0.068 seconds

  # Ordered by: standard name

  # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #      1    0.000    0.000    0.067    0.067 <string>:1(<module>)
  #      1    0.035    0.035    0.067    0.067 main.py:4(matr)
  #   2000    0.004    0.000    0.030    0.000 random.py:200(randrange)
  #   2000    0.002    0.000    0.031    0.000 random.py:244(randint)
  #   2000    0.002    0.000    0.026    0.000 random.py:250(_randbelow_with_getrandbits)
  #      1    0.000    0.000    0.068    0.068 {built-in method builtins.exec}
  #     41    0.001    0.000    0.001    0.000 {built-in method builtins.print}
  #   2040    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
  #   2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
  #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  #     40    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
  #   2547    0.024    0.000    0.024    0.000 {method 'getrandbits' of '_random.Random' objects}


#1254111 function calls in 2.625 seconds

 #  Ordered by: standard name

  # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #      1    0.001    0.001    2.625    2.625 <string>:1(<module>)
  #      1    0.798    0.798    2.624    2.624 main.py:4(matr)
  # 200000    0.674    0.000    1.401    0.000 random.py:200(randrange)
  # 200000    0.274    0.000    1.675    0.000 random.py:244(randint)
  # 200000    0.522    0.000    0.726    0.000 random.py:250(_randbelow_with_getrandbits)
  #      1    0.000    0.000    2.625    2.625 {built-in method builtins.exec}
  #    401    0.043    0.000    0.043    0.000 {built-in method builtins.print}
  # 200400    0.106    0.000    0.106    0.000 {method 'append' of 'list' objects}
  # 200000    0.063    0.000    0.063    0.000 {method 'bit_length' of 'int' objects}
  #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  #    400    0.001    0.000    0.001    0.000 {method 'format' of 'str' objects}
  # 252906    0.141    0.000    0.141    0.000 {method 'getrandbits' of '_random.Random' objects}

#Сложность: О(n^2)
