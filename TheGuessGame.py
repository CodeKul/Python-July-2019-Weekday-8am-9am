import random

while True:
    n1 = int(input("Enter number between 1-10: "))
    n2 = random.randint(1,10)

    if n1 == 0:
        break
    elif n1 > 10:
        print("Enter valid number")
        continue
        
    if n1 == n2:
        print("Winner winner chicken dinner")
    else:
        print("Better luck next time")