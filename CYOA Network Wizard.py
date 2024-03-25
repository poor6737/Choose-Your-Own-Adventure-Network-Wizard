#Choose your own Adventure IT Edition! 

#Idea from Tik Tok. use the def function to first create each "page" then just reference the "page" function 
#to reduce the amount of repetition. 

import os
import sys

# Clear the screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Now, to clear the screen:
cls()

print('Choose Your Own Adventure')
print('Network Wizard Edition')
print(' ')
input('Press Any Key to Continue...')

cls()

def one():
    
    cls()
   
    print('Need Additional Ports (Go to Page 5)')
    print('Printer Trouble (Go to Page 3)')
    print('Wireless Issues (Go to Page 4)')
    print('Tech Bridge P2 (Go to Page 7)')
    print(' ')
    page=input("Enter Page Number: ")

    cls()

    if page == "5":
        five()
    if page == "3":
        three()
    if page == "4":
        four()
    if page == "7":
        seven()

def three():
    
    cls()
    
    print('You arrive to find that you are up against an evil dragon guarding the printer')
    print('Do you?')
    print(' ')
    print('Stay and fix the printer (Go to Page 12)')
    print('Run Away (Go to Page 8)')
    print(' ')
    page=input("Enter Page Number: ")

    if page == "12":
        twelve()
    if page == "8":
        eight()

def four():

    cls()

    print('You arrive and use your network magic to install a new Access Point')
    print('Proceed to Page 11')
    print(' ')
    input("Press any Key to Continue...")

    eleven()

def five():
    print('You harness your telekenesis powers and proceed to rack the massice Chassis switch')
    print('')
    print('Proceed to Page 9')
    print('')
    input("Press any Key to Continue...")

    cls()

    nine()

def six():

    cls()

    print('You arrive and are greeted by an evil SysAdmin who has been powering off servers with no Change Record')
    print('Proceed to Page 10')
    print(' ')
    page=input("Press any Key to Continue...")

    ten()

def seven():

    cls()

    print('You join the Teams call and spend 8 hours on it to find out it was not the network')
    print('You have exhausted yourself, return to Page 1')
    print(' ')
    page=input("Press any Key to Continue...")

    one()

def eight():

    cls()

    print('You flee the dragon and the printer issue, you live to fight another day')
    print('Nobody likes printers anyway')
    print(' ')
    print('Handle Another Incident (Go to Page 1)')
    print('End your day (Go to Page 14)')
    print(' ')
    page=input("Enter Page Number: ")

    if page == "1":
        one()
    if page == "14":
        fourteen()

def nine():

    cls()

    print('You relax with the switch installed and port capacity increased, a job well done')
    print(' ')
    print('Handle another incident (Go to Page 1)')
    print('End your day (Go to Page 14)')
    print(' ')
    page=input("Enter Page Number: ")

    if page == "1":
        one()
    if page == "14":
        fourteen()

def ten():

    cls()

    print('You and the SysAdmin begin to battle it out with spells')
    print('You are both pushed to your limites')
    print(' ')
    print('Proceed to Page 13')
    print(' ')
    input("Press any Key to Continue...")

    thirteen()

def eleven():

    cls()

    print('You are a hero!')
    print('Bringing the SSIDs and connectivity to the masses')
    print('A job well done')
    print(' ')
    print('Handle another incident (Go to Page 1)')
    print('End your day (Go to Page 14)')
    print(' ')
    page=input("Enter Page Number: ")

    if page == "1":
        one()
    if page == "14":
        fourteen()

def twelve():

    cls()

    print('You foolishly stay and try to fix the printer')
    print('The dragon burns you and the printer to ash')
    print(' ')
    choice=input("You have lost. Try again? ")
    
    lower=choice.lower()

    if lower == "yes":
        one()
    if lower == "no":
       
        cls()
       
        sys.exit()

def thirteen():

    cls()

    print('You triumph over the SysAdmin')
    print('You have saved the Data Center from this rogue menace')
    print(' ')
    print('Handle another incident (Go to Page 1)')
    print('End your day (Go to Page 14)')
    print(' ')
    page=input("Enter Page Number: ")

    if page == "1":
        one()
    if page == "14":
        fourteen()

def fourteen():
    print('You have ended your day')
    print('Ever watchful of your Network')
    print(' ')
    print('Perhaps more adventures await you in the future?')
    input(" ")

    cls()
    sys.exit

one()
