# String

s1 = 'Codekul'
print(type(s1))
print(s1)
s2 = "The Gurukul for Coders!"
print(type(s2))
print(s2)
# "Codekul" - 'The Gurukul for Coders'!

print("%s - %s" %(s1,s2))
print("{} - {}".format(s1, s2))
print('''"Codekul" - 'The Gurukul for Coders'!''')
s3 = '''Codekul
    - The Gurukul
        for Coders!'''
print(s3)

s4 = s3.upper()
print(s4)


# List

l1 = [1,2,3,4,5, 'Six', 7.8, True]
l1.insert(0, 20)
l1.append('Ten')
l1.remove(2)
print(l1)


l2 = ['One', l1, ['Red', 'Green', 'Blue']]
print(l2[2])

print(l1.count(2))



# Dictionary

d1 = {'Key1': 'Value1', 'Key2': 'Value2'}
print(d1['Key2'])

d2 = {1: 'One', 2: 'Two', 3: 'Three', 'Four': 4, 'd1': d1}
print(d2['d1'])


# Tuple

t1 = (1,2,3, "four", 7.8, False)
# t1.append(30)
print(t1[5])


