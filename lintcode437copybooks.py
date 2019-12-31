#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:11:31 2019

@author: yiwang
"""

class Solution():
    def copybooks(self, pages, k):
        if pages is None or len(pages) == 0:
            return 0
        # corner case [1,2], 5
        if len(pages) <= k:
            return max(pages)
        start = 1
        end = sum(pages)
        while start + 1 < end:
            mid = (end - start) // 2 + start
            n = self.count(pages, mid)
            if n > k:
                start = mid
            elif n == k:
                end = mid
            else:
                end = mid
        if self.count(pages, start) == k:
            return start
        if self.count(pages, end) == k:
            return end
        return 0

# this routine is better to use for loop rather than while loop                
    def count(self, pages, k):
        n = 1
        bulk = pages[0]
        for i in range(1, len(pages)):
            if bulk + pages[i] > k:
                bulk = pages[i]
                n = n + 1
            else:
                bulk = bulk + pages[i]
        return n
    
t = Solution()
t0 = t.copybooks([3,2,4],2)
print(t0)