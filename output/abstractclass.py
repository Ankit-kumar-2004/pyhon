from abc import ABC,abstractclassmethod
class Car(ABC):
    def show(self):
        print("every car has four wheels")
        @abstractclassmethod
        def speed(self):
            pass

class Maruti(Car):
    def speed(self):
        print("speed is 100km/h")

class suzuki(Maruti):
    def speed(self):
        print("speed is 70km/h")

obj=Maruti()
obj.show()
obj.speed()



                        