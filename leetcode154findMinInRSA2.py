#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 19:39:09 2019

@author: yiwang
"""

"""
due to [1,1,1,0,1], binary search does not work. So, O(logN) -> O(N)
I used line - line

Another solution:
    line 40 "end = mid" change to  "end = end - 1"
    and all nums[-1] in line 39 - line 43 change to nums[end]
    the same idea that O(logN) -> O(N)
"""

class Solution:
    def findmin(self, nums):
        if nums is None or len(nums) == 0:
            return -1
        
        start = 0
        end = len(nums) - 1
        
        if nums[start] == nums[end]:
            # for case [1]
            if len(nums) == 1:
                return nums[0]
            # for case[1,1,1,0,1]
            while ((nums[start] == nums[start + 1]) and \
                   (start + 1 < len(nums) - 1)):
                start = start + 1
            start = start + 1
        
        while (start + 1 < end):
            mid = (end - start) // 2 + start
            if nums[mid] == nums[-1]:
                end = mid
            if nums[mid] < nums[-1]:
                end = mid
            if nums[mid] > nums[-1]:
                start = mid
        
        if nums[start] <= nums[-1]:
            return nums[start]
        if nums[end] <= nums[-1]:
            return nums[end]
        return -1#num[0]
    
t = Solution()
n = t.findmin([2,4,7,9,0,2,2])
print(n)

n = t.findmin([1,1,1,0,1])
print(n)

n = t.findmin([2,2,3,2,2])
print(n)

n = t.findmin([1,1,1,1,1])
print(n)

n = t.findmin([1])
print(n)


