class A:
    def hello(self):
        print("Hello from A")

class B(A):
    print("hello from b")

obj = B()
obj.hello()