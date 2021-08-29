test_list = [1, 2, 3, 4, 5, 1, 2, 2]
count_max = 1

for i in range(len(test_list)):
  count = 1
  for j in range(i + 1, len(test_list)):
    if test_list[i] == test_list[j]:
      count += 1
    if count > count_max: 
      count_max = count
      print(test_list[i], 'и есть наиболее частое число')
#    else: 
#      print('Тут каждое число лишь по одному разу встречается')