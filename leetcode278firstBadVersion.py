#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 00:55:04 2019

@author: yiwang
"""

class Solution:
    def isBadVersion(self, n):
        return n < 5
        
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # false is 1 not 0.
        if (n <= 1 or (self.isBadVersion(n) == 1)):
            return -1
        
        start = 0
        end = n
        while (start + 1 < end):
            mid = (end - start) // 2 + start
            if self.isBadVersion(mid) == 0:
                end = mid
            else:
                start = mid
                
        if self.isBadVersion(start) == 0:
            return start
        if self.isBadVersion(end) == 0:
            return end
        
t = Solution()
print(t.firstBadVersion(10))

print(t.isBadVersion(10))

