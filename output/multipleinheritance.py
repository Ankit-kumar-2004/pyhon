class A:
    def method1(self):
        print("A")

class B:
    def method2(self):
        print("B")

class C(A, B):
    pass

obj = C()
obj.method1()
obj.method2()