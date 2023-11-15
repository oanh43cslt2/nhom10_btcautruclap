string=str(input('Enter a string:'))
reverse=""
for i in string:
    reverse=i+reverse
if reverse==string:
    print(f'{reverse} is a palindrome string')
else:
     print(f'{reverse} is not a palindrome string')
