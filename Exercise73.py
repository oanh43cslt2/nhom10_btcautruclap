string=str(input('Enter a string:'))
a=string.rstrip(".,?!:;")
b=a.lower()
c=b.replace(" ", "")
reverse=""
for i in c:
    reverse=i+reverse
print(reverse)
if reverse==c:
    print(f'{string} is a palindrome string')
else:
     print(f'{string} is not a palindrome string')
