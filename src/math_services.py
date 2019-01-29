import numpy as np


# Defining function to calculate the variance
def variance(integer_list):
    """
    Calculates the variance of the list of integers.

    Receives
    --------
    integer_list : list
        List of integers.

    Returns
    -------

    var : float
        Variance of the list.
    """

    integer_array = np.array(integer_list, dtype=int)
    return np.var(integer_array).astype(float)


def product(integer_list):

    """
    Calculates the product of the list of integers.

    prod : float
        Product of the list.
    """

    integer_array = np.array(integer_list, dtype=int)
    return np.prod(integer_array).astype(float)


def square_list(integer_list):
    """
    Takes the square of every integer in the list.
        List of integer values.

    Returns
    -------
    squared_list : list
        List of the squares of integer values.
    """

    squared_list = [x**2 for x in integer_list]
    integer_list.clear()
    integer_list.extend(squared_list)
    return integer_list
