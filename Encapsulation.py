class AccessControl:

    __a = 0
    def __init__(self, a):
        self.__a = a

    def __display(self):
        print("a:",self.__a)

    def public_display(self):
        self.__display()

    def set_a(self, a):
        self.__a = a


obj1 = AccessControl(10)
obj1.public_display()

obj1.__a= 100
print(obj1.__a)
obj1.public_display()

obj1.set_a(200)
obj1.public_display()