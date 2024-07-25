class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale , Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving through water")


nemo = Fish()
nemo.swim()
nemo.