# encoding: utf-8
#@Time : 2021/6/5 20:37
#@Auther : whgvjp
#@File : MySqrt.py

def mySqrt(x: int) -> int:
    l, r, ans = 0, x, -1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans
