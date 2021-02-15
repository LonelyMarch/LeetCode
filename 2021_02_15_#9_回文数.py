#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-15 13:29:34
@FilePath: /LeetCode/2021_02_15_#9_回文数.py
@version: 
@Descripttion: 
'''


class Solution:
    @classmethod
    def isPalindrome(self, x: int) -> bool:
        a = []
        b = []
        for item in str(x):
            b.append(item)
            a.insert(0, item)
        return a == b


print(Solution.isPalindrome(101))
print(Solution.isPalindrome(-101))
print(Solution.isPalindrome(453478))
