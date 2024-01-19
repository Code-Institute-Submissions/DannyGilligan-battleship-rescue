# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# >>>>>>>>>>>>>>> NOTES TO ADD TO README <<<<<<<<<<<<<<<<

# Resolved bug, made username global in start screen functions, was throwing error
# colored text https://replit.com/talk/ask/How-to-change-terminal-color-in-python/125888 
# typing effect https://stackoverflow.com/questions/20302331/typing-effect-in-python
# site used for character count
# site used for special symbols https://www.compart.com/en/unicode/U+2731

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

# Stores enemy ships destroyed counter value
enemy_ships_destroyed = 0

# Stores the initialised count of merchant ships
merchant_ship_initialise_count = 0

# Stores merchant ship locations on battle grid
merchant_ship_locations = []

# Stores merchant ships destroyed counter value
merchant_ships_destroyed = 0

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
    ['\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m'],
    ['\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m'],
    ['\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m'],
    ['\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m'],
    ['\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m'],
    ['\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m'],
    ['\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m'],
    ['\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m'],
    ['\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m','\x1b[96m~\033[0m']
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
    print(''' \n\n\n\n\n\n\n\n\n\n                         \x1b[92mSecure connection established.\033[0m''')
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
    upon. The function checks if the generated coordinates 
    have already been used in the battleship hull list, if
    they've been used already, the current iteration is skipped
    until a combination of coordinates that haven't been used
    already are generated, at which point they will appended
    to the battleship hull locations list.
    """
    while len(battleship_hull_locations) < int(battleship_hull_locations_initialise_count):
        x_coordinate = (randint(0, 7))
        y_coordinate = (randint(0, 7))
        hull_hit_location = [int(x_coordinate)] + [int(y_coordinate)]
        if hull_hit_location in battleship_hull_locations:
            continue # Note for readme, changed from break to continue, unexpected behaviour
        else:
            battleship_hull_locations.append(hull_hit_location)


def generate_enemy_ship_locations():
    """
    This function will generate random x and y coordinates
    representing the location of each enemy ship on the battle
    grid. This is what the user will be attempting to hit with
    each shot. The function checks if 
    the generated coordinates have already been used in the
    enemy ship and battleship hull lists, if
    they've been used already, the current iteration is skipped
    until a combination of coordinates that haven't been used
    already are generated, at which point they will appended
    to the enemy ship locations list.
    """
    while len(enemy_ship_locations) < enemy_ship_initialise_count:
        x_coordinate = (randint(0, 7))
        y_coordinate = (randint(0, 7))
        enemy_ship_location = [int(x_coordinate)] + [int(y_coordinate)]
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
    to avoid hitting with each shot. The function checks if 
    the generated coordinates have already been used in the
    merchant ship, enemy ship and battleship hull lists, if
    they've been used already, the current iteration is skipped
    until a combination of coordinates that haven't been used
    already are generated, at which point they will appended
    to the merchant ship locations list.
    """
    while len(merchant_ship_locations) < merchant_ship_initialise_count:
        x_coordinate = (randint(0, 7))
        y_coordinate = (randint(0, 7))
        merchant_ship_location = [int(x_coordinate)] + [int(y_coordinate)]
        if merchant_ship_location in merchant_ship_locations:
            continue # Note for readme, changed from break to continue, unexpected behaviour
        elif merchant_ship_location in enemy_ship_locations:
            continue
        elif merchant_ship_location in battleship_hull_locations:
            continue # Note for readme, changed from break to continue, unexpected behaviour
        else:
            merchant_ship_locations.append(merchant_ship_location)



def game_screen():

    global battle_grid
    global torpedo_count
    global enemy_ships_destroyed
    global merchant_ships_destroyed

    clearscreen()
    sleep(0.5)
    typing_effect('--------------------- Battleship Operations SITREP Display ---------------------\n\n',0.01)
    sleep(1)
    while torpedo_count > 0:

        clearscreen()
        print('--------------------- Battleship Operations SITREP Display ---------------------\n\n')
        #sleep(0.5)
        #clearscreen()
        print(f'Torpedos remaining:       \x1b[96m{torpedo_count:02}\033[0m                       Hull integrity:          \x1b[96m{battleship_hull_integrity:02}%\033[0m')   # Note for bug resolved, https://stackoverflow.com/questions/3505831/in-python-how-do-i-convert-a-single-digit-number-into-a-double-digits-string
        print(f'Enemy ships remaining:    \x1b[96m{(len(enemy_ship_locations)):02}\033[0m                       Enemy ships destroyed:    \x1b[96m{enemy_ships_destroyed}\033[0m')
        print(f'Merchant ships remaining: \x1b[96m{(len(merchant_ship_locations)):02}\033[0m                       Merchant ships destroyed: \x1b[96m{merchant_ships_destroyed}\033[0m')
        print('\n')


        col_headers = []                                                  # Empty array to hold the column header values based on the userinput
        for i in range(9):                                                # Iterates for 9 x 9 grid size  
            col_headers.append(i)                                         # Appends the column header numbers to the array 
        col_headers.insert(0, " ")                                        # NOTE FOR BUG, HAD TO INDENT THIS OUTSIDE OF THE LOOP, and insert a blank space so it would align
        print("                             ", *col_headers, sep = ' ')   # Breaks out the column headers from the array and prints horizontally

        row_counter = 0
        for row_array in battle_grid: 
            print("                             ", row_counter, end = " ")
            row_counter += 1
            for col_elem in row_array:
                print(col_elem, end = " ")
            print()
            
        print('Enemy ships: ', end="") # Debug, delete when ready
        print(enemy_ship_locations) # Debug, delete when ready
        print('Merchant ships: ', end="") # Debug, delete when ready
        print(merchant_ship_locations) # Debug, delete when ready
        print('Hull points: ', end="") # Debug, delete when ready
        print(battleship_hull_locations) # Debug, delete when ready

        print('Before a shot has been taken, the torpedo count is: ' + str(torpedo_count))
        user_x_coord = input('\nEnter row to fire upon: \n')
        user_y_coord = input('Enter column to fire upon: \n')

        user_shot = [int(user_x_coord), int(user_y_coord)]
        torpedo_count -= 1

        battle_grid[0][0] = 'X'

        print('A shot has been taken, the torpedo count is now: ' + str(torpedo_count))
        ############ DEBUGGING BELOW ######################

        #print(user_shot) 
        #print(type(user_shot))
        #enemy = enemy_ship_locations[0]
        #print(enemy)
        #print(type(enemy))
        #if enemy == user_shot:
        #    print('They are the same')
        #else: 
        #    print('They are not the same')

        ############ DEBUGGING ABOVE ######################

        if user_shot in enemy_ship_locations:
            typing_effect('\n\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \r', 0.005)
            for iterations in range(8):
                print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \x1b[42m\x1b[97m\x1b[1m   ENEMY SHIP DESTROYED   \x1b[0m\r', end="", flush=True)
                sleep(0.15)
                print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \x1b[7m\x1b[42m\x1b[97m\x1b[1m   ENEMY SHIP DESTROYED   \x1b[0m\r', end="", flush=True)
                sleep(0.15)
            enemy_ship_locations.remove(user_shot)
            battle_grid[int(user_x_coord)][int(user_y_coord)] = '\x1b[92mE\x1b[0m'
            enemy_ships_destroyed += 1
        elif user_shot in merchant_ship_locations:
            typing_effect('\n\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \r', 0.005)
            for iterations in range(10):
                print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \x1b[103m\x1b[30m\x1b[1m MERCHANT SHIP DESTROYED  \x1b[0m\r', end="", flush=True)
                sleep(0.15)
                print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \x1b[7m\x1b[103m\x1b[30m\x1b[1m MERCHANT SHIP DESTROYED  \x1b[0m\r', end="", flush=True)
                sleep(0.15)
            merchant_ship_locations.remove(user_shot)
            battle_grid[int(user_x_coord)][int(user_y_coord)] = '\x1b[93mM\x1b[0m'
            merchant_ships_destroyed += 1
        else:
            typing_effect('\n\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \r', 0.005)
            for iterations in range(10):
                print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \x1b[107m \x1b[30m      TARGET MISSED      \x1b[0m\r', end="", flush=True)
                sleep(0.15)
                print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \x1b[107m \x1b[30m      TARGET MISSED      \x1b[0m\r', end="", flush=True)
                sleep(0.15)


print("WHILE LOOP HAS WORKED!")

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


    
#print('\n\x1b[93m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', end="")
#print('\033[30m\x1b[42m ENEMY SHIP NEUTRALISED  \x1b[0m')
#print('\n\x1b[93m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', end="")
#print('\033[47m\033[31m\033[1m MERCHANT SHIP DESTROYED \033[0m\033[22m')
#print('\n\x1b[93m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', end="")
#print('\x1b[47m\033[30m      TARGET MISSED      \033[0m\033[22m')
#print('\n\033[36m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', end="")
#print('\033[41m\033[37m\033[1m      BATTLESHIP HIT     \033[0m\033[22m')


#print('\n\x1b[93m >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', end="")
#print('\x1b[107m \x1b[92m ENEMY SHIP NEUTRALISED  \x1b[0m')
#print('\n\x1b[93m >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', end="")
#print('\x1b[107m \x1b[31m MERCHANT SHIP DESTROYED \x1b[0m')
#print('\n\x1b[93m >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', end="")
#print('\x1b[107m \x1b[30m      TARGET MISSED      \x1b[0m')
#rint('\n\033[36m >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', end="")
#print('\x1b[107m \x1b[91m      BATTLESHIP HIT     \x1b[0m')


#print('\n\x1b[93m >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', end="")
#print('\x1b[42m\x1b[97m\x1b[1m ENEMY SHIP DESTROYED \x1b[0m')
#print('\n\x1b[93m >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', end="")
#print('\x1b[107m\x1b[31m\x1b[1m MERCHANT SHIP DESTROYED \x1b[0m')
#print('\n\x1b[93m >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', end="")
#rint('\x1b[107m\x1b[30m\x1b[1m     TARGET MISSED      \x1b[0m')
#print('\n\033[36m >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', end="")
#rint('\033[41m\033[37m\033[1m     BATTLESHIP HIT     \x1b[0m')


#typing_effect('\n\x1b[93m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   ', 0.005)
#print('\x1b[107m \x1b[30m      TARGET MISSED     \x1b[0m')


#typing_effect('\n\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \r', 0.005)
#for iterations in range(10):
    #print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \033[41m\033[37m\033[1m      BATTLESHIP HIT      \x1b[0m\r', end="", flush=True)
    #sleep(0.15)
    #print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \x1b[7m\033[41m\033[37m\033[1m      BATTLESHIP HIT      \x1b[0m\r', end="", flush=True)
    #sleep(0.15)

#typing_effect('\n\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \r', 0.005)
#for iterations in range(10):
    #print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \x1b[103m\x1b[30m\x1b[1m MERCHANT SHIP DESTROYED  \x1b[0m\r', end="", flush=True)
    #sleep(0.15)
    #print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \x1b[7m\x1b[103m\x1b[30m\x1b[1m MERCHANT SHIP DESTROYED  \x1b[0m\r', end="", flush=True)
    #sleep(0.15)

#typing_effect('\n\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \r', 0.005)
#for iterations in range(10):
    #print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \x1b[42m\x1b[97m\x1b[1m   ENEMY SHIP DESTROYED   \x1b[0m\r', end="", flush=True)
    #sleep(0.15)
    #print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \x1b[7m\x1b[42m\x1b[97m\x1b[1m   ENEMY SHIP DESTROYED   \x1b[0m\r', end="", flush=True)
    #sleep(0.15)

#typing_effect('\n\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \r', 0.005)
#for iterations in range(10):
    #print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \x1b[107m \x1b[30m      TARGET MISSED      \x1b[0m\r', end="", flush=True)
    #sleep(0.15)
    #print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \x1b[107m \x1b[30m      TARGET MISSED      \x1b[0m\r', end="", flush=True)
    #sleep(0.15)

#print('\n\n\n')
#print('animation test 1')
#print('animation test 2')