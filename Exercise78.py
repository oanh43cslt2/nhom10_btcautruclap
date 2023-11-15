p=int(input('Enter Decimal number is : '))
result=""
while p>=0 :
    S=p%2
    result=str(S)+result
    p=p//2
    if p==0:
        S=p%2
        result=str(S)+result
        p=p//2
        break
print(f'Binary number is: {result}')      

      