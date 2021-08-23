# Задача 1

while True:
  sign = input('Введите знак: ')
  if sign == '0':
    break
  if sign in ('+','-','*','/'):
    first = float(input('Введите первое число: '))
    second = float(input('Введите второе число: '))
    if sign == '+': print('Сумма равна: ', first + second)
    elif sign == '-': print('Разность равна: ', first - second)
    elif sign == '*': print('Произведение равно: ', first * second)
    elif sign == '/': 
      try: print('Частное равно: ', first / second)
      except ZeroDivisionError: print('Делить на 0 запрещено физмат законами')
  else: print('Вы ввели неверый знак операции!!!')   

# Задача 2


num = int(input('Введите целое число: '))

even_digits = 0
odd_digits = 0

while num > 0: 
  if num % 2 == 0:
    even_digits += 1
  else:
    odd_digits += 1  
  num //= 10
  

print('Четных цифр: ', even_digits)
print('Нечетных цифр: ', odd_digits)


# Задача 3

num = int(input('Введите число: '))
inv = 0 
while num > 0:
    inv = inv * 10 + num % 10
    num = num // 10
print(inv)

# Задача 4

n = int(input('Введите число, до которого надо просуммировать: '))
sum = 0
cur_num = 1

for i in range(n):
  sum += cur_num
  cur_num /= -2
#  print('Просуммировав {} первых членов прогрессии получаем {}'.format(i + 1, sum))
print(sum)

# Задача 5

for i in range(32,128):
    print("%4d-%s" % (i,chr(i)), end='')
    if i % 10 == 0:
        print()

# Задача 6

from random import randint 

guess = randint(0, 100)
i = 1

while i <= 10:
    num = int(input(str(i) + '-я попытка: '))
    if num > guess:
        print('Ваше число больше загаданного')
    elif num < guess:
        print('Ваше число меньше загаданного')
    else:
        print('Вы угадали!')
        break
    i += 1
else:
    print('Игра окончена. Это число: ', guess)

# Задача 7

n = int(input('Введите число, до которого надо просуммировать: '))
sum = 0
cur_num = 1

for i in range(n):
  sum += cur_num
  cur_num += 1
  exact = n * (n + 1) / 2
#  print('Просуммировав {} первых членов прогрессии получаем {}'.format(i + 1, sum))
print('Сумма в цикле:' , sum)
print('Сумма по формуле:' , exact)

# Задача 8

n = int(input("Количество вводимых чисел: "))
num = int(input("Цифра для подсчетов: "))
count = 0
for i in range(1, n + 1):
    k = int(input("Введите " + str(i) + "-e число: "))
    while k > 0:
        if k % 10 == num:
            count += 1
        k = k // 10




