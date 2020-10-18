def lettercount():
    word = input('Type any string: ').lower()
    Finder=input ('Write the alphabet you want the count for?    ').lower()

    #Alphabet counter
    count = 0
    for letter in word:
        if letter == Finder:
            count = count + 1
    print('Total number of','"',Finder,'"','count= ', count)

    #Total counter
    tot = 0
    for k in word:
       if (k != " "): #Excluding Space
           tot=tot+1
    print('Total Characters in the given string are - ',tot)

    #Percentage Finder
    Per = round((count/tot)*100,1) #rounding off to 1 digit
    print('Usage of',"'", Finder,"'",'in the given string is -',Per,'%')

lettercount() #calling the function
