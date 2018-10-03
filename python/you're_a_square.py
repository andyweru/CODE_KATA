def is_square(n):
    squareroot = n**(1/2)
    if n < 0:
        return False
    elif squareroot % 1 == 0:
        return True
    else:
        return False