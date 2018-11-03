import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_sort(self):
    	nums = [1,2,3,4,5]
    	comps = selection_sort(nums)
    	self.assertEqual(comps, 10)
    	self.assertEqual(nums, [1,2,3,4,5])

    def test_sort1(self):
    	nums = [1,2,3,4,5]
    	comps = insertion_sort(nums)
    	self.assertEqual(comps, 4)
    	self.assertEqual(nums, [1,2,3,4,5])

    def test_sort2(self):
    	nums = [-4, 6, 2, 10, -3, -10]
    	comps = insertion_sort(nums)
    	self.assertEqual(nums, [-10, -4, -3, 2, 6, 10])

    def test_sort3(self):
    	nums = [3, 60, 1, -5, 2, 5, 6, 6]
    	comps = selection_sort(nums)
    	self.assertEqual(nums, [-5, 1, 2, 3, 5, 6, 6, 60])

    def test_sort4(self):
    	nums = [1,2,5,3,-1]
    	comps = insertion_sort(nums)
    	self.assertEqual(comps, 8)
    	self.assertEqual(nums, [-1,1,2,3,5])

if __name__ == '__main__': 
    unittest.main()
