# encoding: utf-8
#@Time : 2021/5/31 22:23
#@Auther : whgvjp
#@File : IsPowerOfFour.py

# class Solution:
def isPowerOfFour( n: int) -> bool:
    while n/4>=4:
        n=n/4
    return True if n==1 else False

