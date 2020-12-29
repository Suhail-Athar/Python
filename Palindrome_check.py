# Python program to check if a string is palindrome or not
 
x = input('Enter any string: ')
 
w = ""
for i in x:
    w = i + w
 
if (x == w):
    print("Yes",x,'is a Palindrome String')
else:
    print("No",x,'is not a Palindrome String')