alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
beta='DEFGHIJKLMNOPQRSTUVWXYZABC'
Pass=input('Message from Mr. Ceaser: ')
PASS=Pass.upper()
a=1
result=''
n=0
while a<=len(Pass) :
    if (PASS[a-1]) in alpha :
        S=beta[alpha.find(PASS[a-1])]
        n=n+1
    else:
        S=PASS[a-1]
    result=result+S
    a=a+1
print('The message has been translated:', result) 
print('Number of letters translated',n)           
    
        
    
    

