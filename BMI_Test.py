print ('🔴 Calculation of BMI as per WHO recommendation 🔵')
def suhail():
    print('(❎ To terminate press Ctrl + C) | ⚡ Ⓒ Suhail Athar ⚡')
    print ('----------------------------')
    w = float ( input ('✔ Your weight(in kg):  ') )
    h = float ( input ('✔ Your height(in cm):  ') )
    B = float(w * 10000)/(h ** 2)
    B= int (B)
    print ('✦ Your Body Mass Index is', B)
    if (B >=18 and B<=25):
        print ('🔵 You are in healthy range ❤')
    elif (B >25 and B<=30):
        print ('🔴 You are Overweight')
    elif (B >30 and B<=35):
        print ('🔴 You are in Obese Class I')
    elif (B >35 and B<=40):
        print ('🔴 You are in Obese Class II')
    elif (B >40 and B<=45):
        print ('🔴 You are in Obese Class III')
    elif(B >=16 and B<18):
        print ('🍗🧷 You are thin')
    else:
        print ('Are you alive?')
    print ('----------------------------')

while True:
    suhail ()