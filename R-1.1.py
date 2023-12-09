def is_multiple(multiple, number):
    if multiple % number == 0:
        return True
    else:
        return False
    
ans = is_multiple(10, 5)
print(str(ans))
