from math import *
def is_square(n):
    if n%sqrt(n)==0:
        return True
    else:
        return False 

print(is_square(3))