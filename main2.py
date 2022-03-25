import cProfile as cp

# Без использования «Решета Эратосфена»
def algo(n):
  primes = []
  for i in range(2, 10000):
      for j in range(2, i):
          if i % j == 0:
              break
      else:
          primes.append(i)
  print(f'Искомое простое число = {primes[n - 1]} (без)')

# С использованием «Решета Эратосфена»
def sieve(n):
  primes = []
  nums = [i for i in range(2, 10000)]
  for i in nums:
      if i != 0:
          primes.append(i)
          for j in nums[i:]:
              if j % i == 0:
                  nums[j - 2] = 0
  print(f'Искомое простое число = {primes[n - 1]} (с)')

cp.run('algo(34)')
cp.run('sieve(34)')

# Без использования «Решета Эратосфена»
#1234 function calls in 1.615 seconds

 #  Ordered by: standard name

  # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #      1    0.000    0.000    1.615    1.615 <string>:1(<module>)
  #      1    1.614    1.614    1.615    1.615 main.py:4(algo)
  #      1    0.000    0.000    1.615    1.615 {built-in method builtins.exec}
  #      1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
  #   1229    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
  #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# С использованием «Решета Эратосфена»
#1235 function calls in 3.576 seconds

 #  Ordered by: standard name

  # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #      1    0.000    0.000    3.575    3.575 <string>:1(<module>)
  #      1    3.573    3.573    3.575    3.575 main.py:15(sieve)
  #      1    0.002    0.002    0.002    0.002 main.py:17(<listcomp>)
  #      1    0.000    0.000    3.576    3.576 {built-in method builtins.exec}
  #      1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
  #   1229    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
  #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
