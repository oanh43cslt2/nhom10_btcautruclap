import math
a=float(input('Enter the x part of the coordinate:'))
b=float(input('Enter the y part of the coordinate:'))
chuvi=0
S=0
while True :
    x=(input('Enter the x part of the coordinate:(blank to quit)'))
    if x=='':
        S=math.sqrt((preX-a)**2+(preY-b)**2)
        chuvi=chuvi + S
        break
    y=(input('Enter the y part of the coordinate:'))
    if chuvi==0 :
        S=math.sqrt((float(x)-a)**2+(float(y)-b)**2)
    elif chuvi!=0 :
        S=math.sqrt((preX-float(x))**2+(preY-float(y))**2)
    preX=float(x)
    preY=float(y) 
    chuvi=chuvi + S   
print(f'The perimeter of that polygon is {chuvi}')    

    