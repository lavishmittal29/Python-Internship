class Animal:
    def sound(self):
        print("Animal makes Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Bark")

class Cat(Animal):
    def sound(self):
        print("Cat Meows")


dog1=Dog()
cat1=Cat()

dog1.sound()
cat1.sound()