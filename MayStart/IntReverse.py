# encoding: utf-8
#@Time : 2021/5/25 22:57
#@Auther : whgvjp
#@File : IntReverse.py

class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            r  = 0
            while x//10 > 0 :
                y = x%10
                r = (r + y)*10
                x = x//10
            if r+x>2**31-1:
                return 0
            else:
                return r+x
        else:
            x = -1*x
            r = 0
            while x // 10 > 0:
                y = x % 10
                r = (r + y) * 10
                x = x // 10
            if r + x > 2 ** 31:
                return 0
            else:
                return -1*(r + x)

if __name__ == '__main__':
    s = Solution()
    res = Solution.reverse(s,-123)
    print(res)

