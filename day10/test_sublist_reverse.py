from unittest import TestCase
from .puzzle import sublist_reverse


class TestSublistReverse(TestCase):

    def test_sublist_reverse(self):
        lst = [0, 1, 2, 3, 4, 5, 6]
        reversed = sublist_reverse(2, 2, lst)
        assert reversed == [0, 1, 3, 2, 4, 5, 6]

    def test_sublist_reverse_circular_1(self):
        lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        reversed = sublist_reverse(7, 4, lst)
        assert reversed == [7, 1, 2, 3, 4, 5, 6, 0, 9, 8, ]

    def test_sublist_reverse_cirular_4(self):
        lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        reversed = sublist_reverse(8, 3, lst)
        assert reversed == [8, 1, 2, 3, 4, 5, 6, 7, 0, 9]

    def test_sublist_reverse_cirular_limit(self):
        lst = list(range(12))
        reversed = sublist_reverse(7, 12, lst)
        sol = [1, 0, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        assert reversed == sol
