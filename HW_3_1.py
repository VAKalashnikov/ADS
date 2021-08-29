# создадим список с результатом

res = []
count = 0

for d in range(2, 10):
  for num in range(2, 100):
    if num % d == 0:
      count += 1
  res.append(count)
  count = 0

# в списке будут числа кратных чисел, начиная с деления на 2.

print(res)
