
str1 = "ABC"
no = None

try:
    no = int(str1)
except:
    print("str1 is not a number")
finally:
    print("It will execute everytime")
print(no)
print(type(no))

f = None
try:
    f = open("xyz.txt", "r")
except Exception as e:
    print(e)

print("This is next task")