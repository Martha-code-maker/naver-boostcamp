class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Korean(Person):
    pass

first_korea = Korean("YUjin", 25)
print(first_korea.name)