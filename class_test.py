# class Root(object):
#     def __init__(self):
#         print('this is root')
#
# class B(Root):
#     def __init__(self):
#         print('this is B')
#         super(B,self).__init__()
#         print('leave B')
#
# class C(Root):
#     def __init__(self):
#         print('this is C')
#         super(C,self).__init__()
#         print('leave C')
#
#
# class D(B,C):
#     pass
#
# d = D()
# print(d.__class__.__mro__)
# print(D.mro())


# class A():
#     def __init__(self):
#         print("进入A…")
#         print("离开A…")
#
#
# class G():
#     def __init__(self):
#         print("进入G…")
#         print("离开G…")
#
#
# class B(A):
#     def __init__(self):
#         print("进入B…")
#         super(C, self).__init__()  # 困惑点：这里为啥先进入C，不应该先进入B，在进入C么
#         print("离开B…")
#
#
# class C(A):
#     def __init__(self):
#         print("进入C…")
#         super(D, self).__init__()
#         print("离开C…")
#
#
# class D(B, C):
#     def __init__(self):
#         print("进入D…")
#         super().__init__()
#         # super(A,self).__init__()
#         print("离开D…")
#
#
# class E(G):
#     def __init__(self):
#         print("进入E…")
#         # super().__init__()
#         # super(B, self).__init__()  # 对继承自父类的属性进行初始化
#         super(E, self).__init__()
#         # 比如这里是先找到B,然后把类B的对象self转化为类B的对象，再由被转化的类B的对象调用__init__()函数
#         print("离开E…")
#
#
# class F(E, D):
#     def __init__(self):
#         print("进入F…")
#         # super().__init__()
#         super(G,self).__init__()
#         print("离开F…")
#
#
#
# print(E.__mro__)
# e = E()
# print(G.__mro__)
# g = G()
# print(F.__mro__)
# d = F()



# class Base:
#     def __init__(self):
#         print('Base.__init__')
#
#
# class A(Base):
#     def __init__(self):
#         super().__init__()
#         print('A.__init__')
#
#
# class B(Base):
#     def __init__(self):
#         super().__init__()
#         print('B.__init__')
#
#
# class C(Base):
#     def __init__(self):
#         super().__init__()
#         print('C.__init__')
#
#
# class D(A, B, C):
#     def __init__(self):
#         super(B, D).__init__(self)  # D是B的子类，并且需要传递一个参数
#         print('D.__init__')
#
#
# d = D()
#
# print(D.mro())


class Base:
    def __init__(self):
        print(self.__class__.__mro__)
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print(self.__class__.__mro__)
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print(self.__class__.__mro__)
        print('B.__init__')


class C(A, B):
    def __init__(self):
        print(super())
        super().__init__()
        print(super())
        print('C.__init__')

class D(B):
    def __init__(self):
        # print(super())
        super().__init__()
        print(super())
        print('D.__init__')


d = D()
print(d.__class__.mro())

print('\n\n\n\n')


c = C()
print(C.mro())