import Constant

a = 10

print('Type of a:',type(a))
print('Value of a:',a)
print('Address of a:',id(a))

a = 20

print('Type of a:',type(a))
print('Value of a:',a)
print('Address of a:',id(a))

b = 10.20

c = "Codekul"

d = True

a = 10.20

print('Type of a:',type(a))
print('Value of a:',a)
print('Address of a:',id(a))

print('Type of b:',type(b))
print('Value of b:',b)
print('Address of a:',id(b))

print('Type of c:',type(c))
print('Value of c:',c)
print('Address of a:',id(c))

print('Type of d:',type(d))
print('Value of d:',d)
print('Address of a:',id(d))

Constant.ABCD = 20
Constant.XYZ = 200
Constant.PQR = "The Gurukul For Coders!"

print("ABCD:",Constant.ABCD)
print("XYZ:",Constant.XYZ)
print("PQR:",Constant.PQR)