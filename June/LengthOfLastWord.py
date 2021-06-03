# encoding: utf-8
#@Time : 2021/6/3 23:06
#@Auther : whgvjp
#@File : LengthOfLastWord.py

def lengthOfLastWord(s: str) -> int:
    arr = s.split(" ")
    str = arr[-1]
    return len(str)

print(lengthOfLastWord("a "))
