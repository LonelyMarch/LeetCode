#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-21 22:08:17
@FilePath: /LeetCode/2021_02_21_《初级算法_外观数列.py
@version:
@Descripttion:
'''


from collections import Counter


class Solution:
    @classmethod
    def countAndSay(self, n: int) -> str:
        i = "1"
        for times in range(n-1):
            ht = dict(Counter(i))
            i = ""
            for v, k in zip(ht.values(), ht.keys()):
                i = "".join([i, str(v), k])
        return i


print(Solution.countAndSay(5))
