# Author: Victor DeSouza
# Email: victordesouz@umass.edu
# SPIRE ID: 34569497

from logic import nand, implies, iff, xor

def nand_of_tuple(tuple_nand):
    A, B = tuple_nand[0, 1]
    return nand(A, B)

def implies_in_both_directions(list_implies):
   A, B = list_implies[0, 1]
   list_implies = [implies(A, B), implies(B, A)]
   return list_implies

def iff_with_result(list_append):
    A, B = list_append[0, 1]
    list_append = list_append.append(iff(A, B))
    return list_append

def xor_with_result_in_between(list_xor):
    A, B = list_xor[0, 1]
    list_xor = list_xor.insert(xor(A, B), 1)
    return list_xor