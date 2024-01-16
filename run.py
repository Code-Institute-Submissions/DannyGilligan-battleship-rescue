# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high



########## Imports ##########
import os
import sys
import time
from time import sleep


# Stores a valid username
username = None

# Stores the mission difficulty
mission_difficulty = None

# Stores the different difficulty levels
difficulty_levels = ['cadet', 'captain', 'admiral']

# Stores whether the mission was accepted
mission_acceptance = None

# Stores the valid options to accept or reject mission
mission_accept_options = ['y', 'n'] 


def typing_effect(text, speed):   
    words = text
    for char in words:
        time.sleep(speed) #amended to make speed a parameter
        sys.stdout.write(char)
        sys.stdout.flush()


def clearscreen():                                    
    """
    The clearscreen function will clear any 
    content from the current screen
    displayed to the user.
    """
    os.system('cls' if os.name=='nt' else 'clear')


def validate_username_screen():
    """
    The validate_username function will strip any 
    leading or trailing whitespaces from the
    username input variable, the value will then be checked
    to ensure it is more than 2
    characters and less than 15.
    """

    global username
    username = username.strip()


    """
    # While loop is used to perform validation on the username input,
    # must be greater than 2 characters and less than 15. The while 
    # loop will display an alert message until the parameters are satisfied.
    """
    while len(username) < 2 or len(username) > 15:
        clearscreen() # Screen is cleared
        print(banner_art) 
        username = input('\n\n           \033[33mAlert!!' + \
        '\033[0m Enter a valid'\
        + ' callsign between 2 and 15' + \
        ' characters\n\n                                   ')
        username = username.strip() # Strip method is used
    clearscreen() # Screen is cleared 



def mission_difficulty_screen():
    """
    The mission_difficulty_screen will 
    display the screen where the user
    can enter their desired difficulty level.
    The options available, are Cadet (easy),
    Captain (normal) and Admiral (hard). 
    A while loop performs validation on the user
    input, and compares their input against the 
    values held in the difficulty_levels
    variable.
    """
    print(banner_art) # Prints the banner art on the screen
    global mission_difficulty
    global mission_acceptance
    mission_difficulty = input(('\n\n               Enter Mission Diffic') + \
    ('ulty (Cadet, Captain, Admiral) \n\n                                   '))
    mission_difficulty = mission_difficulty.lower()

    while mission_difficulty not in difficulty_levels:
        clearscreen()
        print(banner_art)
        mission_difficulty = input('\n\n       \033[33mAlert!!\033[0m ' + \
        'Enter Mission Difficulty (Cadet, Captain,' + \
        ' Admiral) \n\n                                   ')
        mission_difficulty = mission_difficulty.lower()
    clearscreen()






banner_art_upper = ('''
             ___   ___  ______ ______ __    ____ ____ __ __ ____ ___   
            / _ ) / _ |/_  __//_  __// /   / __// __// // //  _// _ \ 
           / _  |/ __ | / /    / /  / /__ / _/ _\ \ / _  /_/ / / ___/
          /____//_/ |_|/_/    /_/  /____//___//___//_//_//___//_/    
''')

banner_art_lower = ('''
                         ___   ____ ____ _____ __  __ ____
                        / _ \ / __// __// ___// / / // __/
                       / , _// _/ _\ \ / /__ / /_/ // _/ 
                      /_/|_|/___//___/ \___/ \____//___/
''')

banner_art = ('''
             ___   ___  ______ ______ __    ____ ____ __ __ ____ ___   
            / _ ) / _ |/_  __//_  __// /   / __// __// // //  _// _ \ 
           / _  |/ __ | / /    / /  / /__ / _/ _\ \ / _  /_/ / / ___/
          /____//_/ |_|/_/    /_/  /____//___//___//_//_//___//_/    

\033[36m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m
\033[36m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m
\033[36m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m
                         ___   ____ ____ _____ __  __ ____
                        / _ \ / __// __// ___// / / // __/
                       / , _// _/ _\ \ / /__ / /_/ // _/ 
                      /_/|_|/___//___/ \___/ \____//___/

''')





sleep(0.4)
print(banner_art_upper) # Prints 'Battleship' to screen

typing_effect\
('\033[36m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m\n', 0.005)
#sleep(0.1)
typing_effect\
('\033[36m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m\n', 0.005)
#sleep(0.1)
typing_effect\
('\033[36m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m', 0.005)

print(banner_art_lower) # Prints 'Rescue' to screen

# Effects to be used for shot confirmations
#typing_effect('\n\n\n\033[36m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', 0.005)
#print('\033[41m\033[37m\033[1m      BATTLESHIP HIT     \033[0m\033[22m')
#print('\033[42m\033[30m\033[1m ENEMY SHIP NEUTRALISED  \033[0m\033[22m')
#print('\033[47m\033[30m\033[1m      TARGET MISSED      \033[0m\033[22m')
#print('\033[47m\033[31m\033[1m MERCHANT SHIP DESTROYED \033[0m\033[22m')








