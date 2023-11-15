print('  ',end="")
for i in range(1,11) :
    print(str(i).rjust(4," "),end="")
print()
a=1
for b in range(1,11):
    print(str(a).rjust(2,' '),end="")
    for c in range(1,11):
            print(str(b*c).rjust(4," "),end="")
    print()
    a=a+1

