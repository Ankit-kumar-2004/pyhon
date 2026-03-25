class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stoped")

class toyotacar(car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()

car1=toyotacar("parius","electric")
print(car1.type)