import random
log = open('storygamelog.txt', 'w+')
story = open('storygame.txt', 'w+')
global character
hp = 100
Mana = 100
print(f'''--------------------------------------------------------------------------
 Welcome to the game, select a character! 
 [1] Mary
 [2] Oberon 
 [3] Terra 
--------------------------------------------------------------------------''')
bob = True
while True:
    while bob:
        try:
            character = int(input('Character: '))
            bob = False
        except ValueError:
            print('''select a character from the list please''')
    if character == 1:
        log.write('''User picked 'Mary' as a character\n''')
        story.write('Mary is going on an adventure\n')
        character = 'Mary'
        break
    elif character == 2:
        log.write('''User picked 'Oberon' as a character\n''')
        story.write('Oberon is going on an adventure\n')
        character = 'Oberon'
        break
    elif character == 3:
        log.write('''User picked 'Terra' as a character\n''')
        story.write('Terra is going on an adventure\n')
        character = 'Terra'
        break
    else:
        print('Pick a character please')
        bob = True

#
def eventrules():
    global eventchosen, events, event
    events = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    eventchosen = random.choice(events)
    event = ' '
    if eventchosen == 1:
        event = f'{character} has encountered a mountain\n'
    elif eventchosen == 2:
        event = f'{character} has encountered a group of elves\n'
    elif eventchosen == 3:
        event = f'{character} has encountered a dragon\n'
    elif eventchosen == 4:
        event = f'{character} has encountered a small group of mages\n'
    elif eventchosen == 5:
        event = f'{character} has arrived at a rest point\n'
    elif eventchosen == 6:
        event = f'{character} has arrived at a city of elves\n'
    elif eventchosen == 7:
        event = f'{character} has arrived at a city of dragons\n'
    elif eventchosen == 8:
        event = f'{character} has arrived at a mage academy\n'
    elif eventchosen == 9:
        event = f'{character} has entered the sleeping forest\n'
    elif eventchosen == 10:
        event = f'{character} has encountered a mine (of mmmmooooorrrriiaaa)\n'
    log.write(f'''Event number {eventchosen} was chosen, this is the '{event}'\n''')
    story.write(f'{event} \n')
def gamechoicerules():
    global choiceone, choicetwo, choicethree, choicefour
    choiceone = 'undefined'
    choicetwo = 'undefined'
    choicethree = 'undefined'
    choicefour = 'undefined'
    if eventchosen == 1:
        print(eventchosen)
        if character == 'Mary':
            choiceone = 'Scale the cliff'
            choicetwo = 'Try to find another way around the mountain'
            choicethree = 'Go find another path that does involve the mountain'
            choicefour = 'Attempt to hover over the mountain'
        elif character == 'Oberon':
            choiceone = 'Scale the cliff'
            choicetwo = 'Try to find another way around the mountain'
            choicethree = 'Go find another path that does involve the mountain'
            choicefour = 'No special available'
        elif character == 'Terra':
            choiceone = 'Scale the cliff'
            choicetwo = 'Try to find another way around the mountain'
            choicethree = 'Go find another path that does involve the mountain'
            choicefour = 'Fly over the mountain'
    elif eventchosen == 2:
        print(eventchosen)
        if character == 'Mary':
            choiceone = 'Attack'
            choicetwo = 'Say hi'
            choicethree = 'Sneak past them'
            choicefour = 'No special available'
        elif character == 'Oberon':
            choiceone = 'Attack'
            choicetwo = 'Say hi'
            choicethree = 'Sneak past them'
            choicefour = 'Ask them to upgrade your Bow'
        elif character == 'Terra':
            choiceone = 'Attack'
            choicetwo = 'Unavailable'
            choicethree = 'Sneak past them'
            choicefour = 'No special available'
    elif eventchosen == 3:
        print(eventchosen)
        if character == 'Mary':
            choiceone = 'Attack'
            choicetwo = 'Unavailable'
            choicethree = 'Sneak past it'
            choicefour = 'Launch a killing spell at it'
    elif eventchosen == 4:
        print(eventchosen)
        if character == 'Mary':
            choiceone = 'Attack'
            choicetwo = 'Say hi'
            choicethree = 'Sneak past them'
            choicefour = 'Ask them for a chance to rest'
    elif eventchosen == 5:
        print(eventchosen)
        if character == 'Mary':
            choiceone = 'Rest and regenerate health'
            choicetwo = 'Rest and regenerate Mana'
            choicethree = 'Move on'
            choicefour = 'No special available'
    elif eventchosen == 6:
        print(eventchosen)
        if character == 'Mary':
            choiceone = 'Say hi'
            choicetwo = 'Go past'
            choicethree = 'Attack'
            choicefour = 'No special available'
    elif eventchosen == 7:
        print(eventchosen)
        if character == 'Mary':
            choiceone = 'Attack'
            choicetwo = 'Unavailable'
            choicethree = 'Sneak past'
            choicefour = 'No special available'
    elif eventchosen == 8:
        print(eventchosen)
        if character == 'Mary':
            choiceone = 'Say hi'
            choicetwo = 'Eat and drink'
            choicethree = 'Go past'
            choicefour = 'Improve chances of spell success'
    elif eventchosen == 9:
        print(eventchosen)
        if character == 'Mary':
            choiceone = 'Enter'
            choicetwo = 'Go around'
            choicethree = 'Find another path that leads far away'
            choicefour = 'Cast a spell to avoid the curse of the forest'
    elif eventchosen == 10:
        print(eventchosen)
        if character == 'Mary':
            choiceone = '''Say 'They call it a mine' '''
            choicetwo = 'Look for a dwarf'
            choicethree = 'Look for an elf'
            choicefour = 'Summon a dwarf to guide you through the mines (of mmmmoooorrriiiaaaa)'
def gameuserchoicerules():
    global gamechoice
    tom = True
    while tom:
        try:
            gamechoice = int(input('What will you choose to do now? '))
            tom = False
        except ValueError:
            print('select a choice from the list')
        finally:
            if gamechoice == 1:
                'bob'
                tom = False
            elif gamechoice == 2:
                'bob'
                tom = False
            elif gamechoice == 3:
                'bob'
                tom = False
            elif gamechoice == 4:
                'bob'
                tom = False
            else:
                print('select a choice from the list')
playing = True
continued = 0
counter = 0
cardinel = True
while playing:
    cardinel = True
    eventrules()
    gamechoicerules()
    print(f'''-----------------------
{event}
[1] {choiceone}
[2] {choicetwo}
[3] {choicethree}
[4] {choicefour}
-----------------------''')
    gameuserchoicerules()
    story.write(f'{character} decided to {gamechoice}')
    counter += 1
    if counter == 10:
        while cardinel:

            if continued == 4:
                print(f'''-----------------------------------------
{character} finished their journey,
discovering many new places and
meeting many new people, 
they now continue 
going out on adventures after 
fulfilling their first one they 
got a taste for it and continued searched
for that experience again
-----------------------------------------''')
                story.write(f'''{character} finished their journey,
discovering many new places and
meeting many new people, 
they now continue 
going out on adventures after 
fulfilling their first one they 
got a taste for it and continued searched
for that experience again''')
                log.write('End of Game')
                cardinel = False
                playing = False
            else:
                choice = input('continue playing? [y/n]')
                if choice.upper() == 'N':
                    print(f'''-----------------------------------------
{character} decided to retire and go home,
to live for the rest of their life not
knowing what or who they would have
met later on in their journey
-----------------------------------------''')
                    log.write('End of Game')
                    story.write(f'''
{character} decided to retire and go home,
to live for the rest of their life not
knowing what or who they would have
met later on in their journey
''')
                    counter = 0
                    cardinel = False
                    playing = False
                elif choice.upper() == 'Y':
                    log.write('Game continued')
                    story.write(f'''
{character} decided to press on with their adventure
''')
                    print(f'''-----------------------------------------
{character} decided to press on with their adventure
-----------------------------------------''')
                    counter = 0
                    continued += 1
                    cardinel = False
                else:
                    print('Please enter either y or n')