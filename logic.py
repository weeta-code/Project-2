# Author: Victor DeSouza
# Email: victordesouz@umass.edu
# SPIRE ID: 34569497

def nand(A: bool, B: bool) -> bool:
    if A == True and B == True:
        return False
    else: 
        return True

def implies(A, B) -> bool:
    if A == True and B == False:
        return False
    else:
        return True

def iff(A, B) -> bool:
    if A == B:
        return True
    else:
        return False

def xor(A, B) -> bool:
    if A != B:
        return True
    else:
        return False
# print(nand(True, False))
# print(nand(True, True))