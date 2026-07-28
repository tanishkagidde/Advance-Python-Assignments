from abc import ABC, abstractmethod

# SINGLETON PATTERN

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Singleton Instance...")
            cls._instance = super().__new__(cls)
        return cls._instance

print("======== SINGLETON PATTERN ========")
obj1 = Singleton()
obj2 = Singleton()
print("Both objects are same:", obj1 is obj2)

#FACTORY PATTERN

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        return "Woof...Woof"

class Cat(Animal):

    def speak(self):
        return "Meow...Meow"

class AnimalFactory:

    @staticmethod
    def get_animal(name):
        if name.lower() == "dog":
            return Dog()
        elif name.lower() == "cat":
            return Cat()
        else:
            return None

print("========FACTORY PATTERN========")
animal = AnimalFactory.get_animal("dog")
print("Dog:", animal.speak())

animal = AnimalFactory.get_animal("cat")
print("Cat:", animal.speak())

# OBSERVER PATTERN

class Observer:

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received: {message}")

class Subject:

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

print("======== OBSERVER PATTERN ========")
subject = Subject()

o1 = Observer("Tanishka")
o2 = Observer("Aarav")

subject.attach(o1)
subject.attach(o2)

subject.notify("New Notification!")

# STRATEGY PATTERN

class Strategy(ABC):

    @abstractmethod
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):

    def execute(self, a, b):
        return a + b

class SubtractStrategy(Strategy):

    def execute(self, a, b):
        return a - b

class MultiplyStrategy(Strategy):

    def execute(self, a, b):
        return a * b

class Context:

    def __init__(self, strategy):
        self.strategy = strategy

    def perform(self, a, b):
        return self.strategy.execute(a, b)

print("======== STRATEGY PATTERN ========")

context = Context(AddStrategy())
print("Addition:", context.perform(5, 2))

context = Context(SubtractStrategy())
print("Subtraction:", context.perform(5, 2))

context = Context(MultiplyStrategy())
print("Multiplication:", context.perform(5, 2))

#OUTPUT
'''
======== SINGLETON PATTERN ========
Creating Singleton Instance...
Both objects are same: True
========FACTORY PATTERN========
Dog: Woof...Woof
Cat: Meow...Meow
======== OBSERVER PATTERN ========
Tanishka received: New Notification!
Aarav received: New Notification!
======== STRATEGY PATTERN ========
Addition: 7
Subtraction: 3
Multiplication: 10
'''
