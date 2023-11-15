S=0
while True :
    n=(input('Enter product price:'))
    if n=='':
        break
    intn=int(n)
    S=S+intn
a=S%5
if a<2.5 :
    print(f'Total product amount: {S}, when paying cash: {S-a}')
elif a>2.5 :
    print(f'Total product amount: {S}, when paying cash: {S+(5-a)}')     
    