list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]

def list_multiplication(list1, list2):
    mylist = []
    if len(list1) != len(list2):
        raise ValueError
    else:
        for i in range(0, len(list1)):
            mylist.append(list1[i] * list2[i])
    return mylist



list3 = list_multiplication(list1, list2)
print(list3)
