cost=0
S=0
while True:
    a=input("Enter the guest's age: ")
    if a=="":
        break
    age=int(a)
    if age<=2:
        cost=0
    elif 3<=age<=12:
        cost=14.00
    elif age>=65:
        cost=18.00
    else:
        cost=23.00
    S+=cost
print(f'The admission cost for the group:{S:.2f}')



