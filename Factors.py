x=int(input('Enter the number: '))
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:   #To check if remainder is zero
        print(i)
print_factors(x) #Calling the function