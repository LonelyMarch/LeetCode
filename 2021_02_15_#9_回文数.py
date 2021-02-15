#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-15 13:04:01
@FilePath: /LeetCode/2021_02_15_#9_回文数.py
@version: 
@Descripttion: 
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = []
        b = []
        for item in str(x):
            b.append(item)
            a.insert(0, item)
        return a == b
