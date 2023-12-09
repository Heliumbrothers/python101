#ages = [1, 2, 3, 4, 5]

#print(ages(len(ages) // 2))
def swap_item(input_list, swap1, swap2):
    input_list.append(swap1)
    input_list.remove(swap1)
    return input_list


def find_number_bigger_than(input_list, threshold_num):
    for i in range(len(input_list) - 1):
        if input_list[i] > threshold_num:
            return threshold_num
    return ValueError('Could not find a number to fulfill criteria')


def find_number_smaller_than(input_list, threshold_num):
    i = (len(input_list) - 1)
    while i != 0:
        if input_list[i] < threshold_num:
            return input_list[i]
        else:
            i = i - 1
    return ValueError('Could not find a number to fulfill criteria')

numlist = [1, 2, 3, 4, 5]
print(find_number_smaller_than(numlist, 5))


def quick_sort(input_list):
    shortlist = [min(input_list), input_list[len(input_list) // 2], max(input_list)]
    #pivot = shortlist[1]
    pivot = 19
    print(pivot)
    for i in range(0, len(input_list) - 1):
        print('loop has started')
        item_from_left = find_number_bigger_than(input_list, pivot)
        print('succes #1')
        item_from_right = find_number_smaller_than(input_list, pivot)
        print('Success #2')
        print(item_from_left)
        print(item_from_right)
        while input_list.index(item_from_left) < input_list.index(item_from_right):
            if input_list.index(pivot) < input_list.index(item_from_left):
                swap_item(input_list, pivot, item_from_left)
                print(input_list)
            else:
                swap_item(input_list, item_from_left, pivot)
                print(input_list)
    return input_list
        

ages = [5,9,4,6,1,8,4,12,3,18,7,1,5,19,21]

print('result = ' + str(quick_sort(ages)))






