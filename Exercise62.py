price={4.95,9.95,14.95,19.95,24.95}
print('Discount table'.center(49, '_'))
print(f'★ OriginalPrice  | Price    | The discount amount')
for i in price :
    a=str(i)
    if len(a)==5 :
        print(f'★ ${(2.5*i):.2f}         | ${i}   | ${(i*0.6):.2f}')
    elif len(a)==4 :   
        print(f'★ ${(2.5*i):.2f}         | ${i}    | ${(i*0.6):.2f}')
    
    