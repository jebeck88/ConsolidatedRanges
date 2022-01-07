# test_range.py

import unittest
from src.range import Range
from src.range import is_overlapping
from src.range import is_disjoint
from src.range import merge


class RangeTest(unittest.TestCase):

    def test_ctor(self):
        r1 = Range((1, 2))
        self.assertEqual(1, r1.low())
        self.assertEqual(2, r1.high())

        r2 = Range((2, -1))
        self.assertEqual(-1, r2.low())
        self.assertEqual(2, r2.high())

        with self.assertRaises(Exception):
            Range((1, 2, 3))

        with self.assertRaises(Exception):
            Range(1)

    def test_contains(self):
        r1 = Range((-2, 2))
        self.assertTrue(r1.contains(-2))
        self.assertTrue(r1.contains(0))
        self.assertTrue(r1.contains(2))

        self.assertFalse(r1.contains(-2.5))
        self.assertFalse(r1.contains(2.6))

    def test_is_overlapping(self):
        r1 = Range((-3, -2))
        r2 = Range((-1, 1))
        r3 = Range((0, 2))
        r4 = Range((3, 10))
        r5 = Range((4, 5))

        self.assertFalse(is_overlapping(r1, r2))
        self.assertTrue(is_overlapping(r2, r3))
        self.assertFalse(is_overlapping(r3, r4))
        self.assertTrue(is_overlapping(r4, r5))

    def test_is_disjoint(self):
        r1 = Range((-3, -2))
        r2 = Range((-1, 1))
        r3 = Range((0, 2))
        r4 = Range((3, 10))
        r5 = Range((4, 5))

        self.assertNotEqual(is_overlapping(r1, r2), is_disjoint(r1, r2))
        self.assertNotEqual(is_overlapping(r2, r3), is_disjoint(r2, r3))
        self.assertNotEqual(is_overlapping(r3, r4), is_disjoint(r3, r4))
        self.assertNotEqual(is_overlapping(r4, r5), is_disjoint(r4, r5))

    def test_merge(self):

        r1 = Range((-3, -2))
        r2 = Range((-1, 1))
        r3 = Range((0, 2))

        # Cannot merge disjoint ranges
        self.assertTrue(is_disjoint(r1, r2))
        with self.assertRaises(Exception):
            merge(r1, r2)

        # Can merge overlapping ranges
        self.assertTrue(is_overlapping(r2, r3))
        r6 = merge(r2, r3)
        self.assertIsNotNone(r6)
        self.assertIsInstance(r6, Range)
        self.assertEqual(min(r2.low(), r3.low()), r6.low())
        self.assertEqual(max(r2.high(), r3.high()), r6.high())
