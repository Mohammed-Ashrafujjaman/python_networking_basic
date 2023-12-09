#!/usr/bin/pyhton3

class human:
    def speak(self) -> str:
        # print("speak")
        return "speak"

    def walk(self) -> str:
        # print("walk")
        return "walk"

    def eat(self) -> str:
        # print("eat")
        return "eat"

class german(human):
    def __init__(self,eth="German") -> None:
        self.ethnicity = eth
        print(f"I am {self.ethnicity}")
        print("I can: ")
        

g = german()
print(g.speak())
print(g.eat())
print(g.walk())