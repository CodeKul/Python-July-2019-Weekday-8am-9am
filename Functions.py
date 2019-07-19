def my_function():
    print("This is my function")

my_function()

def function_with_param(a):
    print("a:",id(a))
    a = "The Gurukul for Coders!"
    print("a:",id(a))
    print(a)

b = "Codekul"
print("b:",id(b))
function_with_param(b)

def change_list(l):
    print("l:",id(l))
    l.append(6)
    print("l:",id(l))
    print(l)

l1 = [1,2,3,4,5]
print("l1:",id(l1))
change_list(l1)
print(l1)

def function_with_default(a, b, param = 100):
    print(a,b,param)

function_with_default(1, 2, 3)

def function_returning():
    return "Python"

str = function_returning()
print(str)

print(function_returning())