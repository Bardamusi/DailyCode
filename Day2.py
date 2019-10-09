"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def product(iterable):
    """
    :param iterable: Input an iterable with elements that can be multiplied.
    :return: the product of all elements in iterable
    Uses regular for-loop so might be slow
    """

    prod = 1
    for x in iterable:
        prod *= x
    return prod


def UberArray(list):
    """
    :param list: list of integers (and not 0 as that would throw an error here)
    :return:  new array is the product of all the numbers in the original array except the one at i.
    """
    total_prod = product(list)
    res = [total_prod // x for x in list]  # Integer division is good since every entry i is a factor of the product
    return res


def UberArray2(list):
    """
    :param list: list of integers
    :return:  new array is the product of all the numbers in the original array except the one at i.
    Does the question without division, which means we can handle zeros
    Not sure if slicing the list this way is a nice way to deal with it
    """
    new_array = []
    for i in range(len(list)):
        new_array.append(product(list[:i]) * product(list[i+1:]))

    return new_array


if __name__ == "__main__":
    test = [1, 2, 3, 4, 5, 5, 10, 1000000000000000]
    print(product(test))
    print(UberArray2(test))