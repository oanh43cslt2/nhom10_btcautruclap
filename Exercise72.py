string=str(input('Enter a string:'))
reverse=""
for i in string:
    reverse=i+reverse
if reverse==string:
    print(f'{string} is a Palindrome string')
else:
     print(f'{string} is not a Palindrome string')
