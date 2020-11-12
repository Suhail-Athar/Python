import os
def sdt():
    g = int (input("""What would you like to calculate:
    Press 1 for Speed
    Press 2 for Distance
    Press 3 for Time
    --     """))
    if g == 1:
        d = int (input('Enter the Distance:  '))
        t = int (input('Enter the Time:  '))
        S = d/t
        print ('The Speed is: ',S)
    elif g == 2:
        s = int (input('Enter the Speed:  '))
        d = int (input('Enter the Distance:  '))
        T = d/s
        print ('The time required is: ',T)
    elif g == 3:
        s = int (input('Enter the Speed:  '))
        t = int (input('Enter the Time:  '))
        D = s * t
        print ('The distance travelled is: ',D)
    else:
        print ('Sorry, Try again')
		
sdt()
print ('----------------------------')
result=input("Would you like to calculate again? [y/n] > ")
if result=='y':
     os.system('python "C:/Users/DEV-OPS/python/SDT.py"')
else:
     print("Terminating the program...")