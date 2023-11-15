print('Enter an integer from 1 to 100:')
n=0
S=0
max=0
for i in range(1,101) :
    n=int(input('n='))
    if max<n :
        max=n
        S=S+1
print(f'The maximum value found was: {max}')
print(f'The maximum value was updated {S} times')     
        
        