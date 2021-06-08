import random
from Text_adventure import hp, mana, mana_regeneration, character

maxmana = mana
maxhp = hp

def battle():
    global hp, maxhp, enemy_hp, enemy_maxhp, dmg, character, mana, mana_regeneration, maxmana
    enemy_hp = random.randrange(2, 20)*10
    enemy_maxhp = enemy_hp
    while True:
        print("-" * 150)
        mana = mana + mana_regeneration
        if mana >= maxmana:
            mana = maxmana
        if hp >= maxhp:
            hp = maxhp

        if enemy_hp <= 0:
            print("You lost the battle!")
            break
        elif hp <= 0:
            print("You won the battle!")
            break
        else:
            print("Enemy's health: " + str(enemy_hp) + "HP")
            print("▓" * enemy_hp + ("░" * (enemy_maxhp - enemy_hp)))
            print("Your health: " + str(hp) + "HP Your Mana: " + str(mana))
            print("▓" * hp + ("░" * (maxhp - hp)))
            choice = input("[Attack (1-3dmg) Cost:0 mana] [Mana]")
            if choice.lower() == "attack":
                dmg = random.randrange(1, 4)
                print("You used a regular attack...")
            elif choice.lower() == "mana":
                if character == "Mary":
                    choice = input("[Kill Spell (20% Instant kill) Cost:175 mana] [Damage Spell (80% 20dmg) Cost:25 mana] [Wand poke (4-6dmg) Cost:0 mana] [Angelic voice (+30HP) Cost:20 mana]")
                    if choice.lower() == "kill spell":
                        if mana >= 175:
                            x = random.randrange(0, 101)
                            mana = mana - 175
                            if x <= 20:
                                dmg = 9999
                                print("The spell worked!")
                            else:
                                print("Uh oh... the spell didn't work!")
                                dmg = 0
                        else:
                            print("Insufficient mana!")
                            continue
                    elif choice.lower() == "damage spell":
                        if mana >= 25:
                            x = random.randrange(0, 101)
                            mana = mana - 25
                            if x <= 80:
                                dmg = 20
                                print("The spell worked!")
                            else:
                                dmg = 0
                                print("Uh oh... the spell didn't work!")
                        else:
                            print("Insufficient mana!")
                            continue
                    elif choice.lower() == "wand poke":
                        print("You poked the enemy!")
                        dmg = random.randrange(4, 7)
                    elif choice.lower() == "angelic voice":
                        if mana >= 20:
                            mana = mana - 20
                            hp = hp + 30
                            dmg = 0
                            print("You healed 30HP up!")
                        else:
                            print("Insufficient mana!")
                    else:
                        continue
                elif character == "Oberon":
                    choice = input("[Elven bow (10dmg) Cost:5 mana] [Earth spell (22-55dmg) Cost:50 mana] [Mother nature (+20HP 40-45dmg) Cost:100 mana]")
                    if choice.lower() == "elven bow":
                        if mana >= 5:
                            print("You shot the enemy!")
                            dmg = 10
                            mana = mana - 5
                    elif choice.lower() == "earth spell":
                        if mana >= 50:
                            print("The spell created an earth quake!")
                            dmg = random.randrange(22, 56)
                            mana = mana - 50
                        else:
                            print("Insufficient mana!")
                            continue
                    elif choice.lower() == "mother nature":
                        if mana >= 100:
                            print("May mother nature be with you!")
                            print("You healed 20HP!")
                            dmg = random.randrange(40, 46)
                            mana - mana - 100
                        else:
                            print("Insufficient mana!")
                            continue
                    else:
                        continue
                elif character == "Terra":
                    choice = input("[Breathe Fire (0-30dmg) Cost:15 mana] [Stomp attack (15dmg) Cost:0 mana] [Sacrifice (-50HP 50dmg) Cost:50 mana]")
                    if choice.lower() == "breathe fire":
                        if mana >= 15:
                            print("You tried to burn your enemy!")
                            dmg = random.randrange(0, 31)
                            mana = mana - 15
                        else:
                            print("Insufficient mana!")
                    elif choice.lower() == "stomp attack":
                        print("You stomped on the enemy!")
                        dmg = 15
                    elif choice.lower() == "sacrifice":
                        if mana >= 50:
                            print("You sacrificed your own HP for damage!")
                            hp = hp -50
                            dmg = 50
                            mana = mana - 50
                        else:
                            print("Insufficient mana!")
                            continue
                    else:
                        continue
            else:
                continue

            print("-" * 150)

            print("You dealet " + str(dmg) + " damage!")
            enemy_hp = enemy_hp - dmg
            dmg = random.randrange(5, 21)
            hp = hp - dmg
            print("The enemy dealet " + str(dmg) + " damage!")