def swap(a, b):
    c = a
    a = b
    b = c
    return (a, b)

# print(a, b)

x = 10
y = 20

print(swap(x, y))

def change_list_data(l):
    l.append([6,7,8,9,0])
    print(l)

l = [1,2,3,4,5]
change_list_data(l)
print(l)
