#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 19:05:28 2019

@author: yiwang
"""

# Another method is to use twice the binary search. One for finding the peak, \
# another is finding the target in the corresponding part of RSA

class Solution():
    def findTargetRSA(self, nums, target):
        if (nums is None or len(nums) == 0):
            return -1
        point = self.findPoint(nums)
        if (nums[point] > target) or (nums[point - 1] < target):
            return -1
        if (point == 0): # array is not sorted
            loc = self.binSearch(nums, target)
        if (target > nums[-1]): # select first half array
            loc = self.binSearch(nums[:point], target)
        if (target < nums[0]): # select second half array
            loc = self.binSearch(nums[point:], target)
            if (loc < 0):
                return -1
            loc = loc + point
        return loc
        
    def findPoint(self, nums):
        start = 0; end = len(nums) - 1
        while (start + 1 < end):
            mid = int((end - start) / 2) + start
            if (nums[-1] < nums[mid]):
                start = mid
            else:
                end = mid
            
        if (nums[end] > nums[-1]):
            return end + 1
        if (nums[start] > nums[-1]):
            return start + 1
        return 0
            
    def binSearch(self, nums2, target):
        start = 0; end = len(nums2) -1
        while (start + 1 < end):
            mid = int((end - start) / 2) + start
            if (target == nums2[mid]):
                return mid
            if (target > nums2[mid]):
                start = mid
            else:
                end = mid
        if (nums2[start] == target):
            return start
        if (nums2[end] == target):
            return end
        return -1
    
t = Solution()
t0 = t.findTargetRSA([4,5,6,7,0,1,2], 0)
print(t0)