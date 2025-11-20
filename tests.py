import unittest
from unittest import TestCase
from thoughtful import sort, Stack


class Tests(TestCase):
    def test_case_1(self) -> None:
        width = 0
        height = 0
        length = 0
        mass = 0
        with self.assertRaises(AssertionError):
            sort(width, height, length, mass)

    def test_case_2(self) -> None:
        width = 1
        height = 1
        length = 1
        mass = 1
        expected = Stack.STANDARD
        self.assertEqual(sort(width, height, length, mass), expected)

    def test_case_3(self) -> None:
        width = 150
        height = 1
        length = 1
        mass = 1
        expected = Stack.SPECIAL
        self.assertEqual(sort(width, height, length, mass), expected)

    def test_case_4(self) -> None:
        width = 1
        height = 150
        length = 1
        mass = 1
        expected = Stack.SPECIAL
        self.assertEqual(sort(width, height, length, mass), expected)

    def test_case_5(self) -> None:
        width = 1
        height = 1
        length = 150
        mass = 1
        expected = Stack.SPECIAL
        self.assertEqual(sort(width, height, length, mass), expected)

    def test_case_6(self) -> None:
        width = 100
        height = 100
        length = 100
        mass = 1
        expected = Stack.SPECIAL
        self.assertEqual(sort(width, height, length, mass), expected)

    def test_case_7(self) -> None:
        width = 1
        height = 1
        length = 1
        mass = 20
        expected = Stack.SPECIAL
        self.assertEqual(sort(width, height, length, mass), expected)

    def test_case_8(self) -> None:
        width = 100
        height = 100
        length = 100
        mass = 20
        expected = Stack.REJECTED
        self.assertEqual(sort(width, height, length, mass), expected)

    def test_case_9(self) -> None:
        width = 10
        height = 10
        length = 10
        mass = -10
        with self.assertRaises(AssertionError):
            sort(width, height, length, mass)

    def test_case_10(self) -> None:
        width = -10
        height = 10
        length = 10
        mass = 10
        with self.assertRaises(AssertionError):
            sort(width, height, length, mass)

    def test_case_11(self) -> None:
        width = 10
        height = -10
        length = 10
        mass = 10
        with self.assertRaises(AssertionError):
            sort(width, height, length, mass)

    def test_case_12(self) -> None:
        width = 10
        height = 10
        length = -10
        mass = 10
        with self.assertRaises(AssertionError):
            sort(width, height, length, mass)


if __name__ == '__main__':
    unittest.main()
