class car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stoped")

class toyotacar(car):
    def __init__(self,name):
        self.name=name

car1=toyotacar("fortuner")
car2=toyotacar("hyundai")
print(car1.name)
print(car2.name)
print(car2.start())
print(car1.stop())