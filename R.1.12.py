import random

def mychoice(data):
    return data[random.randrange(0, len(data) - 1)]



mylist = [1, 2, 3, 4, 5]
print("my choice is {}".format(mychoice(mylist)))