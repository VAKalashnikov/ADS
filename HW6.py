# рассмотрел задачу из 7-ого уровка, так как делаю все вместе сейчас(и даже вместе с работой =)

arr = [2, 67, 13, 19, -4, 8, 10]   # (7 * 24 + 20 + 4 * 7) = 216 b

for i in range(len(arr)):
  count_gr = count_le = 0  # 24 * 2 = 48 b
  for j in range(len(arr)):
    if arr[i] > arr[j]:
      count_gr += 1
    elif arr[i] < arr[j]:
      count_le += 1
  if count_le == count_gr:
    print(arr[i], ' - это и есть медиана массива.') 

# sum = 264 b
# Windows 64bit
# Python на этом компьютере не стоит, решаю в Colab
