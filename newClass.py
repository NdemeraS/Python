import random

class Greeter(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello " + self.name)

    def bye(self):
        print("Bye " + self.name)


g = Greeter("Jess")
g.hello()
g.bye()