def distinct_pair(list):
    return_list = []
    for i in range(0, len(list) - 1):
        for j in range(2, len(list) - 0):
            if (i + j) % 2 == 1:
                return_list.append(i + j)
    sorted(return_list)
    return set(return_list)


mylist = [1, 2, 3, 4, 5, 6]
print('the distinct odd number pairs are {}'.format(distinct_pair(mylist)))