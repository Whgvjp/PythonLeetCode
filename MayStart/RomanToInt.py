# encoding: utf-8
#@Time : 2021/5/27 22:55
#@Auther : whgvjp
#@File : RomanToInt.py
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 特殊情况
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

# class Solution:
def romanToInt(s: str) -> int:
     dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
     res = 0
     for i in range(len(s)-1):
         if dict[s[i]]<dict[s[i+1]]:
             res = res - dict[s[i]]
         else:
             res = res + dict[s[i]]
     res = res + dict[s[-1]]
     return res

result = romanToInt("XLIX")
print(result)
