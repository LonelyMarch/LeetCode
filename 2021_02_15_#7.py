#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-15 12:13:17
@FilePath: /LeetCode/2021_02_15_#7.py
@version: 
@Descripttion: 
'''


class Solution:
    def reverse(self, x: int) -> int:
        a = []
        for item in str(x):
            a.insert(0, item)
        if "-" == a[-1]:
            a.pop(-1)
            a.insert(0, "-")
        a = int("".join(a))
        if not (-2 ** 31 <= a <= 2 ** 31 - 1):
            a = 0
        return a
