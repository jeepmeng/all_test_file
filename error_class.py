# import abc
from pprint import pprint
from abc import ABC, abstractmethod

class A(ABC):
    def __init__(self,*args):
        print('hhhhh')
        # self.a = funcK(args)
        pass
    # def funcA(self,*args):
    #     c = self.funcK(args)
    #     return c
    @abstractmethod
    def funcK(self):
        pass

class B(A):

    def __init__(self):
        # super().__init__()
        pass
    def funcK(self,*args):
        return args

a = A()
# # print(a.funcA(15))
# pprint(dir(a)[-1])
# print(a.__dict__)
b = B()
print(b.funcK(15))
# print(a.funcA(15))
# pprint(dir(b))