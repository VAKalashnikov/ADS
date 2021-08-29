list_in = [8, 3, 15, 6, 4, 2]
index_out = []

for i in list_in:
    if i % 2 == 0:
        index_out.append(list_in.index(i))

print(index_out)