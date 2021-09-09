# Задача 1

from random import randint

def sort_bubble(list_nums):
  a = list_nums
  for i in range(len(list_nums)):
    for j in range(len(list_nums) - i - 1):
      if a[j] < a[j + 1]:
        a[j], a[j + 1] = a[j + 1], a[j]
  return a

rand_list = [randint(-100, 99) for _ in range(100)]
print(rand_list)
print(sort_bubble(rand_list))