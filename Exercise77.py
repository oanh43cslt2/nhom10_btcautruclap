base2=input('Enter Binary number:')
a=len(base2)-1
Sum=0
b=0
while a>0 :
    c=(int(base2[b])) * (2**a) 
    Sum=Sum+c
    a=a-1
    b=b+1
print(f'Decimal number is {Sum}')    
    
    
    
    
