pi=3
for i in range (2,32,2):
    if i%4==0:
        pi-=4/(i*(i+1)*(i+2))
    else:
        pi+=4/(i*(i+1)*(i+2))
print(pi)
