print ("PROGRAM TO CALCULATE THE AVERAGE WEEKLY EXPENSE")
print ("------------------------------------------------------------------")
a = int (input("First Week expense (Rs.) :   "))
b = int (input("Second Week expense (Rs.) :   "))
c = int (input("Third Week expense (Rs.) :   "))
d = int (input("Last Week expense (Rs.) :   "))
M=a+b+c+d
W= M/4
print("Your Total Monthly expense is: ", M, " rupees")
print("Your average weekly is expense: ", W, " rupees")