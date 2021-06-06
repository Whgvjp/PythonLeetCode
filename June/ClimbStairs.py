# encoding: utf-8
#@Time : 2021/6/6 22:02
#@Auther : whgvjp
#@File : ClimbStairs.py

def climbStairs(n: int) -> int:
    a, b, r = 0, 1, 1
    for i in range(n):
        r = a + b
        a = b
        b = r
    return r

print(climbStairs(5))
