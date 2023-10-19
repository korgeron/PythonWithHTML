class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def say_hello(self):
        print(self.name + " wants to say HELLO!!!")
