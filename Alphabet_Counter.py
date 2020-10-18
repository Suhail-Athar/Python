def lettercount():
    word = input('Type any string: ').lower()
    Finder=input ('Write the alphabet you want the count for?    ').lower()

    #Alphabet counter
    x = word.count(Finder) #using count method
    print('Total number of','"',Finder,'"','=', x)

    #Total counter
    total = len(word) - word.count(" ") #Excluding Spaces
    print('Total Characters in the given string =',total)

    #Percentage Finder
    Per = round((x/total)*100,1) #rounding off to 1 digit
    print('Usage of',"'", Finder,"'",'in the given string is -',Per,'%')

lettercount() #calling the function
