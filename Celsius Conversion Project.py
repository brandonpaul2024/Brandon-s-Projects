# This is some Python pratice, this particular code will help convert Celsius to Fahrenheit and vice versa.
roundnumber = 0
celsius = 0
fahrenheit = 9.0/5.0 * celsius + 32 

def main (roundnumber, celsius):
    print ("Here is a basic conversion chart for Celsius to Fahrenheit.")
    while (roundnumber != 10):
        roundnumber = roundnumber + 1
        while (celsius <= 90):
            celsius = celsius + 10
            fahrenheit = 9.0/5.0 * celsius + 32 
            print (celsius, "Celsius =", fahrenheit, "Fahrenheit")

def usercalc(celsius, fahrenheit):
    conversionNeeded = int(input("Do you want to convert a Celsius to Fahrenheit? (1 = Yes or 2 = No)\n"))
    if conversionNeeded == 1:
        celsius = int(input("Enter the celsius you need converting to fahrenheit:\n" ))
        fahrenheit = 9.0/5.0 * celsius + 32
        print ("The Celsius you entered is", celsius, "that converted to fahrenheit is", fahrenheit)
        fahrenheitmanual (fahrenheit, celsius)
    elif conversionNeeded == 2:
        fahrenheitmanual (fahrenheit, celsius)
    else:
       print ("Unknown answer, please try again. (1 = Yes or 2 = No)")
       usercalc (celsius, fahrenheit)
    
def fahrenheitmanual (fahrenheit, celsius):
    fahrenheitConversion = int(input("Do you want to convert a Fahrenheit number to Celsuis? (1 = Yes or 2 = No)\n"))
    if fahrenheitConversion == 1:
       fahrenheitinput = int(input("Enter the Fahrenheit you want converted to Celsius:\n"))
       celsius = (fahrenheitinput - 32) * 5/9
       print("The Fahrenheit you entered is", fahrenheitinput, "that converted to Celsius is", celsius)
       ending ()
    elif fahrenheitConversion == 2:
        ending ()
    else:
        ending ()
        
def ending ():
    moreconv = int(input("Do you want to do more conversions? (1 = Yes or 2 = No)\n"))
    if moreconv == 1:
        usercalc(celsius, fahrenheit)
    elif moreconv == 2:
        print ("Have a nice rest of your day!")
    else:
        print ("Unknown answer try again.")
        ending ()
        
        
main (roundnumber, celsius,)
usercalc (celsius, fahrenheit)