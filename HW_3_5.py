test_list = [1, 2, 3, 4, 5, -1, 2, -2]
ind = -1

while i < len(test_list):
  if test_list[i] < 0 and ind == -1:
    ind = i
  elif test_list[ind] < test_list[i] < 0:
    ind = i
  i += 1

print('Сам элемент : {}, а его индекс : {}.'.format(test_list[ind], ind)) 