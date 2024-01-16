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



def mission_accept_screen():
    clearscreen()
    time.sleep(.4)
    print('\033[33m*******************************|Battleship Comms|*******************************\033[0m')
    print(''' \n\n\n\n\n\n\n\n\n\n                   Requesting connection with Central Command.''')
    time.sleep(1)
    clearscreen()
    print('\033[33m*******************************|Battleship Comms|*******************************\033[0m')
    print(''' \n\n\n\n\n\n\n\n\n\n                   Requesting connection with Central Command..''')
    time.sleep(.4)
    clearscreen()
    print('\033[33m*******************************|Battleship Comms|*******************************\033[0m')
    print(''' \n\n\n\n\n\n\n\n\n\n                   Requesting connection with Central Command...''')
    time.sleep(.4)
    clearscreen()
    print('\033[33m*******************************|Battleship Comms|*******************************\033[0m')
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing secure connection with Central Command....''')
    time.sleep(.4)
    clearscreen()
    print('\033[33m*******************************|Battleship Comms|*******************************\033[0m')
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing secure connection with Central Command.....''')
    time.sleep(.4)
    clearscreen()
    print('\033[33m*******************************|Battleship Comms|*******************************\033[0m')
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing secure connection with Central Command......''')
    time.sleep(.4)
    clearscreen()
    print('\033[33m*******************************|Battleship Comms|*******************************\033[0m')
    print(''' \n\n\n\n\n\n\n\n\n\n                          \033[32mSecure connection successful.\033[0m''')
    time.sleep(1)
    clearscreen()
    print('\033[33m*******************************|Battleship Comms|*******************************\033[0m')
    message1 = (f''' \n\n\n\n\n\n\n\n\n\n                \033[36mURGENT\033[0m Incoming''')
    message2 = (f''' Message: For {username.capitalize()}'s Eyes Only''')
    print(message1 + message2)
    time.sleep(1.5)
    clearscreen()
    typing_effect(f'''
    {mission_difficulty.capitalize()},\n 
    It is with great regret that I must inform you that the situation 
    has become dire. Our forces are being routed in every theatre 
    and on every front, our supply chains have been decimated and our 
    ability to sustain a defence against this onslaught can be measured 
    now in hours.\n
    Your mission is to intercept and eliminate a fleet of 5 enemy 
    Destroyers that are currently in pursuit of 2 friendly Merchant 
    ships sailing for our Capital Port. These Merchant ships are on a 
    clandestine mission to deliver classified cargo that will turn the 
    tide of this war once and for all!\n
    Unfortunately, during a recent skirmish, the Merchant ships lost all 
    communication capabilities and the Enemy's radar jamming technology 
    is preventing us from locating them. But we know they're out there, 
    somewhere. Hunt down the enemy with extreme prejudice, avoid 
    friendly fire at all costs and rescue those Merchant ships.\n
    Losing that cargo, means losing the war!\n''',0.03)
    sleep(0.5)
    mission_acceptance = input('\n                         Accept' + \
    ' Mission? (Y / N)\n\n                                   ') 
    mission_acceptance = mission_acceptance.lower()

    while mission_acceptance not in mission_accept_options:
        clearscreen()
        print(f'''
    {mission_difficulty.capitalize()},\n 
    It is with great regret that I must inform you that the situation 
    has become dire. Our forces are being routed in every theatre 
    and on every front, our supply chains have been decimated and our 
    ability to sustain a defence against this onslaught can be measured 
    now in hours.\n
    Your mission is to intercept and eliminate a fleet of 5 enemy 
    Destroyers that are currently in pursuit of 2 friendly Merchant 
    ships sailing for our Capital Port. These Merchant ships are on a 
    clandestine mission to deliver classified cargo that will turn the 
    tide of this war once and for all!\n
    Unfortunately, during a recent skirmish, the Merchant ships lost all 
    communication capabilities and the Enemy's radar jamming technology 
    is preventing us from locating them. But we know they're out there, 
    somewhere. Hunt down the enemy with extreme prejudice, avoid 
    friendly fire at all costs and rescue those Merchant ships.\n
    Losing that cargo, means losing the war!\n''')

        mission_acceptance = input('              \033[33mAlert!!\033[0m' + \
        ' Enter Y for Yes or N for No. Accept ' + \
        'Mission?\n\n                                   ')
        mission_acceptance = mission_acceptance.lower()
        print(mission_acceptance + " test test test")
        print(username + " test test test")




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








