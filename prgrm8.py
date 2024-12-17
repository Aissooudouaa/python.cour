import math

number=int(input("please enter an integer number: "))
if number<0:
    print("invalid number")
elif number>0:
    print(math.sqrt(number))

while True:
    nbr=int(input('enter another number: '))
    if nbr==0:
        break

