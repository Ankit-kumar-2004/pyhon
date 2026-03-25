
class person:
    __name = "anonymous"

    def __hello(self):
        print("hello")

    def welcome(self):
        self.__hello()

p1 = person()
p1.welcome()