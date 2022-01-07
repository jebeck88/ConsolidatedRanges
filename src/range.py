from typing import Tuple


class Range(object):
    """
    This class represents a single range, with a low and high value
    """

    def __init__(self, tup: Tuple[float, float]):
        """
        Construct a Range given a tuple
        :param tup: the input tuple
        :type tup: (float, float)
        """
        if len(tup) != 2:
            raise Exception("A range only accepts a tuple with 2 values")
        self.tup = min(tup), max(tup)

    def high(self):
        """
        :return: the high value of the range
        :rtype: float
        """
        return self.tup[1]

    def low(self):
        """
        :return: the low value of the range
        :rtype: float
        """
        return self.tup[0]

    def contains(self, value: float):
        """
        Returns True if value is contained in this range

        :param value: The value to test
        :return True if value is contained in the range
        """
        return self.low() <= value <= self.high()

    def to_tuple(self):
        """
        :return: the range object expressed as a tuple
        :rtype: (float, float)
        """
        return self.tup


def is_overlapping(r1: Range, r2: Range):
    """
    Returns true if the ranges r1 and r2 overlap

    :param r1: The first range
    :param r2: The second range
    :return: True if the two ranges overlap
    """
    return r1.contains(r2.low()) or r1.contains(r2.high()) or r2.contains(r1.low()) or r2.contains(r1.high())


def is_disjoint(r1: Range, r2: Range):
    """
    Returns true if the ranges r1 and r2 are disjoint

    :param r1: The first range
    :param r2: The second range
    :return: True if the two ranges overlap
    """
    return not is_overlapping(r1, r2)


def merge(r1: Range, r2: Range):
    """
    Merges two overlapping ranges together into a new range

    :param r1: The first range
    :param r2: The second range
    :return: a new Range object that spans the entire range of both r1 and r2
    :rtype: Range
    :raise Exception if r1 and r2 are disjoint
    """
    if is_disjoint(r1, r2):
        raise Exception("Cannot merge disjoint ranges")

    low = min(r1.low(), r2.low())
    high = max(r1.high(), r2.high())
    return Range((low, high))
