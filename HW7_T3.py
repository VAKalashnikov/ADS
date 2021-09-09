# Задача 3

# будем искать без сортировки
# для каждого элемента посчитаем, сколько есть элементов больших и меньших него и остановимся, когда их будет поровну

arr = [2, 67, 13, 19, -4, 8, 10]

for i in range(len(arr)):
  count_gr = count_le = 0
  for j in range(len(arr)):
    if arr[i] > arr[j]:
      count_gr += 1
    elif arr[i] < arr[j]:
      count_le += 1
  if count_le == count_gr:
    print(arr[i], ' - это и есть медиана массива.')  

print(sorted(arr))