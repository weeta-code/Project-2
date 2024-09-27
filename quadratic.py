# Authors   : Victor DeSouza
# Emails    : victordesouz@umass.edu    
# Spire IDs : 34569497

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
 
# def quadratic() -> tuple:
#     discriminant = (b ** 2) - (4 * a * c)

#     return  root1, root2
# root1, root2 = quadratic()

def discriminant(a: float, b: float, c: float) -> float:
    d = b**2 - 4 * a * c
    return d


def has_real_root(a: float, b: float, c: float) -> float:
    if discriminant(a, b, c) >= 0:
        return True
    else:
        return False

    # print(discriminant(6, 10, -1))

def get_real_roots(a: float, b: float, c:float) -> tuple:
    x1 = float((-b + discriminant(a, b, c) ** 0.5) / (2 * a))
    x2 = float((-b - discriminant(a, b, c) ** 0.5) / (2 * a))
    return (x1, x2)

# print(str(a), ' * x^2 +', str(b), '* x +', str(c), 'has roots:')
# print(float(root1))
# print(float(root2))