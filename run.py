# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# >>>>>>>>>>>>>>> NOTES TO ADD TO README <<<<<<<<<<<<<<<<

# Resolved bug, made username global in start screen functions, was throwing error
# colored text https://replit.com/talk/ask/How-to-change-terminal-color-in-python/125888 
# typing effect https://stackoverflow.com/questions/20302331/typing-effect-in-python
# site used for character count
# site used for special symbols https://www.compart.com/en/unicode/U+2731
# Resolved bug, shot accuracy len(total_shots) was zero, received divide by zero error, used ternary operator to assign value instead https://rollbar.com/blog/python-zerodivisionerror/#
# Add credit for clearscreen function
# how to hide cursor https://stackoverflow.com/questions/5174810/how-to-turn-off-blinking-cursor-in-command-window
# resolved bug, when it's impossible to win, add condition to while loop, torpedo_count >= int(len(enemy_ship_locations)), add screenshot of code
# resolved bug, add condition to prevent an enemy shot when all enemy or merchant ships are destroyed, add screenshot of code
# resolved bug, add conditions to prevent overwriting an enemy hit or merchant hit symbol when coordinates are fired upon again
# https://pep8ci.herokuapp.com/ PEP8 Code Checker
# Future feature, skip text
# Future feature, user feedback to adjust game variables

# >>>>>>>>>>>>>>> IMPORTS <<<<<<<<<<<<<<<

import os
from random import randint
import sys
import time
from time import sleep

# >>>>>>>>>>>>>>> VARIABLES <<<<<<<<<<<<<<<

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

# Stores locations of enemy shots
enemy_shots = []

# Stores locations of enemy misses
enemy_misses = []

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
hull_plates_remaining = 0

# Stores torpedos available to user
torpedo_count = 0

# Stores valid shot input values
valid_shot_inputs = ['0', '1', '2', '3', '4', '5', '6']

# Stores total number of shots taken (used to calculate accuracy)
total_shots = []

# Stores shot accuracy (enemy ships hit / total shots), displayed as percentage
shot_accuracy = ((enemy_ships_destroyed / len(total_shots)) * 100) \
    if len(total_shots) > 0 else 0


# Stores the battle grid displayed to the user and related shot results
battle_grid = [
    ['\x1b[96m~\033[0m', '\x1b[96m~\033[0m', '\x1b[96m~\033[0m',
        '\x1b[96m~\033[0m', '\x1b[96m~\033[0m', '\x1b[96m~\033[0m',
        '\x1b[96m~\033[0m'],
    ['\x1b[96m~\033[0m', '\x1b[96m~\033[0m', '\x1b[96m~\033[0m',
        '\x1b[96m~\033[0m', '\x1b[96m~\033[0m', '\x1b[96m~\033[0m',
        '\x1b[96m~\033[0m'],
    ['\x1b[96m~\033[0m', '\x1b[96m~\033[0m', '\x1b[96m~\033[0m',
        '\x1b[96m~\033[0m', '\x1b[96m~\033[0m', '\x1b[96m~\033[0m',
        '\x1b[96m~\033[0m'],
    ['\x1b[96m~\033[0m', '\x1b[96m~\033[0m', '\x1b[96m~\033[0m',
        '\x1b[96m~\033[0m', '\x1b[96m~\033[0m', '\x1b[96m~\033[0m',
        '\x1b[96m~\033[0m'],
    ['\x1b[96m~\033[0m', '\x1b[96m~\033[0m', '\x1b[96m~\033[0m',
        '\x1b[96m~\033[0m', '\x1b[96m~\033[0m', '\x1b[96m~\033[0m',
        '\x1b[96m~\033[0m'],
    ['\x1b[96m~\033[0m', '\x1b[96m~\033[0m', '\x1b[96m~\033[0m',
        '\x1b[96m~\033[0m', '\x1b[96m~\033[0m', '\x1b[96m~\033[0m',
        '\x1b[96m~\033[0m'],
    ['\x1b[96m~\033[0m', '\x1b[96m~\033[0m', '\x1b[96m~\033[0m',
        '\x1b[96m~\033[0m', '\x1b[96m~\033[0m', '\x1b[96m~\033[0m',
        '\x1b[96m~\033[0m']
]

# Stores the 'Battleship' portion of the banner art
banner_art_upper = (r'''
             ___   ___  ______ ______ __    ____ ____ __ __ ____ ___
            / _ ) / _ |/_  __//_  __// /   / __// __// // //  _// _ \
           / _  |/ __ | / /    / /  / /__ / _/ _\ \ / _  /_/ / / ___/
          /____//_/ |_|/_/    /_/  /____//___//___//_//_//___//_/
''')

# Stores the banner art wave patterns
banner_art_mid = ('\x1b[96m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\
〜〜〜〜〜〜〜〜〜〜\033[0m\n\x1b[96m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\
〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m\n\x1b[96m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\
〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m')

# Stores the 'Rescue' portion of the banner art
banner_art_lower =\
    (r'''                         ___   ____ ____ _____ __  __ ____
                        / _ \ / __// __// ___// / / // __/
                       / , _// _/ _\ \ / /__ / /_/ // _/
                      /_/|_|/___//___/ \___/ \____//___/
    ''')

# >>>>>>>>>>>>>>> FUNCTIONS <<<<<<<<<<<<<<<

# The typing effect code was adapted from
# a Stackoverflow post credited in the
# README.md file, I tweaked it to make
# 'speed' a parameter so it could be
# customised depending on the context.


def typing_effect(text, speed):
    """
    The typing effect functions will provide a visual
    effect that mimics the text being 'typed' in real
    time across the screen. 
    """
    # This function has been adapted from a Stackoverflow
    # post credited in the README.md file.
    # The change to the original code relates to adding
    # speed as a parameter that can be adjusted as needed

    words = text
    for char in words:
        time.sleep(speed)  # amended to make speed a parameter
        sys.stdout.write(char)
        sys.stdout.flush()




def clearscreen():
    """
    The clearscreen function will clear any
    content from the current screen
    displayed to the user.
    """
    # The clearscreen code below was taken
    # in full, without any tweaking from a
    # Stackoverflow post credited in the README.md file
    os.system('cls' if os.name == 'nt' else 'clear')


def start_screen():
    """
    The start screen function displays the initial welcome to
    the user along with the banner art and callsign input field
    """
    global username
    clearscreen()
    sleep(0.4)
    print('\033[?25l', end="")  # Code to hide cursor credited in README.md
    print(banner_art_upper)  # Prints 'Battleship' to screen

    typing_effect('\x1b[96m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\
〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m\n', 0.005)
    typing_effect('\x1b[96m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\
〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m\n', 0.005)
    typing_effect('\x1b[96m〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\
〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜\033[0m\n', 0.005)
    print(banner_art_lower)  # Prints 'Rescue' to screen
    print('\n')
    sleep(0.0)
    typing_effect('                         The enemy \
controls the land.\n', 0.02)
    typing_effect('                         The enemy \
controls the skies.\n', 0.02)
    typing_effect('            One Battleship stands between \
them controlling the seas.\n', 0.02)
    sleep(0.4)
    username_prompt = typing_effect('\n            Enter your call \
sign below (between \x1b[93m2\033[0m and \x1b[93m15\033[0m \
characters):\n\n', 0.02)
    print('\033[?25h', end="")  # Code to show cursor credited in README.md
    username = input('                                 ')


def validate_username_screen():
    """
    The validate_username function will strip any
    leading or trailing whitespaces from the
    username input variable, the value will then be checked
    to ensure it is more than 2 characters and less than 15
    using the len() method and a while loop.
    """
    global username
    username = username.strip()

    # While loop is used to perform validation on the username input,
    # must be greater than 2 characters and less than 15. The while
    # loop will display an alert message until the parameters are satisfied.
    while len(username) < 2 or len(username) > 15:
        clearscreen()  # Screen is cleared
        print(banner_art_upper)
        print(banner_art_mid)
        print(banner_art_lower)
        print('\n')
        print('                         The enemy controls the land.')
        print('                         The enemy controls the skies.')
        print('            One Battleship stands betwe\
en them controlling the seas.')
        username = input('\n           \x1b[93mAlert!!\
\033[0m Enter a valid call sign between \x1b[93m2\033[0m and \
\x1b[93m15\033[0m characters\n\n                                   ')
        username = username.strip()  # Strip method is used
    clearscreen()  # Screen is cleared


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
    print(banner_art_upper)
    print(banner_art_mid)
    print(banner_art_lower)
    global mission_difficulty
    global mission_acceptance
    mission_difficulty = input(('\n\n               Enter Mis\
sion Difficulty (Cadet, Captain, Admir\
al) \n\n                                   '))
    mission_difficulty = mission_difficulty.lower()

    while mission_difficulty not in difficulty_levels:
        clearscreen()
        print(banner_art_upper)
        print(banner_art_mid)
        print(banner_art_lower)
        mission_difficulty = input('\n\n       \x1b[93mAlert!\
!\033[0m Enter Mission Difficulty (select \x1b[93mC\
adet\033[0m, \x1b[93mCaptain\033[0m or \x1b[93mAdmir\
al\033[0m) \n\n                                   ')
        mission_difficulty = mission_difficulty.lower()
    clearscreen()


def initialise_game_values():
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
    global hull_plates_remaining
    global torpedo_count

    if mission_difficulty == 'cadet':
        enemy_ship_initialise_count = 10
        merchant_ship_initialise_count = 8
        battleship_hull_locations_initialise_count = 5
        hull_plates_remaining = 10
        torpedo_count = 45
    elif mission_difficulty == 'captain':
        enemy_ship_initialise_count = 12
        merchant_ship_initialise_count = 7
        battleship_hull_locations_initialise_count = 10
        hull_plates_remaining = 8
        torpedo_count = 40
    else:
        enemy_ship_initialise_count = 14
        merchant_ship_initialise_count = 6
        battleship_hull_locations_initialise_count = 15
        hull_plates_remaining = 6
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
    print('\033[?25l', end="")  # Code to hide cursor credited in README.md
    time.sleep(.4)
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing \
secure connection with Central Command''')
    time.sleep(.4)
    clearscreen()
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing \
secure connection with Central Command.''')
    time.sleep(.4)
    clearscreen()
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing \
secure connection with Central Command..''')
    time.sleep(.4)
    clearscreen()
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing \
secure connection with Central Command...''')
    time.sleep(.4)
    clearscreen()
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing \
secure connection with Central Command....''')
    time.sleep(.4)
    clearscreen()
    print(''' \n\n\n\n\n\n\n\n\n\n              Establishing \
secure connection with Central Command.....''')
    time.sleep(.4)
    clearscreen()
    print(''' \n\n\n\n\n\n\n\n\n\n                         \x1b\
[92mSecure connection established.\033[0m''')
    time.sleep(1)
    clearscreen()
    message1 = (f''' \n\n\n\n\n\n\n\n\n\n                \x1b\
[96mURGENT\033[0m Incoming''')
    message2 = (f''' Message: For {username.capitalize()}'s \
Eyes Only''')
    print(message1 + message2)
    time.sleep(2)
    clearscreen()
    typing_effect(f'''
    {mission_difficulty.capitalize()},
    It is with great regret that I must inform you that \
the situation has
    become dire. Our forces are being routed in every \
theatre and on every
    front, our supply chains have been decimated and our \
ability to sustain
    a defence against this onslaught can be measured now \
in hours.\n
    Your orders are to intercept and eliminate a fleet of \
{enemy_ship_initialise_count} enemy Destroyers
    currently pursuing {merchant_ship_initialise_count} \
friendly Merchant ships sailing for our Capital Port.
    These Merchant ships are on a clandestine mission to \
deliver classified
    cargo that will turn the tide of this war once and for \
all!\n
    Unfortunately, during a recent skirmish, the Merchant \
ships lost all
    communication capabilities and the enemy's radar jamming \
technology is
    preventing us from locating them. But we know they're \
out there, somewhere.
    Hunt down the enemy with extreme prejudice, avoid \
friendly fire at all
    costs and rescue those Merchant ships.\n
    Losing that cargo, means losing the war!\n''', 0.03)
    sleep(0.5)
    print('\033[?25h', end="")  # Code to show cursor credited in README.md
    mission_acceptance = input('\n                         Accept \
Mission? (Y / N)\n\n                                   ')
    mission_acceptance = mission_acceptance.lower()

    while mission_acceptance not in mission_accept_options:
        clearscreen()
        print(f'''
    {mission_difficulty.capitalize()},
    It is with great regret that I must inform you that \
the situation has
    become dire. Our forces are being routed in every \
theatre and on every
    front, our supply chains have been decimated and our \
ability to sustain
    a defence against this onslaught can be measured now \
in hours.\n
    Your orders are to intercept and eliminate a fleet of \
{enemy_ship_initialise_count} enemy Destroyers
    currently pursuing {merchant_ship_initialise_count} \
friendly Merchant ships sailing for our Capital Port.
    These Merchant ships are on a clandestine mission to \
deliver classified
    cargo that will turn the tide of this war once and for \
all!\n
    Unfortunately, during a recent skirmish, the Merchant \
ships lost all
    communication capabilities and the enemy's radar jamming \
technology is
    preventing us from locating them. But we know they're \
out there, somewhere.
    Hunt down the enemy with extreme prejudice, avoid \
friendly fire at all
    costs and rescue those Merchant ships.\n
    Losing that cargo, means losing the war!\n''')

        mission_acceptance = input('              \x1b[93mAler\
t!!\033[0m Enter \x1b[93mY\033[0m for Yes or \x1b[93mN\033[0m \
for No. Accept Mission?\n\n                                   ')
        mission_acceptance = mission_acceptance.lower()

    if mission_acceptance == 'n':
        sleep(0.2)
        clearscreen()
        sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n')
        print('    This war will only be won, when those \
with the courage to fight, use it.\n\n')
        print('                       \x1b[91mDisconnect\
ing from Central Command\x1b[1m')
        sleep(10)
        clearscreen()
        raise SystemExit()


def generate_battleship_hull_hit_locations():
    """
    This function will generate random x and y coordinates
    representing the location of each hull hit points on the
    user's battleship. This is what the enemy will be firing
    upon. The function checks if the generated coordinates
    have already been used in the battleship hull list, if
    they've been used already, the current iteration is skipped
    until a combination of coordinates that haven't been used
    already are generated, at which point they will be appended
    to the battleship hull locations list.
    """
    while len(battleship_hull_locations) \
            < int(battleship_hull_locations_initialise_count):
        x_coordinate = (randint(0, 6))
        y_coordinate = (randint(0, 6))
        hull_hit_location = [int(x_coordinate)] + [int(y_coordinate)]
        if hull_hit_location in battleship_hull_locations:
            continue
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
    already are generated, at which point they will be appended
    to the enemy ship locations list.
    """
    while len(enemy_ship_locations) < enemy_ship_initialise_count:
        x_coordinate = (randint(0, 6))
        y_coordinate = (randint(0, 6))
        enemy_ship_location = [int(x_coordinate)] + [int(y_coordinate)]
        if enemy_ship_location in enemy_ship_locations:
            continue
        elif enemy_ship_location in battleship_hull_locations:
            continue
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
    already are generated, at which point they will be appended
    to the merchant ship locations list.
    """
    while len(merchant_ship_locations) < merchant_ship_initialise_count:
        x_coordinate = (randint(0, 6))
        y_coordinate = (randint(0, 6))
        merchant_ship_location = [int(x_coordinate)] + [int(y_coordinate)]
        if merchant_ship_location in merchant_ship_locations:
            continue
        elif merchant_ship_location in enemy_ship_locations:
            continue
        elif merchant_ship_location in battleship_hull_locations:
            continue
        else:
            merchant_ship_locations.append(merchant_ship_location)


def sitrep_loading():
    """
    The sitrep loading function will display information
    to the user about the battleship, this is an attempt
    at further immersion into the game to enhance
    the user experience
    """
    clearscreen()
    print('\033[?25l', end="")  # Code to hide cursor credited in README.md
    print('\n\n\n\n')
    sleep(0.2)
    typing_effect("                         Loading \
SITREP Display Module\x1b[0m\n\n", 0.01)
    sleep(0.4)
    typing_effect("                    Vessel Name        \
: \x1b[96mMeridian Queen\033[0m\n", 0.01)
    sleep(0.4)
    typing_effect("                    Vessel Type        \
: \x1b[96mSovereign Class Heavy Battleship\033[0m\n", 0.01)
    sleep(0.4)
    typing_effect("                    Primary Armament   \
: \x1b[96m'Sea Stiletto' Nuclear Torpedo\033[0m\n", 0.01)
    sleep(0.4)
    typing_effect("                    Secondary Armament \
: \x1b[96m'Arbiter' 16\" Deck Guns\033[0m\n", 0.01)
    sleep(0.4)
    typing_effect("                    Hull Armour        \
: \x1b[96m50mm Titanium Plates\033[0m\n", 0.01)
    sleep(0.4)
    typing_effect("                    Propulsion Systems \
: \x1b[92mOnline\033[0m\n", 0.01)
    sleep(0.4)
    typing_effect("                    Navigation Systems \
: \x1b[92mOnline\033[0m\n", 0.01)
    sleep(0.4)
    typing_effect("                    Weapons Systems    \
: \x1b[92mOnline\033[0m\n", 0.01)
    sleep(0.4)
    typing_effect("                    Radar Targetting   \
: \x1b[91mOffline\033[0m\n\n\n", 0.01)
    sleep(0.4)
    print("                          \x1b[92mSITRE\
P Display Module Ready\033[0m")
    print('\033[?25h', end="")  # Code to show cursor credited in README.md
    sleep(2)


##################################################################################################################################################################### VALIDATED IN CI LINTER UP TO THIS POINT

def game_screen():

    global battle_grid
    global torpedo_count
    global enemy_ships_destroyed
    global merchant_ships_destroyed
    global shot_accuracy
    global total_shots
    global hull_plates_remaining

    clearscreen()
    print('\033[?25l', end="") # Code to hide cursor credited in README.md
    sleep(0.5)
    typing_effect('--------------------- \x1b[96mBattleship Operations SITREP Display\033[0m ---------------------\n',0.01)
    sleep(0.5)
    print('\033[?25h', end="") # Code to show cursor credited in README.md
    while torpedo_count > 0 and hull_plates_remaining > 0 and int(len(enemy_ship_locations)) > 0 and int(len(merchant_ship_locations)) > 0 and torpedo_count >= int(len(enemy_ship_locations)):
        ### 1. PRINTS SITREP PANEL TO SCREEN ###
        clearscreen()
        print('--------------------- \x1b[96mBattleship Operations SITREP Display\033[0m ---------------------\n')
        shot_accuracy = int((enemy_ships_destroyed / len(total_shots)) * 100) if len(total_shots) > 0 else 0
        print(f'Torpedos remaining:       \x1b[96m{torpedo_count:02}\033[0m                   (\x1b[90mX\x1b[0m) Missed shots:             \x1b[96m{(len(miss_locations)):02}\033[0m')   # Note for bug resolved, https://stackoverflow.com/questions/3505831/in-python-how-do-i-convert-a-single-digit-number-into-a-double-digits-string
        print(f'Hull plates remaining:    \x1b[96m{hull_plates_remaining:02}\033[0m                       Shot accuracy:           \x1b[96m{shot_accuracy:02}%\033[0m')
        print(f'Enemy ships remaining:    \x1b[96m{(len(enemy_ship_locations)):02}\033[0m                   (\x1b[92mE\x1b[0m) Enemy ships destroyed:    \x1b[96m{enemy_ships_destroyed:02}\033[0m')
        print(f'Merchant ships remaining: \x1b[96m{(len(merchant_ship_locations)):02}\033[0m                   (\x1b[93mM\x1b[0m) Merchant ships destroyed: \x1b[96m{merchant_ships_destroyed:02}\033[0m')
        print('\n')

        ### 2. PRINTS BATTLE GRIP TO SCREEN ###
        col_headers = []                                                  # Empty array to hold the column header values based on the userinput
        for i in range(7):                                                # Iterates for 9 x 9 grid size  
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

        print('\x1b[92mWEAPONS READY\x1b[0m')

        ### 3. PROMPTS USER TO ENTER VALID X COORDINATE INPUT (WHILE LOOP VALIDATES) ###
        user_x_coord = input('\nEnter row to fire upon: \n')

        while user_x_coord not in valid_shot_inputs:
            clearscreen()
            print('--------------------- \x1b[96mBattleship Operations SITREP Display\033[0m ---------------------\n')
            #sleep(0.5)
            #clearscreen()
            shot_accuracy = int((enemy_ships_destroyed / len(total_shots)) * 100) if len(total_shots) > 0 else 0
            print(f'Torpedos remaining:       \x1b[96m{torpedo_count:02}\033[0m                   (\x1b[90mX\x1b[0m) Missed shots:             \x1b[96m{(len(miss_locations)):02}\033[0m')   # Note for bug resolved, https://stackoverflow.com/questions/3505831/in-python-how-do-i-convert-a-single-digit-number-into-a-double-digits-string
            print(f'Hull armour remaining:    \x1b[96m{hull_plates_remaining:02}\033[0m                       Shot accuracy:           \x1b[96m{shot_accuracy:02}%\033[0m')
            print(f'Enemy ships remaining:    \x1b[96m{(len(enemy_ship_locations)):02}\033[0m                   (\x1b[92mE\x1b[0m) Enemy ships destroyed:    \x1b[96m{enemy_ships_destroyed:02}\033[0m')
            print(f'Merchant ships remaining: \x1b[96m{(len(merchant_ship_locations)):02}\033[0m                   (\x1b[93mM\x1b[0m) Merchant ships destroyed: \x1b[96m{merchant_ships_destroyed:02}\033[0m')
            print('\n')
            col_headers = []                                                  
            for i in range(7):                                                 
                col_headers.append(i)                                         
            col_headers.insert(0, " ")                                        
            print("                             ", *col_headers, sep = ' ')   
            row_counter = 0
            for row_array in battle_grid: 
                print("                             ", row_counter, end = " ")
                row_counter += 1
                for col_elem in row_array:
                    print(col_elem, end = " ")
                print()
            print('\x1b[92mWEAPONS READY\x1b[0m')
            user_x_coord = input('\nEnter row to fire upon: (enter coordinate between \x1b[93m0\033[0m and \x1b[93m6\033[0m) \n')


        ### 4. PROMPTS USER TO ENTER VALID Y COORDINATE INPUT (WHILE LOOP VALIDATES) ###
        user_y_coord = input('Enter column to fire upon: \n')

        while user_y_coord not in valid_shot_inputs:
            clearscreen()
            print('--------------------- \x1b[96mBattleship Operations SITREP Display\033[0m ---------------------\n')
            #sleep(0.5)
            #clearscreen()
            shot_accuracy = int((enemy_ships_destroyed / len(total_shots)) * 100) if len(total_shots) > 0 else 0
            print(f'Torpedos remaining:       \x1b[96m{torpedo_count:02}\033[0m                   (\x1b[90mX\x1b[0m) Missed shots:             \x1b[96m{(len(miss_locations)):02}\033[0m')   # Note for bug resolved, https://stackoverflow.com/questions/3505831/in-python-how-do-i-convert-a-single-digit-number-into-a-double-digits-string
            print(f'Hull armour remaining:    \x1b[96m{hull_plates_remaining:02}\033[0m                       Shot accuracy:           \x1b[96m{shot_accuracy:02}%\033[0m')
            print(f'Enemy ships remaining:    \x1b[96m{(len(enemy_ship_locations)):02}\033[0m                   (\x1b[92mE\x1b[0m) Enemy ships destroyed:    \x1b[96m{enemy_ships_destroyed:02}\033[0m')
            print(f'Merchant ships remaining: \x1b[96m{(len(merchant_ship_locations)):02}\033[0m                   (\x1b[93mM\x1b[0m) Merchant ships destroyed: \x1b[96m{merchant_ships_destroyed:02}\033[0m')
            print('\n')
            col_headers = []                                                  
            for i in range(7):                                                 
                col_headers.append(i)                                         
            col_headers.insert(0, " ")                                        
            print("                             ", *col_headers, sep = ' ')   
            row_counter = 0
            for row_array in battle_grid: 
                print("                             ", row_counter, end = " ")
                row_counter += 1
                for col_elem in row_array:
                    print(col_elem, end = " ")
                print()
            print('\x1b[92mWEAPONS READY\x1b[0m')
            print('\nEnter row to fire upon: ')
            print(user_x_coord)
            user_y_coord = input('Enter column to fire upon: (enter coordinate between \x1b[93m0\033[0m and \x1b[93m6\033[0m) \n')

        ### 5. ASSIGNS VALID X AND Y COORDINATE INPUTS to USER SHOT ###
        user_shot = [int(user_x_coord), int(user_y_coord)]
        torpedo_count -= 1
        total_shots.append(user_shot) # Debug, delete when ready


        ### 6. CHECKS IF USER SHOT IS IN ENEMY SHIPS LOCATIONS LIST ###
        if user_shot in enemy_ship_locations:
            print('\033[?25l', end="") # Code to hide cursor credited in README.md
            typing_effect('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \r', 0.005)
            for iterations in range(4):
                print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m \x1b[42m\x1b[97m\x1b[1m    ENEMY SHIP DESTROYED    \x1b[0m\r', end="", flush=True)
                sleep(0.15)
                print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m \x1b[7m\x1b[42m\x1b[97m\x1b[1m    ENEMY SHIP DESTROYED    \x1b[0m\r', end="", flush=True)
                sleep(0.15)
            print('\033[?25h', end="") # Code to show cursor credited in README.md
            enemy_ship_locations.remove(user_shot)
            battle_grid[int(user_x_coord)][int(user_y_coord)] = '\x1b[92mE\x1b[0m'
            enemy_ships_destroyed += 1

        ### 7. CHECKS IF USER SHOT IS IN MERCHANT SHIPS LOCATIONS LIST ###
        elif user_shot in merchant_ship_locations:
            print('\033[?25l', end="") # Code to hide cursor credited in README.md
            typing_effect('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \r', 0.005)
            for iterations in range(4):
                print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m \x1b[103m\x1b[30m\x1b[1m  MERCHANT SHIP DESTROYED   \x1b[0m\r', end="", flush=True)
                sleep(0.15)
                print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m \x1b[7m\x1b[103m\x1b[30m\x1b[1m  MERCHANT SHIP DESTROYED   \x1b[0m\r', end="", flush=True)
                sleep(0.15)
            print('\033[?25h', end="") # Code to show cursor credited in README.md
            merchant_ship_locations.remove(user_shot)
            battle_grid[int(user_x_coord)][int(user_y_coord)] = '\x1b[93mM\x1b[0m'
            merchant_ships_destroyed += 1
        
        ### 8. ELSE IT IS A MISS ###
        else:
            print('\033[?25l', end="") # Code to hide cursor credited in README.md
            typing_effect('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \r', 0.005)
            for iterations in range(3):
                print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m \x1b[107m \x1b[30m       \x1b[1mTARGET MISSED       \x1b[0m\r', end="", flush=True)
                sleep(0.15)
                print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m \x1b[107m \x1b[30m       \x1b[1mTARGET MISSED       \x1b[0m\r', end="", flush=True)
                sleep(0.15)
            print('\033[?25h', end="") # Code to show cursor credited in README.md
            miss_locations.append(user_shot)
            # The condition below will prevent overwriting 
            # an enemy ship hit or merchant ship hit symbol
            if battle_grid[int(user_x_coord)][int(user_y_coord)] == '\x1b[96m~\033[0m':
                battle_grid[int(user_x_coord)][int(user_y_coord)] = '\x1b[90mX\x1b[0m'

        ### 9. ENEMY SHOT IS GENERATED BY COMPUTER, IF ENEMY SHIPS ARE STILL AFLOAT ###
        if len(enemy_ship_locations) > 0 and len(merchant_ship_locations) > 0 and torpedo_count >= int(len(enemy_ship_locations)):
            clearscreen()
            print('--------------------- \x1b[96mBattleship Operations SITREP Display\033[0m ---------------------\n')
            #sleep(0.5)
            #clearscreen()
            print('\033[?25l', end="") # Code to hide cursor credited in README.md
            shot_accuracy = int((enemy_ships_destroyed / len(total_shots)) * 100) if len(total_shots) > 0 else 0
            print(f'Torpedos remaining:       \x1b[96m{torpedo_count:02}\033[0m                   (\x1b[90mX\x1b[0m) Missed shots:             \x1b[96m{(len(miss_locations)):02}\033[0m')   # Note for bug resolved, https://stackoverflow.com/questions/3505831/in-python-how-do-i-convert-a-single-digit-number-into-a-double-digits-string
            print(f'Hull plates remaining:    \x1b[96m{hull_plates_remaining:02}\033[0m                       Shot accuracy:           \x1b[96m{shot_accuracy:02}%\033[0m')
            print(f'Enemy ships remaining:    \x1b[96m{(len(enemy_ship_locations)):02}\033[0m                   (\x1b[92mE\x1b[0m) Enemy ships destroyed:    \x1b[96m{enemy_ships_destroyed:02}\033[0m')
            print(f'Merchant ships remaining: \x1b[96m{(len(merchant_ship_locations)):02}\033[0m                   (\x1b[93mM\x1b[0m) Merchant ships destroyed: \x1b[96m{merchant_ships_destroyed:02}\033[0m')
            print('\n')
            col_headers = []                                                  
            for i in range(7):                                                 
                col_headers.append(i)                                         
            col_headers.insert(0, " ")                                        
            print("                             ", *col_headers, sep = ' ')   
            row_counter = 0
            for row_array in battle_grid: 
                print("                             ", row_counter, end = " ")
                row_counter += 1
                for col_elem in row_array:
                    print(col_elem, end = " ")
                print()
            sleep(0.3)
            print('\n\n\n\n')
            for iterations in range(3):
                
                print('\x1b[91m\x1b[1mALERT!!! ENEMY TORPEDO IN THE WATER\033[0m\r', end="", flush=True)
                sleep(0.08)  
                print('\x1b[91mALERT!!! ENEMY TORPEDO IN THE WATER\033[0m\r', end="", flush=True)
                sleep(0.08)
            print('\033[?25h', end="") # Code to show cursor credited in README.md
            enemy_shot_x_coor = (randint(0, 6))
            enemy_shot_y_coor = (randint(0, 6))
            enemy_shot = [int(enemy_shot_x_coor)] + [int(enemy_shot_y_coor)]
            enemy_shots.append(enemy_shot)

            ### 10. CHECKS IF ENEMY SHOT IS IN MERCHANT SHIP LIST ###
            if enemy_shot in merchant_ship_locations:
                print('\033[?25l', end="") # Code to hide cursor credited in README.md
                typing_effect('\n\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \r', 0.005)
                for iterations in range(4):
                    print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m \x1b[103m\x1b[30m\x1b[1m  MERCHANT SHIP DESTROYED   \x1b[0m\r', end="", flush=True)
                    sleep(0.15)
                    print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m \x1b[7m\x1b[103m\x1b[30m\x1b[1m  MERCHANT SHIP DESTROYED   \x1b[0m\r', end="", flush=True)
                    sleep(0.15)
                print('\033[?25h', end="") # Code to show cursor credited in README.md
                merchant_ship_locations.remove(enemy_shot)
                battle_grid[int(enemy_shot_x_coor)][int(enemy_shot_y_coor)] = '\x1b[93mM\x1b[0m'
                merchant_ships_destroyed += 1

            ### 11. CHECKS IF ENEMY SHOT IS IN BATTLESHIP HULL LIST ###    
            elif enemy_shot in battleship_hull_locations:
                print('\033[?25l', end="") # Code to hide cursor credited in README.md
                typing_effect('\n\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \r', 0.005)
                for iterations in range(4):
                    print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m \033[41m\033[37m\033[1m       BATTLESHIP HIT       \x1b[0m\r', end="", flush=True)
                    sleep(0.15)
                    print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m \x1b[7m\033[41m\033[37m\033[1m       BATTLESHIP HIT       \x1b[0m\r', end="", flush=True)
                    sleep(0.15)
                print('\033[?25h', end="") # Code to show cursor credited in README.md
                battleship_hull_locations.remove(enemy_shot)
                hull_plates_remaining -= 1

            ### 12. ELSE IT IS A MISS ###    
            else:
                print('\033[?25l', end="") # Code to hide cursor credited in README.md
                typing_effect('\n\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m   \r', 0.005)
                for iterations in range(3):
                    print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m \x1b[107m \x1b[30m        \x1b[1mENEMY MISSED       \x1b[0m\r', end="", flush=True)
                    sleep(0.15)
                    print('\x1b[96m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m \x1b[107m \x1b[30m        \x1b[1mENEMY MISSED       \x1b[0m\r', end="", flush=True)
                    sleep(0.15)
                print('\033[?25h', end="") # Code to show cursor credited in README.md
                enemy_misses.append(enemy_shot)
        

def end_game_conditions():
    """
    The end game conditions function will check for conditions
    that are present relating to either a mission success or
    mission failure. If the enemy ships have all been destroyed
    while there are still merchant ships afloat, it will result
    in mission success. Any other scenario will be considered
    a mission failure. A narrative for both outcomes is displayed
    to the user, along with options to either restart the game
    or exit the program.
    """
    sleep(0.5)

    # NARRATIVE FOR MISSION SUCCESS IS SHOWN BELOW
    if len(enemy_ship_locations) == 0 and len(merchant_ship_locations) > 0:
        clearscreen()
        print('\n\n\n\n\n\n\n\n\n\x1b[1m             Battle \
Update : \x1b[96mEnemy Ships Destroyed\x1b[0m\n')
        for iterations in range(20):
            print('             \x1b[1mMission Status:\
\x1b[0m \x1b[1m\x1b[92mSuccess\x1b[0m\r', end="", flush=True)
            sleep(0.1)
            print('             \x1b[1mMission Status:\
\x1b[0m \x1b[97mSuccess\x1b[0m\r', end="", flush=True)
            sleep(0.1)
        clearscreen()
        sleep(0.2)
        print('\033[?25l', end="")  # Code to hide cursor credited in README.md
        typing_effect(f'''\n    {username},
        We've received confirmation that the merchant ships have been destroyed.
        The cargo has been lost, there is nothing more we can do. Your orders are
        to stand down. All communication channels have been opened and made
        available to the Meridian Queen. Have your crew contact loved ones, or
        make their peace in whichever way they choose.\n
        We have lost this war, but so has the enemy. 4 minutes ago the
        Oppenheimer Protocol was activated. Our last remaining ICBMs were
        equipped with the experimental 'Hades' warhead and are currently en route
        to targets of strategic value within enemy territory. The enemy has
        already reciprocated in kind. Our analysts predict that small pockets of
        humanity around the globe will survive the initial blasts and subsequent
        fallout in just enough numbers to prevent the extinction of our species.
        \n    May the survivors be granted wisdom beyond our own.\n\n''', 0.03)
        sleep(3)
        print('    God forgive us.\n')
        sleep(2)
        print('\033[?25h', end="")  # Code to show cursor credited in README.md
        valid_end_game_choices = ['r', 'e']
        end_game_prompt = print("         Type 'R' to return to the start \
screen, or 'E' to exit program\n")
        end_game_choice = input("                                       ")
        end_game_choice = end_game_choice.lower()
        while end_game_choice not in valid_end_game_choices:
            clearscreen()
            print(f'''\n    {username},
        We've received confirmation that the merchant ships have been destroyed.
        The cargo has been lost, there is nothing more we can do. Your orders are
        to stand down. All communication channels have been opened and made
        available to the Meridian Queen. Have your crew contact loved ones, or
        make their peace in whichever way they choose.\n
        We have lost this war, but so has the enemy. 4 minutes ago the
        Oppenheimer Protocol was activated. Our last remaining ICBMs were
        equipped with the experimental 'Hades' warhead and are currently en route
        to targets of strategic value within enemy territory. The enemy has
        already reciprocated in kind. Our analysts predict that small pockets of
        humanity around the globe will survive the initial blasts and subsequent
        fallout in just enough numbers to prevent the extinction of our species.
            \n    May the survivors be granted wisdom beyond our own.\n''')
            print('    God forgive us.\n')
            end_game_prompt = print("     \x1b[93mAlert!!\x1b[0m Type '\x1b[93mR\
\x1b[0m' to return to the start screen, or '\x1b[93mE\
\x1b[0m' to exit program\n")
            end_game_choice = input("                                       ")
            end_game_choice = end_game_choice.lower()

        if end_game_choice == "r":
            main()
        else:
            sleep(0.3)
            clearscreen()
            sleep(0.2)
            print('\n\n\n\n\n\n\n\n\n')
            print('                       \x1b[96mDisconnect\
ing from Central Command\x1b[1m')
            sleep(4)
            clearscreen()
            raise SystemExit()


    # NARRATIVE FOR MISSION FAILURE IS SHOWN BELOW
    else:
        clearscreen()
        if torpedo_count < int(len(enemy_ship_locations)):
            print('\n\n\n\n\n\n\n\n\n\x1b[1m             Battle \
Update : \x1b[96mTorpedo Quantity Insufficient\x1b[0m\n')
            for iterations in range(20):
                print('             \x1b[1mMission Status:\
\x1b[0m \x1b[1m\x1b[91mFailed\x1b[0m\r', end="", flush=True)
                sleep(0.1)
                print('             \x1b[1mMission Status:\
\x1b[0m \x1b[97mFailed\x1b[0m\r', end="", flush=True)
                sleep(0.1)
        elif torpedo_count == 0 and int(len(enemy_ship_locations)) > 0:
            print('\n\n\n\n\n\n\n\n\n\x1b[1m                  Battle \
Update : \x1b[96mTorpedo Complement Exhausted\x1b[0m\n')
            for iterations in range(20):
                print('                  \x1b[1mMission Status:\
\x1b[0m \x1b[1m\x1b[91mFailed\x1b[0m\r', end="", flush=True)
                sleep(0.1)
                print('                  \x1b[1mMission Status:\
\x1b[0m \x1b[97mFailed\x1b[0m\r', end="", flush=True)
                sleep(0.1)
        elif len(merchant_ship_locations) == 0:
            print('\n\n\n\n\n\n\n\n\n\x1b[1m                  Battle \
Update : \x1b[96mAll Merchant Ships Destroyed\x1b[0m\n')
            for iterations in range(20):
                print('                  \x1b[1mMission Status:\
\x1b[0m \x1b[1m\x1b[91mFailed\x1b[0m\r', end="", flush=True)
                sleep(0.1)
                print('                  \x1b[1mMission Status:\
\x1b[0m \x1b[97mFailed\x1b[0m\r', end="", flush=True)
                sleep(0.1)
        else:
            print('\n\n\n\n\n\n\n\n\n\x1b[1m                    Battle \
Update : \x1b[96mBattleship Hull Breached\x1b[0m\n')
            for iterations in range(25):
                print('                    \x1b[1mMission Status:\
\x1b[0m \x1b[1m\x1b[91mFailed\x1b[0m\r', end="", flush=True)
                sleep(0.1)
                print('                    \x1b[1mMission Status:\
\x1b[0m \x1b[97mFailed\x1b[0m\r', end="", flush=True)
                sleep(0.1)
        clearscreen()
        sleep(0.2)
        print('\033[?25l', end="")  # Code to hide cursor credited in README.md
        typing_effect(f'''\n    {username},
    We've received confirmation that the merchant ships have been destroyed.
    The cargo has been lost, there is nothing more we can do. Your orders are
    to stand down. All communication channels have been opened and made
    available to the Meridian Queen. Have your crew contact loved ones, or
    make their peace in whichever way they choose.\n
    We have lost this war, but so has the enemy. 4 minutes ago the
    Oppenheimer Protocol was activated. Our last remaining ICBMs were
    equipped with the experimental 'Hades' warhead and are currently en route
    to targets of strategic value within enemy territory. The enemy has
    already reciprocated in kind. Our analysts predict that small pockets of
    humanity around the globe will survive the initial blasts and subsequent
    fallout in just enough numbers to prevent the extinction of our species.
        \n    May the survivors be granted wisdom beyond our own.\n\n''', 0.03)
        sleep(3)
        print('    God forgive us.\n')
        sleep(2)
        print('\033[?25h', end="")  # Code to show cursor credited in README.md
        valid_end_game_choices = ['r', 'e']
        end_game_prompt = print("         Type 'R' to return to the start \
screen, or 'E' to exit program\n")
        end_game_choice = input("                                       ")
        end_game_choice = end_game_choice.lower()
        while end_game_choice not in valid_end_game_choices:
            clearscreen()
            print(f'''\n    {username},
    We've received confirmation that the merchant ships have been destroyed.
    The cargo has been lost, there is nothing more we can do. Your orders are
    to stand down. All communication channels have been opened and made
    available to the Meridian Queen. Have your crew contact loved ones, or
    make their peace in whichever way they choose.\n
    We have lost this war, but so has the enemy. 4 minutes ago the
    Oppenheimer Protocol was activated. Our last remaining ICBMs were
    equipped with the experimental 'Hades' warhead and are currently en route
    to targets of strategic value within enemy territory. The enemy has
    already reciprocated in kind. Our analysts predict that small pockets of
    humanity around the globe will survive the initial blasts and subsequent
    fallout in just enough numbers to prevent the extinction of our species.
            \n    May the survivors be granted wisdom beyond our own.\n''')
            print('    God forgive us.\n')
            end_game_prompt = print("     \x1b[93mAlert!!\x1b[0m Type '\x1b[93mR\
\x1b[0m' to return to the start screen, or '\x1b[93mE\
\x1b[0m' to exit program\n")
            end_game_choice = input("                                       ")
            end_game_choice = end_game_choice.lower()

        if end_game_choice == "r":
            main()
        else:
            sleep(0.3)
            clearscreen()
            sleep(0.2)
            print('\n\n\n\n\n\n\n\n\n')
            print('                       \x1b[96mDisconnect\
ing from Central Command\x1b[1m')
            sleep(4)
            clearscreen()
            raise SystemExit()


def main():
    """
    The main function will trigger all
    functions necessary to run the game
    """
    # Displays start screen
    start_screen()
    # Validates username input
    validate_username_screen()
    # Requests user to select difficulty
    mission_difficulty_screen()
    # Initialises the starting game values
    initialise_game_values()
    # Displays mission details with prompt
    mission_accept_screen()
    # Creates battleship hull locations
    generate_battleship_hull_hit_locations()
    # Creates enemy ship locations
    generate_enemy_ship_locations()
    # Creates merchant ship locations
    generate_merchant_ship_locations()
    # Displays battleship information to user
    sitrep_loading()
    # Contains the core game mechanics and logic
    game_screen()
    # Checks for end game conditions
    end_game_conditions()


main()
