#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 23:48:48 2019

@author: yiwang
"""

"""
the time complexity is nlogMax(L)
n is because calculating the count
"""


class Solution():
    def woodcut(self, L, k):
        if L is None or len(L) == 0:
            return 0
        start = 0
        end = max(L[:])
        while start + 1 < end:
            mid = (end - start) // 2 + start
            count = self.count(L, mid)
            if count >= k:
                start = mid
            else:
                end = mid
            
        if self.count(L, end) >= k:
            return end
        if self.count(L, start) >= k:
            return start
        return 0

    def count(self, L, length):
        if length == 0:
            return 0
        n = 0
        for i in range(len(L)):
            n = n + L[i]//length
        return n
    
t = Solution()
t0 = t.woodcut([232, 124, 456], 7)
print(t0)
t0 = t.woodcut([6,6,5,5,6,5,4,4,5,6,6,6,5,4,5,6,5,6,4,4,4,4,6,4,5,5,4,6,6,6,6,4,6,4,4,5,6,5,5,4,6,4,6,4,4,6,4,5,6,5,6,6,5,4,4,5,6,4,5,5,5,6,6,4,4,5,5,6,5,5,6,4,6,4,5,6,4,4,4,6,4,6,4,5,4,6,5,6,6,5,4,4,6,5,6,5,6,4,4,6,4,6,5,4,4,4,4,6,6,4,6,6,6,5,4,4,6,4,4,4,5,4,6,4,6,6,4,5,6,5,6,5,4,5,5,5,4,6,5,4,5,6,4,4,6,6,5,6,6,4,6,5,6,5,4,6,4,6,4,6,5,6,4,6,6,4,5,4,6,6,5,6,6,5,4,4,4,4,4,5,5,4,6,5,4,6,4,6,5,6,6,5,4,5,6,4,4,6,5,5,6,6,6,4,6,6,5,6,5,4,6,5,4,6,5,6,4,5,4,4,5,4,5,6,6,4,4,4,4,6,6,6,6,6,5,5,4,4,5,5,6,6,5,6,6,6,4,5,5,4,6,4,6,4,4,6,5,6,6,6,5,4,4,4,6,4,6,4,5,6,6,4,5,6,6,6,6,6,4,5,6,4,4,4,4,5,5,5,6,5,5,5,4,4,5,6,6,4,6,6,6,4,5,4,6,5,6,5,5,6,5,4,5,4,6,4,5,5,5,5,5,5,4,5,5,6,4,5,6,5,6,5,6,4,4,5,6,5,6,6,6,5,4,5,4,6,6,6,6,4,5,5,4,5,5,5,4,6,5,5,4,6,5,6,6,6,4,4,4,6,4,6,6,4,5,4,5,6,6,6,5,6,4,6,6,5,6,5,6,4,4,6,4,6,5,6,6,5,4,6,5,6,6,5,6,6,4,6,6,5,6,5,6,4,5,5,5,6,6,4,5,4,4,6,4,6,6,5,6,6,6,5,6,6,4,6,6,5,5,6,5,6,6,6,5,5,6,6,5,4,6,5,6,5,6,5,5,6,5,4,5,6,5,4,6,5,5,4,5,4,5,6,5,6,4,6,5,4,4,4,5,5,4,5,4,6,4,5,5,6,5,6,6,5,4,6,6,5,5,6,5,5,5,5,6,5,5,4,4,6,4,5,4,6,6,5,6,5,6,6,4,5,5,5,5,6,6,4,4,5,6,5,5,6,4,6,6,5,5,6,4,4,4,4,5,4,5,4,5,5,4,5,5,5,4,6,4,4,4,5,4,4,5,4,6,6,5,6,4,4,6,6,4,4,5,6,5,5,4,6,6,4,6,5,4,5,5,6,6,6,4,6,6,5,6,4,5,6,4,6,4,5,5,4,4,6,6,6,4,6,5,5,4,5,5,4,5,6,6,6,4,5,4,5,6,4,6,4,5,4,5,4,6,6,6,5,4,6,4,6,4,5,6,5,6,6,6,5,4,5,6,6,6,6,4,5,6,5,4,4,5,5,4,4,4,5,4,6,6,6,6,4,5,5,4,5,4,5,4,4,6,4,5,5,6,4,6,5,4,6,4,6,5,5,6,5,4,4,5,4,4,5,5,5,5,4,4,5,6,4,4,6,6,5,4,6,5,5,4,4,6,4,6,4,5,6,4,5,4,6,5,4,4,5,6,4,4,5,5,6,6,6,6,6,6,4,6,5,6,6,6,6,4,4,5,6,5,4,5,4,4,5,6,5,5,4,4,4,6,6,6,6,6,4,5,4,4,4,4,5,6,4,4,5,5,6,6,6,6,4,6,6,5,4,6,4,5,4,5,5,4,6,6,4,6,4,5,4,5,5,4,6,5,5,4,4,6,6,5,5,4,6,5,5,6,6,4,6,6,4,6,6,4,5,6,6,5,4,5,4,5,5,5,4,6,5,4,6,5,4,4,5,6,5,5,6,4,4,6,4,4,5,4,5,5,4,5,5,4,4,6,4,5,6,4,4,5,6,6,4,5,4,6,5,5,5,5,6,4,5,6,6,6,4,6,5,4,6,5,4,5,4,5,4,6,4,6,6,4,5,6,4,4,6,5,4,4,5,6,6,4,6,6,4,6,5,6,6,4,4,5,5,6,5,4,4,5,4,5,4,4,6,4,4,4,4,4,4,6,6,6,5,6,5,5,4,5,5,5,5,5,6,5,6,4,6,5,4,5,4,5,4,6,5,5,4,5,6,5,4,5,5,6,4,6,5,6,4,6,6,5,6,4,4,4,5,4,6,4,4,4,5,4,5,4,6,4,4,5,4,5,6,4,6,6,5,4,5,4,5,6,4,5,6,4,5,4,5,5,4,4,5,4,5,6,5,4,5,5,6,4,5,5,4,6,6,6,5,5,5,6,6,4,6,5,4,6,6,6,5,6,6,4,4,5,6,4,4,5,6,5,5,5,6,6,5,4,6,6,5,4,5,6,4,4,6,4,6,4,4,5,4,5,4,5,4,6,4,5,5,6,5,5,4,6,6,4,6,5,5,5,6,5,4,5,6,6,4,6,6,4,5,6,4,6,4,5,4,4,6,5,5,4,6,5,4,6,6,4,4,5,6,4,4,4,4,4,6,6,6,4,5,5,4,4,5,4,4,5,6,5,4,6,6,6,5,6,5,4,5,4,6,6,5,6,5,4,4,5,4,4,4,6,4,5,5,4,4,5,4,5,5,5,5,5,6,4,5,4,4,4,4,4,4,5,4,6,5,5,4,4,5,5,4,4,5,5,6,4,6,4,5,5,6,5,5,6,4,4,5,5,6,5,4,4,4,4,4,6,5,4,5,6,4,4,6,4,4,4,6,4,4,6,5,6,6,6,5,6,5,4,5,4,5,5,6,5,6,4,6,5,6,4,4,6,6,4,4,5,5,5,5,5,4,6,4,5,4,4,4,4,5,6,4,4,5,4,5,5,6,6,5,6,6,5,6,6,5,5,4,5,4,5,5,5,4,4,6,5,4,6,6,6,4,4,6,5,6,5,6,6,4,5,6,6,6,4,4,4,5,4,4,6,5,5,6,4,6,4,6,4,4,4,5,6,6,6,6,5,6,5,5,4,4,6,4,6,4,4,6,6,5,4,4,6,5,4,5,4,4,6,6,6,5,5,5,6,6,6,4,4,6,5,6,4,6,5,6,5,5,5,5,6,5,6,6,4,6,6,6,6,4,5,6,5,6,4,6,6,5,5,4,4,6,4,4,5,4,4,5,6,6,4,4,6,6,6,4,5,4,5,6,6,5,6,4,5,5,5,4,4,4,5,4,5,5,5,5,4,4,5,5,6,4,6,5,5,4,4,6,6,5,6,4,4,6,4,6,4,6,4,4,4,6,5,6,4,6,5,4,4,6,4,6,6,4,5,6,6,4,4,4,4,6,5,4,4,5,5,6,6,5,4,4,4,6,6,5,5,5,6,4,5,4,5,5,4,4,6,5,4,5,4,6,5,6,5,4,4,6,4,5,6,5,4,5,4,5,4,4,5,6,5,6,5,4,5,4,4,5,6,4,6,4,6,4,5,4,4,6,5,5,5,4,5,6,4,5,4,4,6,5,5,6,5,6,6,4,4,6,6,6,6,4,6,4,4,5,4,4,4,6,6,5,4,6,4,6,6,6,5,4,5,6,5,5,5,5,5,4,4,6,4,5,5,5,5,5,5,5,4,6,4,6,6,4,5,4,4,6,5,6,5,4,4,6,5,6,5,6,5,5,6,6,6,5,4,4,4,5,4,6,6,5,5,4,6,5,6,6,5,4,4,5,4,6,5,4,6,6,5,5,5,5,6,6,6,6,6,4,6,6,5,6,6,4,4,4,4,5,4,5,4,4,6,6,6,6,6,6,5,5,5,5,5,5,4,5,4,6,4,4,5,5,5,6,6,5,6,5,4,4,4,6,6,5,6,4,5,5,6,6,4,5,5,4,5,5,4,5,6,5,6,5,6,6,5,5,4,5,4,5,6,5,5,5,4,4,6,5,5,4,4,6,6,6,6,5,6,6,4,5,5,4,5,4,4,4,4,5,6,6,5,4,4,4,5,6,5,5,4,4,6,5,4,6,4,4,4,4,5,6,4,5,5,4,5,4,5,6,5,5,4,5,6,4,5,4,4,4,6,5,4,5,6,4,5,4,4,4,5,5,5,6,6,4,4,6,6,4,4,5,5,6,4,6,6,6,6,4,5,6,4,6,6,6,5,6,5,6,5,5,5,5,5,5,5,4,6,5,4,4,6,6,6,6,6,4,5,4,6,4,5,5,6,6,5,5,6,6,5,6,5,6,4,5,4,5,4,5,6,5,4,5,5,6,4,4,6,6,6,6,5,5,6,4,6,4,6,6,6,6,4,6,5,4,6,4,4,5,6,6,6,6,4,5,6,4,6,4,4,4,6,6,4,5,6,4,6,6,5,6,6,6,5,5,4,4,5,5,5,6,5,6,6,6,6,6,5,5,5,6,4,5,6,5,4,4,5,4,5,5,4,4,6,4,4,6,4,5],90000)
print(t0)
t0 = t.woodcut([6,6,5,5,6,5,4,4,5,6,6,6,5,4,5,6,5,6,4,4,4,4,6,4,5,5,4,6,6,6,6,4,6,4,4,5,6,5,5,4,6,4,6,4,4,6,4,5,6,5,6,6,5,4,4,5,6,4,5,5,5,6,6,4,4,5,5,6,5,5,6,4,6,4,5,6,4,4,4,6,4,6,4,5,4,6,5,6,6,5,4,4,6,5,6,5,6,4,4,6,4,6,5,4,4,4,4,6,6,4,6,6,6,5,4,4,6,4,4,4,5,4,6,4,6,6,4,5,6,5,6,5,4,5,5,5,4,6,5,4,5,6,4,4,6,6,5,6,6,4,6,5,6,5,4,6,4,6,4,6,5,6,4,6,6,4,5,4,6,6,5,6,6,5,4,4,4,4,4,5,5,4,6,5,4,6,4,6,5,6,6,5,4,5,6,4,4,6,5,5,6,6,6,4,6,6,5,6,5,4,6,5,4,6,5,6,4,5,4,4,5,4,5,6,6,4,4,4,4,6,6,6,6,6,5,5,4,4,5,5,6,6,5,6,6,6,4,5,5,4,6,4,6,4,4,6,5,6,6,6,5,4,4,4,6,4,6,4,5,6,6,4,5,6,6,6,6,6,4,5,6,4,4,4,4,5,5,5,6,5,5,5,4,4,5,6,6,4,6,6,6,4,5,4,6,5,6,5,5,6,5,4,5,4,6,4,5,5,5,5,5,5,4,5,5,6,4,5,6,5,6,5,6,4,4,5,6,5,6,6,6,5,4,5,4,6,6,6,6,4,5,5,4,5,5,5,4,6,5,5,4,6,5,6,6,6,4,4,4,6,4,6,6,4,5,4,5,6,6,6,5,6,4,6,6,5,6,5,6,4,4,6,4,6,5,6,6,5,4,6,5,6,6,5,6,6,4,6,6,5,6,5,6,4,5,5,5,6,6,4,5,4,4,6,4,6,6,5,6,6,6,5,6,6,4,6,6,5,5,6,5,6,6,6,5,5,6,6,5,4,6,5,6,5,6,5,5,6,5,4,5,6,5,4,6,5,5,4,5,4,5,6,5,6,4,6,5,4,4,4,5,5,4,5,4,6,4,5,5,6,5,6,6,5,4,6,6,5,5,6,5,5,5,5,6,5,5,4,4,6,4,5,4,6,6,5,6,5,6,6,4,5,5,5,5,6,6,4,4,5,6,5,5,6,4,6,6,5,5,6,4,4,4,4,5,4,5,4,5,5,4,5,5,5,4,6,4,4,4,5,4,4,5,4,6,6,5,6,4,4,6,6,4,4,5,6,5,5,4,6,6,4,6,5,4,5,5,6,6,6,4,6,6,5,6,4,5,6,4,6,4,5,5,4,4,6,6,6,4,6,5,5,4,5,5,4,5,6,6,6,4,5,4,5,6,4,6,4,5,4,5,4,6,6,6,5,4,6,4,6,4,5,6,5,6,6,6,5,4,5,6,6,6,6,4,5,6,5,4,4,5,5,4,4,4,5,4,6,6,6,6,4,5,5,4,5,4,5,4,4,6,4,5,5,6,4,6,5,4,6,4,6,5,5,6,5,4,4,5,4,4,5,5,5,5,4,4,5,6,4,4,6,6,5,4,6,5,5,4,4,6,4,6,4,5,6,4,5,4,6,5,4,4,5,6,4,4,5,5,6,6,6,6,6,6,4,6,5,6,6,6,6,4,4,5,6,5,4,5,4,4,5,6,5,5,4,4,4,6,6,6,6,6,4,5,4,4,4,4,5,6,4,4,5,5,6,6,6,6,4,6,6,5,4,6,4,5,4,5,5,4,6,6,4,6,4,5,4,5,5,4,6,5,5,4,4,6,6,5,5,4,6,5,5,6,6,4,6,6,4,6,6,4,5,6,6,5,4,5,4,5,5,5,4,6,5,4,6,5,4,4,5,6,5,5,6,4,4,6,4,4,5,4,5,5,4,5,5,4,4,6,4,5,6,4,4,5,6,6,4,5,4,6,5,5,5,5,6,4,5,6,6,6,4,6,5,4,6,5,4,5,4,5,4,6,4,6,6,4,5,6,4,4,6,5,4,4,5,6,6,4,6,6,4,6,5,6,6,4,4,5,5,6,5,4,4,5,4,5,4,4,6,4,4,4,4,4,4,6,6,6,5,6,5,5,4,5,5,5,5,5,6,5,6,4,6,5,4,5,4,5,4,6,5,5,4,5,6,5,4,5,5,6,4,6,5,6,4,6,6,5,6,4,4,4,5,4,6,4,4,4,5,4,5,4,6,4,4,5,4,5,6,4,6,6,5,4,5,4,5,6,4,5,6,4,5,4,5,5,4,4,5,4,5,6,5,4,5,5,6,4,5,5,4,6,6,6,5,5,5,6,6,4,6,5,4,6,6,6,5,6,6,4,4,5,6,4,4,5,6,5,5,5,6,6,5,4,6,6,5,4,5,6,4,4,6,4,6,4,4,5,4,5,4,5,4,6,4,5,5,6,5,5,4,6,6,4,6,5,5,5,6,5,4,5,6,6,4,6,6,4,5,6,4,6,4,5,4,4,6,5,5,4,6,5,4,6,6,4,4,5,6,4,4,4,4,4,6,6,6,4,5,5,4,4,5,4,4,5,6,5,4,6,6,6,5,6,5,4,5,4,6,6,5,6,5,4,4,5,4,4,4,6,4,5,5,4,4,5,4,5,5,5,5,5,6,4,5,4,4,4,4,4,4,5,4,6,5,5,4,4,5,5,4,4,5,5,6,4,6,4,5,5,6,5,5,6,4,4,5,5,6,5,4,4,4,4,4,6,5,4,5,6,4,4,6,4,4,4,6,4,4,6,5,6,6,6,5,6,5,4,5,4,5,5,6,5,6,4,6,5,6,4,4,6,6,4,4,5,5,5,5,5,4,6,4,5,4,4,4,4,5,6,4,4,5,4,5,5,6,6,5,6,6,5,6,6,5,5,4,5,4,5,5,5,4,4,6,5,4,6,6,6,4,4,6,5,6,5,6,6,4,5,6,6,6,4,4,4,5,4,4,6,5,5,6,4,6,4,6,4,4,4,5,6,6,6,6,5,6,5,5,4,4,6,4,6,4,4,6,6,5,4,4,6,5,4,5,4,4,6,6,6,5,5,5,6,6,6,4,4,6,5,6,4,6,5,6,5,5,5,5,6,5,6,6,4,6,6,6,6,4,5,6,5,6,4,6,6,5,5,4,4,6,4,4,5,4,4,5,6,6,4,4,6,6,6,4,5,4,5,6,6,5,6,4,5,5,5,4,4,4,5,4,5,5,5,5,4,4,5,5,6,4,6,5,5,4,4,6,6,5,6,4,4,6,4,6,4,6,4,4,4,6,5,6,4,6,5,4,4,6,4,6,6,4,5,6,6,4,4,4,4,6,5,4,4,5,5,6,6,5,4,4,4,6,6,5,5,5,6,4,5,4,5,5,4,4,6,5,4,5,4,6,5,6,5,4,4,6,4,5,6,5,4,5,4,5,4,4,5,6,5,6,5,4,5,4,4,5,6,4,6,4,6,4,5,4,4,6,5,5,5,4,5,6,4,5,4,4,6,5,5,6,5,6,6,4,4,6,6,6,6,4,6,4,4,5,4,4,4,6,6,5,4,6,4,6,6,6,5,4,5,6,5,5,5,5,5,4,4,6,4,5,5,5,5,5,5,5,4,6,4,6,6,4,5,4,4,6,5,6,5,4,4,6,5,6,5,6,5,5,6,6,6,5,4,4,4,5,4,6,6,5,5,4,6,5,6,6,5,4,4,5,4,6,5,4,6,6,5,5,5,5,6,6,6,6,6,4,6,6,5,6,6,4,4,4,4,5,4,5,4,4,6,6,6,6,6,6,5,5,5,5,5,5,4,5,4,6,4,4,5,5,5,6,6,5,6,5,4,4,4,6,6,5,6,4,5,5,6,6,4,5,5,4,5,5,4,5,6,5,6,5,6,6,5,5,4,5,4,5,6,5,5,5,4,4,6,5,5,4,4,6,6,6,6,5,6,6,4,5,5,4,5,4,4,4,4,5,6,6,5,4,4,4,5,6,5,5,4,4,6,5,4,6,4,4,4,4,5,6,4,5,5,4,5,4,5,6,5,5,4,5,6,4,5,4,4,4,6,5,4,5,6,4,5,4,4,4,5,5,5,6,6,4,4,6,6,4,4,5,5,6,4,6,6,6,6,4,5,6,4,6,6,6,5,6,5,6,5,5,5,5,5,5,5,4,6,5,4,4,6,6,6,6,6,4,5,4,6,4,5,5,6,6,5,5,6,6,5,6,5,6,4,5,4,5,4,5,6,5,4,5,5,6,4,4,6,6,6,6,5,5,6,4,6,4,6,6,6,6,4,6,5,4,6,4,4,5,6,6,6,6,4,5,6,4,6,4,4,4,6,6,4,5,6,4,6,6,5,6,6,6,5,5,4,4,5,5,5,6,5,6,6,6,6,6,5,5,5,6,4,5,6,5,4,4,5,4,5,5,4,4,6,4,4,6,4,5],9000)
print(t0)
