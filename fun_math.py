# Authors   : Victor DeSouza
# Emails    : victordesouz@umass.edu    
# Spire IDs : 34569497
import math

def cullen(n: int) -> int:
    num = n * 2 ** n + 1
    return num

def woodall(n: int) -> int:
    num = n * 2 ** n - 1
    return num

def fermat(n: int) -> int:
    num = 2 ** 2 ** n + 1
    return num

def divides_evenly(dividend, divisor):
    if dividend % divisor == 0:
        return True
    else:
        return False
    
def cone_volume(r: int, h: int) -> int:
    num = math.pi * r ** 2 * (h/3)
    return num

print(cone_volume(4, 5))