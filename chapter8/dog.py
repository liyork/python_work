class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over")


if __name__ == '__main__':
    my_dog = Dog('willie', 6)
    print(f"my dog's name is {my_dog.name}")
    print(f"my dog's age is {my_dog.age}")
    my_dog.sit()
    my_dog.roll_over()

    print()

    my_dog = Dog('willie1', 11)
    print(f"my dog's name is {my_dog.name}")
    print(f"my dog's age is {my_dog.age}")
    my_dog.sit()
    my_dog.roll_over()
