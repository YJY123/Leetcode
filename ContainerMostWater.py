#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Solution 1
        max_Area = 0
        for i in range(len(height)-1):
            for j in range(1, len(height)):
                max_Area = max(((j-i)*min(height[i], height[j])), max_Area)
        return max_Area

        # Solution 2
        i, j = 0, len(height) - 1
        max_Area = 0
        while i < j:
            max_Area = max(max_Area, (j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_Area

        # Solution 3
        l, r, width, water = 0, len(height)-1, len(height)-1, 0
        for x in range(width, 0, -1):
            if height[l] < height[r]:
                water, l = max(water, height[l]*x), l+1
            else:
                water, r = max(water, height[r]*x), r-1
        return water

        # Solution 4
        left, r, water = 0, len(height) - 1, 0
        while left < r:
            h = min(height[left], height[r])
            water, left, r = max(water, h * (r - left)), left + (height[left] == h), r - (height[r] == h)
        return water