def minmax(input_list):
    _list_ = []
    input_list = sorted(input_list)
    _list_.append(input_list[0])
    _list_.append(input_list[len(input_list) - 1])
    tuple(_list_)
    return _list_

numlist = [1, 2, 3, 4]
print(minmax(numlist))