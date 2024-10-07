import os
from time import sleep

print('Welcome to Make a Robot!')
print('-' * 33)

parts = {
        'heads': {
            1: 'Thermo-Scope Visor',
            2: 'Audio Disruptor Headset',
            3: 'Cerebral Relay Node'
        },
        'torso': {
            1: 'Energy Core Chestplate',
            2: 'Magnetic Manipulator Torso',
            3: 'Data Processor Module'
        },
        'legs': {
            1: 'Hydraulic Strider Legs',
            2: 'Spider Walker Legs',
            3: 'Rocket-Propelled legs'
        }
    }

arts = {
    'heads_arts': {
        1: f'1. {parts['heads'][1]}' 
        '''
         ____
        /    \\
       | -  - |
       |  O   |
        \\____/
        ''',
        2: f'2. {parts['heads'][2]}' 
        '''
         _|_
        (O O)
        | - |
        ''',
        3: f'3. {parts['heads'][3]}' 
        '''
         ____
        (o_o)
        /_=_\\
        '''
    },
    'torso_arts': {
        1: f'1. {parts['torso'][1]}' 
        '''
        /O\\
        |O|
        \\O/                  
        ''',
        2: f'2. {parts['torso'][2]}' 
        '''
        /M\\
        |+|
        \\M/
        ''',
        3: f'3. {parts['torso'][3]}' 
        '''
        /-\\
       |[=]|
        \\-/
        '''
    },
    'legs_arts': {
        1: f'1. {parts['legs'][1]}' 
        '''
         |
        /|\\
        / \\
        ''',
        2: f'2. {parts['legs'][2]}' 
        '''
        | |
       /   \\
       /   \\
        ''',
        3: f'3. {parts['legs'][3]}'
        '''
         | 
        / \\
        |=|
        '''
    }
}
arts_with_names = {
    'heads_arts': {
        1: 
        '''
        ____
       /    \\
      | -  - |
      |  O   |
       \\____/''',
        2:
        '''
        _|_
       (O O)
       | - |''',
        3:
        '''
        ____
       (o_o)
       /_=_\\''',
    },
    'torso_arts': {
        1:
        '''
        /O\\
        |O|
        \\O/''',
        2:
        '''
        /M\\
        |+|
        \\M/''',
        3:
        '''
        /-\\
       |[=]|
        \\-/'''
    },
    'legs_arts': {
        1:
        '''
         |
        /|\\
        / \\''',
        2:
        '''
        | |
       /   \\
       /   \\''',
        3:
        '''
         | 
        / \\
        |=|'''
    }
}

def robotDrawer(choosed_head, choosed_torso, choosed_legs, robotName):
    print('Wait for your robot to be created...')
    for i in range(5):
        time_to_wait = 5 - i
        print(f'{time_to_wait}...')
        sleep(1)

    print('Your robot is ready!')
    print(robotName)
    print(f'{arts_with_names['heads_arts'][choosed_head]}{arts_with_names['torso_arts'][choosed_torso]}{arts_with_names['legs_arts'][choosed_legs]}')

def robotMaker(robotName):
    print('Choose robot parts to make your robot!')
    print('Heads:')
    # head chooser
    for i in arts['heads_arts']:
        print(arts['heads_arts'][i])
    choosed_head = input()
    try:
        choosed_head = int(choosed_head)
    except ValueError as err:
        print('Choose a number between 1 and 3!')
        robotMaker()
    if 1 <= choosed_head <= 3:
        match choosed_head:
            case 1:
                print(f'You\'ve choosed a {parts["heads"][1]} head')
            case 2:
                print(f'You\'ve choosed a {parts["heads"][2]} head')
            case 3:
                print(f'You\'ve choosed a {parts["heads"][3]} head')
    else:
        print('Choose a number between 1 and 3!')
        robotMaker()
    # torso chooser
    for i in arts['torso_arts']:
        print(arts['torso_arts'][i])
    choosed_torso = input()
    try:
        choosed_torso = int(choosed_torso)
    except ValueError as err:
        print('Choose a number between 1 and 3!')
        robotMaker()
    if 1 <= choosed_torso <= 3:
        match choosed_torso:
            case 1:
                print(f'You\'ve choosed a {parts["torso"][1]} torso')
            case 2:
                print(f'You\'ve choosed a {parts["torso"][2]} torso')
            case 3:
                print(f'You\'ve choosed a {parts["torso"][3]} torso')
    else:
        print('Choose a number between 1 and 3!')
        robotMaker()
    # legs chooser
    for i in arts['legs_arts']:
        print(arts['legs_arts'][i])
    choosed_legs = input()
    try:
        choosed_legs = int(choosed_legs)
    except ValueError as err:
        print('Choose a number between 1 and 3!')
        robotMaker()
    if 1 <= choosed_legs <= 3:
        match choosed_legs:
            case 1:
                print(f'You\'ve choosed a {parts["legs"][1]} legs')
            case 2:
                print(f'You\'ve choosed a {parts["legs"][2]} legs')
            case 3:
                print(f'You\'ve choosed a {parts["legs"][3]} legs')
    else:
        print('Choose a number between 1 and 3!')
        robotMaker()

    robotDrawer(choosed_head, choosed_torso, choosed_legs, robotName)

def robotNamer():
    robotNameVerifier = False
    while robotNameVerifier == False:
        robotName = input('Give a name for your robot: ')
        if robotName != '': # If name is not empty
            print(f'Your robot\'s name is {robotName}')
            robotNameVerifier = True
            return robotMaker(robotName)
        else: # If name is empty
            print('Input a robot\'s name!')

robotNamer()