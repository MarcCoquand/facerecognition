

def mmult(m, c):
    """
    Receives a matrix and returns a new matrix
    where every element in the matrix is multiplied
    by the provided constant
    :param m: matrix
    :param c: constant
    :return: new matrix with the applied constant
    """
    return map(lambda x: x * c, m)


def msum(m):
    """
    Returns the sum of every element in the matrix
    """
    return sum(map(sum, m))


def apply(op, l1, l2):
    """
    Returns a list of the same length as l1 and l2 where each
    index is the result of the provided operation on l1[i] & l2[i]
    NOTE: Shadows built in function apply but since it is deprecated
    since version 2.3 we don't care.
    Reference: https://docs.python.org/2/library/functions.html#apply
    """
    return map(lambda tup: op(float(tup[0]), float(tup[1])), zip(l1, l2))


def flatten(l):
    """
    Receives a nested list and returns all the values in a single list
        Example: [[1], [2, 3], 4] -> [1, 2, 3, 4]
    :return: flattened list
    """
    if not l: return l
    return flatten(l[0]) + flatten(l[1:]) if isinstance(l[0], list) else l[:1] + flatten(l[1:])

