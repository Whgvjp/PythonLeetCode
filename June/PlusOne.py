# encoding: utf-8
#@Time : 2021/6/4 20:08
#@Auther : whgvjp
#@File : PlusOne.py

from typing import List
def plusOne(digits: List[int]) -> List[int]:
    length = len(digits)
    res = 0
    for i in range(0,length):
        res = res + digits[i]*(10**(length-i-1))
    res = res + 1
    arr = []
    for i in str(res):
        arr.append(int(i))
    return arr

print(plusOne([1,2,3]))
