"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def GoogleSumA(list, k):
    """
    :param list: of numbers two of which should sum up to
    :param k: the number they should sum to
    :return: booloan with True if two numbers in array sum to k
    """

    dict = {}
    for i in list:
        if i in dict:
            print(str(i) + "+" + str(dict[i]) + "=" + str(k))
            return True
        else:
            dict[k-i] = i

    return False


def GoogleSumB(list, k):
    """
    :param list: of numbers two of which should sum up to
    :param k: the number they should sum to
    :return: booloan with True if two numbers in array sum to k
    """

    sorted_l = sorted(list)
    low_index = 0
    high_index = len(list)-1

    while low_index <= high_index:
        test_val = sorted_l[low_index] + sorted_l[high_index]
        print(test_val)
        if test_val == k:
            return True
        elif test_val < k:
            low_index += 1
        elif test_val > k:
            high_index -= 1

    return False


if __name__ == "__main__":
    test1 = [10, 15, 3, 7, -10, 5, 0, 0]
    print(GoogleSumA(test1, 17))
    print(GoogleSumB(test1, 17))
