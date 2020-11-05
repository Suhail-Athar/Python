print ('🔴 Calculation of BMI as per WHO recommendation 🔵')
def suhail():
    print('(❎ To terminate press Ctrl + C) | ⚡ Ⓒ Suhail Athar ⚡')
    print ('----------------------------')
    w = float ( input ('✔ Your weight(in kg):  ') )
    h = float ( input ('✔ Your height(in cm):  ') )
    B = (w * 10000)/(h ** 2)
    B= int (B)
    print ('✦ Your Body Mass Index is', B)
    if B in range(18, 25):
        print ('🔵 You are in healthy range ❤')
    elif B in range(26, 30):
        print ('🔴 You are Overweight')
    elif B in range(31, 35):
        print ('🔴 You are in Obese Class I')
    elif B in range(36, 40):
        print ('🔴 You are in Obese Class II')
    elif B in range(41, 45):
        print ('🔴 You are in Obese Class III')
    else:
        print ('Are you alive?')
    print ('----------------------------')

while True:
    suhail ()
