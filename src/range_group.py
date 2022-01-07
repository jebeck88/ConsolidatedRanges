# This class manages a group of ranges
from typing import List
from src.range import Range
from src.range import is_overlapping
from src.range import merge


class RangeGroup(object):
    """
    This class represents a collection of ranges
    """

    # self.ranges is a simple list of range objects
    ranges: List[Range]

    def __init__(self, inputs: List[tuple[float, float]]):
        """
        Creates a range group from a list of tuples
        :param inputs: the input ranges
        :type inputs: [(float, float)]
        """
        self.ranges = []
        for next_tup in inputs:
            self.ranges.append(Range(next_tup))

    def print(self):
        """
        This method prints out the list of ranges
        """
        result = []
        for r in self.ranges:
            result.append(r.to_tuple())
        print(result)

    def consolidate(self):
        """
        This method consolidates the list of ranges by repeatedly scanning the list and performing pair-wise mergers
        until no more mergers can be done.
        """
        while self._single_pass():
            pass

    def _single_pass(self):
        """
        This method takes a single pass over the list of ranges and tries to find a pair to merge

        :return: True if a merge occurred, False if no merges are possible
        :rtype Boolean
        """
        n = len(self.ranges)
        if n > 1:
            for i in range(0, n):
                for j in range(i+1, n):
                    r1 = self.ranges[i]
                    r2 = self.ranges[j]
                    if is_overlapping(r1, r2):
                        r3 = merge(r1, r2)
                        self.ranges.pop(i)
                        self.ranges.pop(j - 1)
                        self.ranges.append(r3)
                        return True
        return False


# Main
if __name__ == '__main__':
    # Create some test ranges
    input_ranges = [(-10, -9), (-8, -4), (-5, -3), (-7, -6), (-1, 3), (1, 2), (2, 3), (5, 8)]
    rg = RangeGroup(input_ranges)

    # Print the input ranges
    print("Input Ranges:")
    rg.print()

    # consolidate the ranges
    rg.consolidate()

    # Print the output ranges
    print("OutputRanges:")
    rg.print()
