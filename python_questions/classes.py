
'''
  Basic structure of Python classes, properties, method overrides, calling base class members
'''

class MyClass:
    # class variable -> same for all instances
    x = [1, 2, 3]

    def __init__(self, new_name='banana'):
        self.name = new_name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f'name is {self.name}'

    # self.__name is totally encapsulated
    # outside callers use property name getter/setter
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def foo(self, some_str):
        print(f'MyClass {some_str}')


class MySubClass(MyClass):

    def __init__(self, new_name='bar'):
        # older syntax way of doing it...
        # MyClass.__init__(self, new_name)
        # new Python3 method: super()
        super().__init__(new_name)

    def foo(self, some_str):
        # MyClass.foo(self, some_str)
        super().foo(some_str)
        print(f'MySubClass {some_str}')


class MySubSubClass(MySubClass):

    def __init__(self, new_name='car'):
        # MySubClass.__init__(self, new_name)
        super().__init__(new_name)

    # you will get a warning about changing the method signature but it still works
    # if you add a variable and specify the default value that warning goes away
    def foo(self, some_str, some_other_str=None):
        # MySubClass.foo(self, some_str)
        super().foo(some_str)
        print(f'MySubSubClass {some_str} and {some_other_str}')


myClassInst = MyClass('apple')
print(f'myClassInst is {myClassInst}')

myClassInst2 = MySubClass()
print(f'myClassInst2 is {myClassInst2}')

myClassInst3 = MySubSubClass()
print(f'myClassInst3 is {myClassInst3}')

print(f'type is: {type(myClassInst)}')
print(f'id is: {id(myClassInst)}')
print(f'hash of string apple is {hash("apple")}')
print(f'hash of myClassInst is {hash(myClassInst)}')

myClassInst.name = 'grapefruit'
print(f'myClassInst is {myClassInst}')

myClassInst.foo('banana split')
myClassInst2.foo('strawberry')

print(f'myClassInst x = {myClassInst.x}')
print(f'myClassInst2 x = {myClassInst2.x}')

myClassInst3.foo('batman', 'robin')

# Multiple Inheritance in Python
class First(object):
    def __init__(self):
        print('first')

class Second(First):
    def __init__(self):
        super().__init__()
        print('second')

class Third(First):
    def __init__(self):
        super().__init__()
        print('third')

class Fourth(Second, Third):
    def __init__(self):
        super().__init__()
        print('fourth and final')

forth = Fourth()




