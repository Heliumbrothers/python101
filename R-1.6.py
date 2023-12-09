def squares_odd(num):
    value = 0
    for i in range(1, num, 2):
        value += i * i
    return value

print(squares_odd(5))