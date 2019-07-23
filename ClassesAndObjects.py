class MyClass:
    my_var = 0
    def __init__(self):
        print("__init__")
        self.my_var = 20

    def member_function(self):
        print("member_function")

    def display(self):
        print("Value of my_var:",self.my_var)

myObj = MyClass()
# myObj.member_function()
myObj.my_var = 10
# print(myObj.my_var)
myObj.display()

myAnotherObj = MyClass()
myAnotherObj.my_var = 30
myAnotherObj.display()

myObj.display()
myAnotherObj.display()

print(id(myObj))
print(id(myAnotherObj))

print(id(myObj.my_var))
print(id(myAnotherObj.my_var))

