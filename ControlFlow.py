'''
    if condition:
        true statements
    else:
        false statements
'''

a = 30
b = 20

# if a != 10:
#     print("Codekul")
#     print("The Gurukul for Coders!")
# else:
#     print("Python-July-2019-Weekday-8am-9am")

# if a < b:
#     print("a is less than b")
# else:
#     if a == b:
#         print("a and b are equal")
#     else:
#         print("a is greater than b")

if a < b:
    print("a is less than b")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# Loops

'''
    initialisation
    while condition:
        statements
        incr/decr
'''

i = 0

while i < 10:
    if i % 2 == 0:
        print("Codekul")
    else:
        print("The Gurukul for Coders!")
    i += 1

s1 = [1,2,3,4,5,6,7,8,9]
i = 0
while i < 9:
    print("Value of s1[i]:",s1[i])
    i += 1

print(i)

'''
for item in collection:
    statements
'''

s2 = "This is another statement"
for num in s2:
    print(num)
