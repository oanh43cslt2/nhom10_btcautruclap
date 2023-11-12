print('_______________________')
print('| Celsius | Fahrenheit|')
print('|_________|___________|')
for i in range (0,101,10):
    a=str(i)
    f=i*9/5+32
    b=str(f)
    if len(a)==1:
        print (f'|   {i}     |   {f}    |')
    elif len(a)==2 and len(b)==4:
        print (f'|   {i}    |   {f}    |')
    elif len(a)==2 and len(b)==5:
        print (f'|   {i}    |   {f}   |')
    elif len(a)==3:
        print (f'|   {i}   |   {f}   |')
print('|_________|___________|')
