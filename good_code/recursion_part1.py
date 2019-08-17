
"""
Recursion
Part 1
"""


def findPairs(my_list, tag=10):
    """
    return the number of pairs numbers within the integer that sum to 10
    :param my_list: tuple
    :param tag: int
    :return: int
    """

    def get_str(List):
        # connect all elements in tuple to string
        try:
            len(List)  # special case when tuple like (12937)
            if len(List) == 0:  # base line
                return ''

            elif len(List) == 1:
                return str(List[0])

            else:
                return str(List[0]) + get_str(List[1:])  # recursion

        except TypeError:
            return str(List)

    def inner(a):
        # inner loop

        if len(a) == 2:  # base line
            if int(a[0]) + int(a[1]) == tag:
                return 1
            else:
                return 0

        if int(a[0]) + int(a[1]) == tag:
            a = a[0] + a[2:]
            return 1 + inner(a)

        else:
            a = a[0] + a[2:]
            return inner(a)

    def outer(a):
        # outer loop
        if len(a) == 2:  # base line
            return inner(a)

        else:
            return inner(a) + outer(a[1:])

    my_str = get_str(my_list)

    # special situation
    if len(my_str) < 2:
        return None

    num = outer(my_str)
    return num


def recMin(nestedLis, num=float('inf')):
    """
    return the smallest value in nestedLis

    :param nestedLis: list
    :param num: default
    :return: int
    """

    if len(nestedLis) == 0:  # base line
        if num == float('inf'):
            return None
        else:
            return num

    Lis_zero = nestedLis[0]
    nestedLis.remove(nestedLis[0])

    # recursion
    try:
        len(Lis_zero)  # if Lis_zero is list
        return recMin(Lis_zero + nestedLis, num)

    except TypeError:
        if Lis_zero < num:
            return recMin(nestedLis, Lis_zero)
        else:
            return recMin(nestedLis, num)


def mergeList(nestedLis):
    """
    return a single list containing all of the values in nestedLis

    :param nestedLis: list
    :return: list
    """
    if len(nestedLis) == 0:  # base line
        return []

    Lis_zero = nestedLis[0]
    nestedLis.remove(nestedLis[0])

    # recursion
    try:
        len(Lis_zero)
        return mergeList(Lis_zero + nestedLis)
    except TypeError:
        return [Lis_zero] + mergeList(nestedLis)


def addNext(n):
    """
    calculate the sum of every other integer between 0 and n

    :param n: int
    :return: int
    """
    if n < 2:  # base line
        return n
    return n + addNext(n - 2)  # recursion


def swapElements(my_list):
    """
    return a copy of the list in which neighboring elements have been swapped

    :param my_list: list
    :return: list
    """

    if len(my_list) < 2:  # base line
        return []

    pair = my_list[:2][::-1]  # change index
    my_list.remove(my_list[0])
    my_list.remove(my_list[0])

    return pair + swapElements(my_list)  # recusion


def funkyNums(num):
    """
    print inverted sequence

    :param num: positive int
    :return: no return , just print
    """
    if len(str(num)) == 1:  # base line
        print(num)

    else:
        print(str(num)[-1], end='')  # recursion
        funkyNums(str(num)[:-1])


def calcStamp(my_tuple):
    """
    return the min number of stamps that would be required in order to pay the postage cost

    :param my_tuple: tuple
    :return: int
    """

    def helper(i, tmp_sum, tmp):
        # find all solution

        if tmp_sum > target or i == n:  # base line
            return

        if tmp_sum == target:
            res.append(tmp)
            return

        helper(i,  tmp_sum + postage_cost[i], tmp + [postage_cost[i]])
        helper(i+1, tmp_sum, tmp)

    def find_shortest(res, min_len=float('inf')):
        # find shortest solution in res, then return length

        if len(res) == 1:  # base line

            if min_len < len(res[0]):
                return min_len
            else:
                return len(res[0])

        pre_len = len(res[0])

        if pre_len < min_len:
            later_len = find_shortest(res[1:], min_len=pre_len)

            if pre_len < later_len:
                return pre_len

            else:
                return later_len

        else:
            later_len = find_shortest(res[1:], min_len=min_len)

            if min_len < later_len:
                return min_len

            else:
                return later_len

    target = my_tuple[0]
    postage_cost = my_tuple[1]

    n = len(postage_cost)
    res = []
    helper(0, 0, [])
    return find_shortest(res, min_len=float('inf'))
