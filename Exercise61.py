S=0
i=0
while True:
    n=int(input('Enter n:'))
    if n==0 and i==0:
        print('Error!')
        break
    if n==0:
        break
    S+=n
    i+=1
if i!=0:
    print('The average of a collection of values entered :',S/i)
