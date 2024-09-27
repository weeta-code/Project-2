# Author: Victor DeSouza
# Email: victordesouz@umass.edu
# SPIRE ID: 34569497

from logic import nand, implies, iff, xor

def nand_of_tuple(tuple_nand):
    A = tuple_nand[0]
    B = tuple_nand[1]
    return nand(A, B)

def implies_in_both_directions(list_implies):
    A = list_implies[0]
    B = list_implies[1]

    list_implies[0] = implies(A, B)
    list_implies[1] = implies(B, A)
    return list_implies

def iff_with_result(list_append):
    A = list_append[0]
    B = list_append[1]
    list_append.append(iff(A, B))
    return list_append


def xor_with_result_in_between(list_xor):
    A = list_xor[0]
    B = list_xor[1]
    list_xor.insert(1, xor(A, B))
    return list_xor