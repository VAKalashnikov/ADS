test_list = [1, 2, 3, 4, 5, -1, 2, -2, -5, -10, -10]

if test_list[0] > test_list[1]:
    min_ind_1 = 0
    min_ind_2 = 1
else:
    min_ind_1 = 1
    min_ind_2 = 0
    
for i in range(2, len(test_list)):
    if test_list[i] < test_list[min_ind_1]:
        temp = min_ind_1
        min_ind_1 = i
        if test_list[b] < test_list[min_ind_2]:
            min_ind_2 = temp
    elif test_list[i] < test_list[min_ind_2]:
        min_ind_2 = i

print(test_list[min_ind_1], test_list[min_ind_2])