#!/usr/bin/python3

from termcolor import colored

class animal:
    def __init__(self,color,age):
        self.color = color
        self.age = age
    
    def run(self):
        print(colored("running....",'green'))
        return

    def eat(self):
        print("eating.......")
        return
    
dog = animal('white', 7)

print(dog.run())