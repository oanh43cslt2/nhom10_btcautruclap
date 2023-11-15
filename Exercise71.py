from math import  *
x=int(input('Enter x ='))
guess=x/2
while fabs(guess*guess-x)>=pow(10,-12):
    guess=guess+(x/guess-guess)/2
print('The square root of x is :',guess)
