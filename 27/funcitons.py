def sumi(*args):
    print(sum(args))


sumi(3,5,6,5,4)

def calculate(**kwargs):
    print(int(kwargs["add"]) * int(kwargs["multupli"]))


calculate(add=3, multupli=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="nissan", model="GTR")
print(my_car)
