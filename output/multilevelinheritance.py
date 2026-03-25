class A:
    def show_A(self):
        print("Class A")

class B(A):
    def show_B(self):
        print("Class B")

class C(B):
    def show_C(self):
        print("Class C")

obj = C()

obj.show_A()   
obj.show_B()   
obj.show_C()  