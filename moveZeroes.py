#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1
        count = nums.count(0)
        nums = [i for i in nums if i != 0]
        nums = nums + [0]*count

        # Solution 2
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[j] = nums[i]
                    nums[i] = 0
                j += 1

        # Solution 3
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1