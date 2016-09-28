
def mmult(m, c):
    """
        mmult receives a matrix and returns a new matrix
        where every element in the matrix is multiplied
        by the provided constant
    """
    return map(lambda x: map(lambda y: y * c, x), m)


def msum(m):
    """
        msum returns the sum of every element in the matrix
    """
    return sum(map(sum, m))