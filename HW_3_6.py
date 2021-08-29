ind_min = 0
ind_max = 0
test_list = [1, 2, 3, 4, 5, -1, 2, -2, -5]

for i in range(1, len(test_list)):
  if test_list[i] < test_list[ind_min]:
    min_id = i
  elif test_list[i] > test_list[ind_max]:
    max_id = i

print(min_id, max_id)
print(test_list[min_id], test_list[max_id])

sum = 0
for k in range(min_id, max_id):
  sum += test_list(k)

print(sum)