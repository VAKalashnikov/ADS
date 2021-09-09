# Задача 2

# сначала реализуем функцию слияния

def merge(list_1, list_2):
  list_res = []
  i = 0
  j = 0
  while i < len(list_1) and j < len(list_2):
    if list_1[i] < list_2[j]:
      list_res.append(list_1[i])
      i += 1
    else:
      list_res.append(list_2[j])
      j += 1
  if i < len(list_1):
    list_res += list_1[i:]
  if j < len(list_2):
    list_res += list_2[j:] 
  return list_res

# теперь сортируем

def merge_sort(arr):
  if len(arr) == 1: return arr

  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  return merge(left, right)

test_list = [2, 67, 13, 19, -4, 8]
print(merge_sort(test_list))
