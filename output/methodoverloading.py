class A:
    def show(self):
        print("welcome")

    def show(self,firstname=""):
        print("welcome",firstname)

    def show(self,firstname="",lastname=""):
        print("welcome",firstname,lastname)

obj=A()
obj.show()
obj.show("Ankit")
obj.show("Ankit","kumar")
