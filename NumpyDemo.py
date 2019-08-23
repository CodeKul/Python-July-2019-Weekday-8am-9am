import numpy as np

a = np.arange(9).reshape(3, 3)

print(a)

b = np.array( [[10,20,30], [40, 50, 60], [70, 80, 90]] )

print(b)

ab = a / b

print(ab)

c = np.array( [ [1,2], [3,4] ], dtype=complex )

print(c)
