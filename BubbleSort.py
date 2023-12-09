
def sort(input_list):
    list(input_list)
    for j in range(0, 4):
        for i in range(len(input_list)- 1):
            if input_list[i] > input_list[i + 1]:
                input_list.insert(i + 2, input_list[i])
                input_list.remove(input_list[i])
        else:
            continue

    return input_list


print(sort([0, 2, 3, 1]))