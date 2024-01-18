# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# >>>>>>>>>>>>>>> NOTES TO ADD TO README <<<<<<<<<<<<<<<<

# Resolved bug, made username global in start screen functions, was throwing error 

# >>>>>>>>>>>>>>> Imports <<<<<<<<<<<<<<<

import os
from random import randint
import sys
import time
from time import sleep

# >>>>>>>>>>>>>>> Variables <<<<<<<<<<<<<<<

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

# Stores the initialised count of enemy ships
enemy_ship_initialise_count = 0

# Stores enemy ship locations on battle grid
enemy_ship_locations = []

# Stores the initialised count of merchant ships
merchant_ship_initialise_count = 0

# Stores merchant_ship_locations on battle grid
merchant_ship_locations = []

# Stores the initialised count of battleship hull locations
battleship_hull_locations_initialise_count = 0

# Stores user's battleship hull locations on battle grid
battleship_hull_locations = []

# Stores locations of missed shots on battle grid
miss_locations = []

# Stores value of the user's battleship hull integrity
battleship_hull_integrity = 0

# Stores torpedos available to user
torpedo_count = 0

# Stores the battle grid displayed to the user and related shot results
battle_grid = [
    ['\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m',],
    ['\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m',],
    ['\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m',],
    ['\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m',],
    ['\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m',],
    ['\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m',],
    ['\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m',],
    ['\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m','\x1b[94m~\033[0m',]
]


# Stores the 'Battleship' portion of the banner art
banner_art_upper = ('''
             ___   ___  ______ ______ __    ____ ____ __ __ ____ ___   
            / _ ) / _ |/_  __//_  __// /   / __// __// // //  _// _ \ 
           / _  |/ __ | / /    / /  / /__ / _/ _\ \ / _  /_/ / / ___/
          /____//_/ |_|/_/    /_/  /____//___//___//_//_//___//_/    
''')

# Stores the 'Rescue' portion of the banner art
banner_art_lower = ('''
                         ___   ____ ____ _____ __  __ ____
                        / _ \ / __// __// ___// / / // __/
                       / , _// _/ _\ \ / /__ / /_/ // _/ 
                      /_/|_|/___//___/ \___/ \____//___/
''')


# Stores the banner art in its entirety (used without typing effect)
banner_art = ('''
             ___   ___  ______ ______ __    ____ ____ __ __ ____ ___   
            / _ ) / _ |/_  __//_  __// /   / __// __// // //  _// _ \ 
           / _  |/ __ | / /    / /  / /__ / _/ _\ \ / _  /_/ / / ___/
          /____//_/ |_|/_/    /_/  /____//___//___//_//_//___//_/    

\x1b[96m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m
\x1b[96m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m
\x1b[96m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m
                         ___   ____ ____ _____ __  __ ____
                        / _ \ / __// __// ___// / / // __/
                       / , _// _/ _\ \ / /__ / /_/ // _/ 
                      /_/|_|/___//___/ \___/ \____//___/

''')

# Stores the mission details message at the mission accept screen
mission_details_message = ('''It is with great regret that I must inform you that the situation has
    become dire. Our forces are being routed in every theatre and on every
    front, our supply chains have been decimated and our ability to sustain
    a defence against this onslaught can be measured now in hours.\n
    Your mission is to intercept and eliminate a fleet of 5 enemy Destroyers
    currently pursuing 2 friendly Merchant ships sailing for our Capital Port. 
    These Merchant ships are on a clandestine mission to deliver classified 
    cargo that will turn the tide of this war once and for all!\n
    Unfortunately, during a recent skirmish, the Merchant ships lost all
    communication capabilities and the enemy's radar jamming technology is
    preventing us from locating them. But we know they're out there, somewhere.
    Hunt down the enemy with extreme prejudice, avoid friendly fire at all
    costs and rescue those Merchant ships.\n
    Losing that cargo, means losing the war!\n''')


# >>>>>>>>>>>>>>> Functions <<<<<<<<<<<<<<<

def typing_effect(text, speed):
    """
    The typing effect functions will provide a visual
    effect that mimics the text being 'typed' in real
    time across the screen. This functions has been
    adapted from a Stackoverflow post credited in the 
    README.md file
    """ 
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


def start_screen():
    """
    The start screen function displays the initial welcome to
    the user along with the banner art and callsign input field
    """
    global username

    sleep(0.4)
    print(banner_art_upper) # Prints 'Battleship' to screen

    typing_effect\
    ('\x1b[96m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m\n', 0.005)
    #sleep(0.1)
    typing_effect\
    ('\x1b[96m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m\n', 0.005)
    #sleep(0.1)
    typing_effect\
    ('\x1b[96m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m', 0.005)

    print(banner_art_lower) # Prints 'Rescue' to screen

    # Effects to be used for shot confirmations
    #typing_effect('\n\n\n\033[36m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', 0.005)
    #print('\033[41m\033[37m\033[1m      BATTLESHIP HIT     \033[0m\033[22m')
    #print('\033[42m\033[30m\033[1m ENEMY SHIP NEUTRALISED  \033[0m\033[22m')
    #print('\033[47m\033[30m\033[1m      TARGET MISSED      \033[0m\033[22m')
    #print('\033[47m\033[31m\033[1m MERCHANT SHIP DESTROYED \033[0m\033[22m')

    sleep(0.6)
    typing_effect('                         The enemy controls the Land.\n', 0.03)
    typing_effect('                         The enemy controls the Skies.\n', 0.03)
    typing_effect('            One Battleship stands between them controlling the Seas.\n', 0.03)
    sleep(0.4)
    username_prompt = typing_effect('\n            Enter your callsign below (between \x1b[93m2\033[0m and \x1b[93m15\033[0m characters):\n\n', 0.03)
    username = input('                                 ')


def validate_username_screen():
    """
    The validate_username function will strip any 
    leading or trailing whitespaces from the
    username input variable, the value will then be checked
    to ensure it is more than 2 characters and less than 15.
    """
    global username
    username = username.strip()

    # While loop is used to perform validation on the username input,
    # must be greater than 2 characters and less than 15. The while 
    # loop will display an alert message until the parameters are satisfied.
    
    while len(username) < 2 or len(username) > 15:
        clearscreen() # Screen is cleared
        print(banner_art) 
        username = input('\n\n           \x1b[93mAlert!!' + \
        '\033[0m Enter a valid'\
        + ' callsign between \x1b[93m2\033[0m and \x1b[93m15\033[0m' + \
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
    print(banner_art)
    global mission_difficulty
    global mission_acceptance
    mission_difficulty = input(('\n\n               Enter Mission Diffic') + \
    ('ulty (Cadet, Captain, Admiral) \n\n                                   '))
    mission_difficulty = mission_difficulty.lower()

    while mission_difficulty not in difficulty_levels:
        clearscreen()
        print(banner_art)
        mission_difficulty = input('\n\n       \x1b[93mAlert!!\033[0m ' + \
        'Enter Mission Difficulty (select \x1b[93mCadet\033[0m, \x1b[93mCaptain\033[0m' + \
        ' or \x1b[93mAdmiral\033[0m) \n\n                                   ')
        mission_difficulty = mission_difficulty.lower()
    clearscreen()


def initialise_game_values(): # Note for bug in readme, had to move this higher up in the program due to unexpected behaviour
    """
    This function will determine and initialise the game values
    to be used when the game is launched. The values of the number
    of battleship hull hit locations, enemy ships, merchant ships,
    torpedos and the hull integrity starting value will be 
    assigned using this function, and driven by the difficulty
    level selected by the user
    """
    global enemy_ship_initialise_count
    global merchant_ship_initialise_count
    global battleship_hull_locations_initialise_count
    global battleship_hull_integrity
    global torpedo_count

    if mission_difficulty == 'cadet':
        enemy_ship_initialise_count = 5
        merchant_ship_initialise_count = 5
        battleship_hull_locations_initialise_count = 5
        battleship_hull_integrity = 100
        torpedo_count = 45
    elif mission_difficulty == 'captain':
        enemy_ship_initialise_count = 10
        merchant_ship_initialise_count = 4
        battleship_hull_locations_initialise_count = 10
        battleship_hull_integrity = 80
        torpedo_count = 40
    else:
        enemy_ship_initialise_count = 15
        merchant_ship_initialise_count = 3
        battleship_hull_locations_initialise_count = 15
        battleship_hull_integrity = 60
        torpedo_count = 35


def mission_accept_screen():
    """
    The mission accept screen function will provide a 
    visual effect where the user is connecting to 'Central Command'
    in order to access a message containing the mission details.
    This message will then display an input field requesting the 
    user to accept or reject.
    """

    clearscreen()
    time.sleep(.4)
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing secure connection with Central Command''')
    time.sleep(.4)
    clearscreen()
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing secure connection with Central Command.''')
    time.sleep(.4)
    clearscreen()
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing secure connection with Central Command..''')
    time.sleep(.4)
    clearscreen()
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing secure connection with Central Command...''')
    time.sleep(.4)
    clearscreen()
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing secure connection with Central Command....''')
    time.sleep(.4)
    clearscreen()
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing secure connection with Central Command.....''')
    time.sleep(.4)
    clearscreen()
    print(''' \n\n\n\n\n\n\n\n\n\n                          \x1b[92mSecure connection successful.\033[0m''')
    time.sleep(1)
    clearscreen()
    message1 = (f''' \n\n\n\n\n\n\n\n\n\n                \x1b[96mURGENT\033[0m Incoming''')
    message2 = (f''' Message: For {username.capitalize()}'s Eyes Only''')
    print(message1 + message2)
    time.sleep(2)
    clearscreen()
    typing_effect(f'''
    {mission_difficulty.capitalize()}, 
    It is with great regret that I must inform you that the situation has
    become dire. Our forces are being routed in every theatre and on every
    front, our supply chains have been decimated and our ability to sustain
    a defence against this onslaught can be measured now in hours.\n
    Your mission is to intercept and eliminate a fleet of {enemy_ship_initialise_count} enemy Destroyers 
    currently pursuing {merchant_ship_initialise_count} friendly Merchant ships sailing for our Capital Port. 
    These Merchant ships are on a clandestine mission to deliver classified 
    cargo that will turn the tide of this war once and for all!\n
    Unfortunately, during a recent skirmish, the Merchant ships lost all
    communication capabilities and the enemy's radar jamming technology is
    preventing us from locating them. But we know they're out there, somewhere.
    Hunt down the enemy with extreme prejudice, avoid friendly fire at all
    costs and rescue those Merchant ships.\n
    Losing that cargo, means losing the war!\n''',0.03)
    sleep(0.5)
    mission_acceptance = input('\n                         Accept' + \
    ' Mission? (Y / N)\n\n                                   ') 
    mission_acceptance = mission_acceptance.lower()

    while mission_acceptance not in mission_accept_options:
        clearscreen()
        print(f'''
    {mission_difficulty.capitalize()}, 
    It is with great regret that I must inform you that the situation has
    become dire. Our forces are being routed in every theatre and on every
    front, our supply chains have been decimated and our ability to sustain
    a defence against this onslaught can be measured now in hours.\n
    Your mission is to intercept and eliminate a fleet of {enemy_ship_initialise_count} enemy Destroyers 
    currently pursuing {merchant_ship_initialise_count} friendly Merchant ships sailing for our Capital Port. 
    These Merchant ships are on a clandestine mission to deliver classified 
    cargo that will turn the tide of this war once and for all!\n
    Unfortunately, during a recent skirmish, the Merchant ships lost all
    communication capabilities and the enemy's radar jamming technology is
    preventing us from locating them. But we know they're out there, somewhere.
    Hunt down the enemy with extreme prejudice, avoid friendly fire at all
    costs and rescue those Merchant ships.\n
    Losing that cargo, means losing the war!\n''')

        mission_acceptance = input('              \x1b[93mAlert!!\033[0m' + \
        ' Enter \x1b[93mY\033[0m for Yes or \x1b[93mN\033[0m for No. Accept ' + \
        'Mission?\n\n                                   ')
        mission_acceptance = mission_acceptance.lower()



def generate_battleship_hull_hit_locations():
    """
    This function will generate random x and y coordinates
    representing the location of each hull hit points on the 
    user's battleship. This is what the enemy will be firing
    upon.
    """
    while len(battleship_hull_locations) < int(battleship_hull_locations_initialise_count):
        x_coordinate = (randint(0, 7))
        y_coordinate = (randint(0, 7))
        hull_hit_location = (x_coordinate, y_coordinate)
        if hull_hit_location in battleship_hull_locations:
            continue # Note for readme, changed from break to continue, unexpected behaviour
        else:
            battleship_hull_locations.append(hull_hit_location)


def generate_enemy_ship_locations():
    """
    This function will generate random x and y coordinates
    representing the location of each enemy ship on the battle
    grid. This is what the user will be attempting to hit with
    each shot.
    """
    while len(enemy_ship_locations) < enemy_ship_initialise_count:
        x_coordinate = (randint(0, 7))
        y_coordinate = (randint(0, 7))
        enemy_ship_location = (x_coordinate, y_coordinate)
        if enemy_ship_location in enemy_ship_locations:
            continue # Note for readme, changed from break to continue, unexpected behaviour
        elif enemy_ship_location in battleship_hull_locations:
            continue # Note for readme, changed from break to continue, unexpected behaviour
        else:
            enemy_ship_locations.append(enemy_ship_location)


def generate_merchant_ship_locations():
    """
    This function will generate random x and y coordinates
    representing the location of each merchant ship on the
    battle grid. This is what the user will be attempting
    to avoid hitting with each shot.
    """
    while len(merchant_ship_locations) < merchant_ship_initialise_count:
        x_coordinate = (randint(0, 7))
        y_coordinate = (randint(0, 7))
        merchant_ship_location = (x_coordinate, y_coordinate)
        if merchant_ship_location in merchant_ship_locations:
            continue # Note for readme, changed from break to continue, unexpected behaviour
        elif merchant_ship_location in enemy_ship_locations:
            continue
        elif merchant_ship_location in battleship_hull_locations:
            continue # Note for readme, changed from break to continue, unexpected behaviour
        else:
            merchant_ship_locations.append(merchant_ship_location)



def game_screen():
    clearscreen()
    sleep(0.5)
    typing_effect('--------------------- Battleship Operations SITREP Display ---------------------\n\n',0.02)
    sleep(0.5)
    print('Torpedos remaining:       \x1b[96m00\033[0m            Hull integrity:         \x1b[96m100%\033[0m')
    print('Enemy ships remaining:    \x1b[96m00\033[0m            Enemy ships destroyed:    \x1b[96m00\033[0m')
    print('Merchant ships remaining: \x1b[96m00\033[0m            Merchant ships destroyed: \x1b[96m00\033[0m')

    for rows in range(8):



def main():
    """
    The main function will trigger all 
    functions necessary to run the game
    """
    start_screen() # Displays start screen
    validate_username_screen() # Validates username input
    mission_difficulty_screen() # Requests user to select difficulty 
    initialise_game_values() # Initialises the starting game values 
    mission_accept_screen() # Displays mission details with prompt
    generate_battleship_hull_hit_locations() # Creates battleship hull hit locations
    generate_enemy_ship_locations() # Creates enemy ship locations
    generate_merchant_ship_locations() # Creates merchant ship locations
    game_screen() # Displays the main game screen
main()


# Debugging messages below, delete when ready!
# clearscreen()
# print('Mission difficulty selected: ' + mission_difficulty)
# print('Enemy ships starting value: ' + str(enemy_ship_initialise_count))
# print('Merchant ships starting value: ' + str(merchant_ship_initialise_count))
# print('Battleship hull locations starting value: ' + str(battleship_hull_locations_initialise_count))
# print('Battleship hull integrity starting value: ' + str(battleship_hull_integrity))
# print('Torpedo count starting value: ' + str(torpedo_count))
# print('\nBattleship hull locations: ', end="")
# print(battleship_hull_locations)
# print('\nEnemy ship locations: ', end="")
# print(enemy_ship_locations)
# print('\nMerchant ship locations: ', end="")
# print(merchant_ship_locations)