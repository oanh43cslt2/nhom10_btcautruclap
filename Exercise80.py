import random 
max=0
min=float('inf')
result=0
for i in range(1,11) :
    H=0
    T=0
    Time=0     
    while True :
        val=random.choice('HT')
        if val=='H' :
            print(val,end=" ")
            H=H+1
            T=0
        elif val=="T":
            T=T+1
            print(val,end=" ")
            H=0
        Time+=1    
        if T==3 or H==3 :
            break
    result+=Time    
    print(f'({Time} flips)')
    if max<Time :
        max=Time
    if min>Time :
        min=Time     
print('Min value:', min)
print('Max value:', max)
print( 'Mean value:', result/10)
