# Python program to demonstrate
# name mangling


class Student:
    def __init__(self, namex):
        self.__name = namex

    def displayName(self):
        print(self.__name)


s1 = Student("Santhosh")
s1.displayName()


# Raises an error
for name in dir(s1):
    print(name)
