m=int(input('Enter m='))
n=int(input('Enter n='))
min=m
if min>n:
    min=n
d=min-1
while m%d!=0 or n%d!=0:
    d=d-1
print(f'{d} as the greatest common divisor of {n} and {m}')
