# encoding: utf-8
#@Time : 2021/5/25 0:32
#@Auther : whgvjp
#@File : Testmain.py
class Testmain:
    def suma(self, a:int,b:int) -> int:
        return a+b


if __name__ == '__main__':
    a = Testmain
    b = Testmain.suma(a,1,2)
    print(b)

