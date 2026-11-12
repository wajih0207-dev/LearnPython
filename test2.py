class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        print("Hello "+self.name)

p1 = Person("Wa")
p1.greeting()


xx = 0
print(f"x = {xx:.3f}")
