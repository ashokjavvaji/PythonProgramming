print('+----------------+')
print('| OOPS IN PYTHON |')
print('+----------------+')

'''
Syntax
class <classname>():
    <statements>
class has class varibales, instance variables and datamembers
constructor
def __init__(self,<args>):
    self.<attribute>=argument
for all the class methods, if it has to use its own variables, it needs reference of itself and it is 'self'
you can add any number of instance variables just by calling the object.<variable name>=<value>
pass - marks end of the delcaration/block
self is the mandatory argument for all the class methods
'''
print('--- Classes and Inheritance ---')
class Car():
    def __init__(self,model,price):
        self.model=model
        self.price=price
    def hikePrice(self):
        self.price=self.price*1.15

honda=Car('city',800000)

print(honda.__dict__)
print(help(honda))

# SuperCar class inherits the methods of Car.
# This is inheritance in python
class SuperCar(Car):
    pass

tata=SuperCar('Nexon',1200000)
print(tata.__dict__)
print(help(tata))#shows the tree of the object

print('--adding additional attibs--')
tata.rating='A+'
tata.hikePrice()
print(tata.__dict__)

#Abstract classes
# Abstract classes
from abc import ABC, abstractmethod
#abc - package for Abstract classes and their implementation
#ABC - Abstract Base Classes - this is the base/parent for all the classes
#      that want to have abstract methods
#abstractmethod - annotation for declaring a method as abstract

print('--Abstract classes--')
class Parent(ABC):
    def method1(self):
        print('In Method#1 of Parent')
    @abstractmethod
    def method2(self):
        pass#pass -> empty definition
    pass
class Child(Parent):
    def method2(self):
        print('In Method#2 in Child')
        pass
    pass
ch=Child()
ch.method1()
ch.method2()
