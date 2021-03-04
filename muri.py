class MyClass:
    x = 5


print(MyClass)
p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        print('__init__() gaigai func is called babe dududude')
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
        print("my god dang age is " + str(self.age))


p1 = Person("Jonia", 55555)
p1.myfunc()
