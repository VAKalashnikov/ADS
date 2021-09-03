# Задача 2

# Пусть надо найти i - е простое число
# Просто будем создавать массив из простых чисел, до того момента, пока в нем не станет i элементов.

list_of_primes = []

def i_prime(i):
  for num in range(2, i ** 2):
      if all(num % i != 0 for i in range(2, num)) and len(list_of_primes) < i:
        list_of_primes.append(num)
  return list_of_primes[-1]

print(i_prime(33))

time_3 = cProfile.run('i_prime(100)')
#         5796518 function calls in 1.356 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.010    0.010    1.356    1.356 <ipython-input-8-cc0502f89122>:7(i_prime)
#  5785220    0.876    0.000    0.876    0.000 <ipython-input-8-cc0502f89122>:9(<genexpr>)
#        1    0.000    0.000    1.356    1.356 <string>:1(<module>)
#     9998    0.470    0.000    1.345    0.000 {built-in method builtins.all}
#        1    0.000    0.000    1.356    1.356 {built-in method builtins.exec}
#     1229    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       67    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


import math

def erato(i):
  i_max = prime_counting_function(i)
  lst_prime = [_ for _ in range(2, i_max)]
  len_lst = len(lst_prime)

  for number in lst_prime:
    if number != 0:
      for j in range(number, len_lst, number):
        lst_prime[j] = 0
  res_list = [x for x in lst_prime if x != 0]
  return res_list[-1]      

def prime_counting_function(i):
  count_of_primes = 0
  cur_number = i
  while count_of_primes <= i:
    count_of_primes = cur_number / math.log(cur_number)
    cur_number += 1
  return cur_number

# time_4 = cProfile.run('erato(100)')
#         557 function calls in 0.001 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <ipython-input-9-66e6bcd163a0>:12(<listcomp>)
#        1    0.000    0.000    0.001    0.001 <ipython-input-9-66e6bcd163a0>:15(prime_counting_function)
#        1    0.000    0.000    0.001    0.001 <ipython-input-9-66e6bcd163a0>:3(erato)
#        1    0.000    0.000    0.000    0.000 <ipython-input-9-66e6bcd163a0>:5(<listcomp>)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      549    0.000    0.000    0.000    0.000 {built-in method math.log}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
