#!/usr/bin/env python
# coding=utf-8

'''
@Author: LonelyMarch
@LastEditors: LonelyMarch
@LastEditTime: 2021-02-15 15:59:28
@FilePath: /LeetCode/2021_02_15_#13_罗马数字转整数.py
@version: 
@Descripttion: 
'''


class Solution:
    @classmethod
    def romanToInt(self, s: str) -> int:
        a = 0
        try:
            s.split("IV")[1]
            a -= 2
        except:
            pass
        try:
            s.split("IX")[1]
            a -= 2
        except:
            pass
        try:
            s.split("XL")[1]
            a -= 20
        except:
            pass
        try:
            s.split("XC")[1]
            a -= 20
        except:
            pass
        try:
            s.split("CD")[1]
            a -= 200
        except:
            pass
        try:
            s.split("CM")[1]
            a -= 200
        except:
            pass
        for item in s:
            b = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 00, "D": 500, "M": 1000}
            a += b[item]
        return a


print(Solution.romanToInt("MCMXCIV"))
