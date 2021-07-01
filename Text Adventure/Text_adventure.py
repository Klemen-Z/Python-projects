import random, json, Battle_function
log = open('storygamelog.txt', 'w+')
story = open('storygame.txt', 'w+')
global hp, character, mana, mana_regeneration
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
        hp = 100
        mana = 200
        mana_regeneration = 10
        log.write('''User picked 'Mary' as a character\n''')
        story.write('Mary is going on an adventure\n')
        character = 'Mary'
        json.dump({
            "character": "Mary",
            "hp": 100,
            "mana": 200,
            "mana_regeneration": 10,
            "enemy one": 180,
            "enemy two": 70,
            "enemy three": 90,
            "damage one": 20,
            "damage two": 5,
            "damage three": 10,
            "mana one": 50,
            "mana two": 100,
            "mana three": 175
        }, open("Information.json", "w"))
        break
    elif character == 2:
        hp = 75
        mana = 100
        mana_regeneration = 5
        log.write('''User picked 'Oberon' as a character\n''')
        story.write('Oberon is going on an adventure\n')
        character = 'Oberon'
        json.dump({
            "character": "Oberon",
            "hp": 75,
            "mana": 100,
            "mana_regeneration": 5,
            "enemy one": 180,
            "enemy two": 70,
            "enemy three": 90,
            "damage one": 20,
            "damage two": 5,
            "damage three": 10,
            "mana one": 50,
            "mana two": 100,
            "mana three": 175
        }, open("Information.json", "w"))
        break
    elif character == 3:
        hp = 200
        mana = 50
        mana_regeneration = 5
        log.write('''User picked 'Terra' as a character\n''')
        story.write('Terra is going on an adventure\n')
        character = 'Terra'
        json.dump({
            "character": "Terra",
            "hp": 200,
            "mana": 50,
            "mana_regeneration": 5,
            "enemy one": 180,
            "enemy two": 70,
            "enemy three": 90,
            "damage one": 20,
            "damage two": 5,
            "damage three": 10,
            "mana one": 50,
            "mana two": 100,
            "mana three": 175
        }, open("Information.json", "w"))
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
        if character == 'Mary':
            choiceone = 'Attack'
            choicetwo = 'Say hi'
            choicethree = 'Sneak past them'
            choicefour = 'No special available'
        elif character == 'Oberon':
            choiceone = 'Attack'
            choicetwo = 'Say hi'
            choicethree = 'Sneak past them'
            choicefour = 'Ask them for a chance to rest'
        elif character == 'Terra':
            choiceone = 'Attack'
            choicetwo = 'Unavailable'
            choicethree = 'Sneak past them'
            choicefour = 'No special available'
    elif eventchosen == 3:
        if character == 'Mary':
            choiceone = 'Attack'
            choicetwo = 'Unavailable'
            choicethree = 'Sneak past it'
            choicefour = 'Launch a killing spell at it'
        elif character == 'Oberon':
            choiceone = 'Attack'
            choicetwo = 'Unavailable'
            choicethree = 'Sneak past it'
            choicefour = 'Sing it to sleep'
        elif character == 'Terra':
            choiceone = 'Attack'
            choicetwo = 'Try to intimidate it'
            choicethree = 'Sneak past them'
            choicefour = 'No special available'
    elif eventchosen == 4:
        if character == 'Mary':
            choiceone = 'Attack'
            choicetwo = 'Say hi'
            choicethree = 'Sneak past them'
            choicefour = 'Ask them for a chance to rest'
        elif character == 'Oberon':
            choiceone = 'Attack'
            choicetwo = 'Say hi'
            choicethree = 'Sneak past them'
            choicefour = 'No special available'
        elif character == 'Terra':
            choiceone = 'Attack'
            choicetwo = 'Unavailable'
            choicethree = 'Sneak past them'
            choicefour = 'Destroy them with your fiery breath'
    elif eventchosen == 5:
        choiceone = 'Rest and regenerate health'
        choicetwo = 'Rest and regenerate Mana'
        choicethree = 'Move on'
        choicefour = 'No special available'
    elif eventchosen == 6:
        if character == 'Mary':
            choiceone = 'Say hi'
            choicetwo = 'Go past'
            choicethree = 'Attack'
            choicefour = 'No special available'
        elif character == 'Oberon':
            choiceone = 'Say hi'
            choicetwo = 'Ignore them'
            choicethree = 'Attack'
            choicefour = 'Ask them for weapon upgrades'
        elif character == 'Terra':
            choiceone = 'Attack'
            choicetwo = 'Unavailable'
            choicethree = 'Fly past'
            choicefour = 'Grab loot'
    elif eventchosen == 7:
        if character == 'Mary':
            choiceone = 'Attack'
            choicetwo = 'Unavailable'
            choicethree = 'Sneak past'
            choicefour = 'No special available'
        elif character == 'Oberon':
            choiceone = 'Attack'
            choicetwo = 'Unavailable'
            choicethree = 'Sneak past'
            choicefour = 'No special available'
        elif character == 'Terra':
            choiceone = 'Attack'
            choicetwo = 'Unavailable'
            choicethree = 'Fly past'
            choicefour = 'Grab loot'
    elif eventchosen == 8:
        if character == 'Mary':
            choiceone = 'Say hi'
            choicetwo = 'Eat and drink'
            choicethree = 'Go past'
            choicefour = 'Improve chances of spell success'
        elif character == 'Oberon':
            choiceone = 'Attack'
            choicetwo = 'Ignore them'
            choicethree = 'Sneak past them'
            choicefour = 'No special available'
        elif character == 'Terra':
            choiceone = 'Attack'
            choicetwo = 'Unavailable'
            choicethree = 'Sneak past them'
            choicefour = 'No special available'
    elif eventchosen == 9:
        if character == 'Mary':
            choiceone = 'Enter'
            choicetwo = 'Go around the forest'
            choicethree = 'Find another path that leads far away'
            choicefour = 'Cast a spell to avoid the curse of the forest'
        elif character == 'Oberon':
            choiceone = 'Attack'
            choicetwo = 'Ignore them'
            choicethree = 'Sneak past them'
            choicefour = 'No special available'
        elif character == 'Terra':
            choiceone = 'Enter the forest'
            choicetwo = 'Find another path'
            choicethree = 'Go around the forest'
            choicefour = 'Fly past it'
    elif eventchosen == 10:
        if character == 'Mary':
            choiceone = '''Say 'They call it a mine' '''
            choicetwo = 'Look for a dwarf'
            choicethree = 'Look for an elf'
            choicefour = 'Summon a dwarf'
        elif character == 'Oberon':
            choiceone = '''Say 'They call it a mine' '''
            choicetwo = 'Look for a dwarf'
            choicethree = 'Attempt to guide yourself through the mines'
            choicefour = 'Call for a dwarf'
        elif character == 'Terra':
            choiceone = 'Attack the dwarves'
            choicetwo = 'Unavailable'
            choicethree = 'Unavailable'
            choicefour = 'Fly past it'
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
            if eventchosen == 1:
                if gamechoice == 1:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 2:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 3:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        if character == 'Mary':
                            pass
                            tom = False
                        elif character == 'Oberon':
                            pass
                            tom = False
                        elif character == 'Terra':
                            pass
                            tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 4:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                else:
                    pass
            elif eventchosen == 2:
                if gamechoice == 1:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 2:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 3:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 4:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                else:
                    pass
            elif eventchosen == 3:
                if gamechoice == 1:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 2:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 3:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 4:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                else:
                    pass
            elif eventchosen == 4:
                if gamechoice == 1:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 2:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 3:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 4:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                else:
                    pass
            elif eventchosen == 5:
                if gamechoice == 1:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 2:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 3:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 4:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                else:
                    pass
            elif eventchosen == 6:
                if gamechoice == 1:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 2:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 3:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 4:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                else:
                    pass
            elif eventchosen == 7:
                if gamechoice == 1:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 2:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 3:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 4:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                else:
                    pass
            elif eventchosen == 8:
                if gamechoice == 1:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 2:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 3:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 4:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                else:
                    pass
            elif eventchosen == 9:
                if gamechoice == 1:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 2:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 3:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 4:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                else:
                    pass
            elif eventchosen == 10:
                if gamechoice == 1:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 2:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 3:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                elif gamechoice == 4:
                    if character == 'Mary':
                        pass
                        tom = False
                    elif character == 'Oberon':
                        pass
                        tom = False
                    elif character == 'Terra':
                        pass
                        tom = False
                else:
                    pass
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
                json.dump({"character": "", "hp": 0, "mana": 0, "mana_regeneration": 0, "enemy one": 0, "enemy two": 0,
                           "enemy three": 0,
                           "damage one": 0, "damage two": 0, "damage three": 0, "mana one": 0, "mana two": 0,
                           "mana three": 0
                           }, open("information.json", "w"))
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
                    json.dump({"character": "", "hp": 0, "mana": 0, "mana_regeneration": 0, "enemy one": 0,
                               "enemy two": 0, "enemy three": 0,
                               "damage one": 0, "damage two": 0, "damage three": 0, "mana one": 0, "mana two": 0,
                               "mana three": 0},
                              open("information.json", "w"))
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