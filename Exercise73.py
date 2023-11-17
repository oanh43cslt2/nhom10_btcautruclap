string=input('Enter a string:')
letter=(' ',',','?',';','!','.')
reverse=""
reverse1=''
for i in string:
    if i in letter :
        reverse=i.replace(i,"")+reverse
    else :
        reverse=reverse+i  
print(reverse)            
for n in reverse :
    reverse1=n+reverse1
print(reverse1)     
if reverse==reverse1 :
    print(f'{string} is a Palindrome string')
else:
     print(f'{string} is not a Palindrome string')
