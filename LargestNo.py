# Write a Python program to get the largest number from a list.

l1 = [23, 54, 654, 25, 9, 502, 45, 62, 879, 29]

largest = l1[0]

for no in l1:
    if no > largest:
        largest = no
    
print("Largest no:", largest)