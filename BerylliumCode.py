import random

def main():

    headingrotas()

    print('''
          Hello traveller, welcome to Realm of the Arcane Scribes, I hope you are ready for your adventure!
          This is a terminal based game created by ...
          ''')
    
    ### Choose the character from the function
    print('The first of many choices start here:')
    usercharacter = characterchoice()
    print(f'You have chosen to play this adventure as a {usercharacter}')

    ### Chose the location of play
    location = areaofplay()
    print(f'I see you have decided to choose {location}, you must be brave, I hope you are ready to fight for your survival!')

    if location == 'cave':
        finalchoice = caveroute()
    elif location == 'forrest':
        finalchoice = forrestroute()
    else:
        print('Not a valid option')

    if finalchoice == 'attack':
        print('You win! Congratulations!')
    elif finalchoice == 'run':
        print('You lost sorry!')

def characterchoice():
    usercharacter = input(str("Please choose between a Human or an Orc?: ")).title()
    return usercharacter

def areaofplay():
    location = input(str("Now for the first choice brave traveller ... forrest or cave? Which would you like to conquer? ")).lower()
    return location

def caveroute():
    print('''
    I see you have chosen the scary cave as a starting point. 
    You start with 100 base health points, if you take damage you will lose health and possibly die!
    ''')
    
    userhealth = 100

    ### Optimized random selection
    enemy = random.choice(['skeleton', 'bat', 'troll'])
    print(f'''
          Ahhh, a {enemy} is attacking, what do you do? Attack or run?
          ''')
    choice = input().lower()

    finalchoice = fightingenemy(enemy, choice, userhealth)

    return finalchoice

## Defining combat function outside of caveroute
def fightingenemy(enemy, choice, userhealth):
    
    ### Added enemy hp and damage
    if enemy == 'goblin':
        enemyhp, enemydamage = 2, 20
    elif enemy == 'tree monster':
        enemyhp, enemydamage = 5, 50
    elif enemy == 'giant':
        enemyhp, enemydamage = 7, 70
    elif enemy == 'bat':
        enemyhp, enemydamage = 2, 20
    elif enemy == 'skeleton':
        enemyhp, enemydamage = 5, 50
    elif enemy == 'troll':
        enemyhp, enemydamage = 7, 70

    ### Combat loop
    if choice == 'attack':    
        while enemyhp > 0 and userhealth > 0:
            if choice == 'attack':
                attackroll = random.randint(1,10)
                print(f'You attack the {enemy} and dealt {attackroll} damage!')

                enemyhp = enemyhp - attackroll

                if enemyhp > 0:
                    print(f'The {enemy} attacks you!')
                    userhealth = userhealth - enemydamage
                    print(f'You take {enemydamage} damage, your health is now {userhealth}')

            if userhealth <= 0:
                print('You have been defeated!')
                return

        if enemyhp <= 0:
            print(f'You defeated the {enemy}!')
    
    elif choice == 'run':
        print('You decided to run!')

    return choice

def forrestroute():
    print('''
    I see you have chosen the spooky forrest as a starting point. 
    You start with 100 base health points, if you take damage you will lose health and possibly die!
    ''')
    
    userhealth = 100

    ### Optimized random selection
    enemy = random.choice(['tree monster', 'goblin', 'giant'])
    print(f'''
          Ahhh, a {enemy} is attacking, what do you do? Attack or run?
          ''')
    choice = input().lower()

    finalchoice = fightingenemy(enemy, choice, userhealth)

    return finalchoice


def headingrotas():
    print("""""
  _____            _                    __   _   _                                                 _____           _ _               
 |  __ \          | |                  / _| | | | |              /\                               / ____|         (_) |              
 | |__) |___  __ _| |_ __ ___     ___ | |_  | |_| |__   ___     /  \   _ __ ___ __ _ _ __   ___  | (___   ___ _ __ _| |__   ___  ___ 
 |  _  // _ \/ _` | | '_ ` _ \   / _ \|  _| | __| '_ \ / _ \   / /\ \ | '__/ __/ _` | '_ \ / _ \  \___ \ / __| '__| | '_ \ / _ \/ __|
 | | \ \  __/ (_| | | | | | | | | (_) | |   | |_| | | |  __/  / ____ \| | | (_| (_| | | | |  __/  ____) | (__| |  | | |_) |  __/\__ |
 |_|  \_\___|\__,_|_|_| |_| |_|  \___/|_|    \__|_| |_|\___| /_/    \_\_|  \___\__,_|_| |_|\___| |_____/ \___|_|  |_|_.__/ \___||___/                                                                                                                                  
    """)

main()