so=0
tong=0
while True :
    n=int(input('nhập vào số nguyên:'))
    if n==0 and so==0 :
        print('Lỗi .')
        break
    if n==0 :
        break
    so=so+1
    tong=tong+n   
if so!=0 :
    print(tong/so)