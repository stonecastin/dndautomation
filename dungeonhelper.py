"""
Dungeon Helper

Runs a full encounter with one goblin using dnd 5e combat

fully customizable!

"""

import random as r

goblin_img = "ascii art placeholder"

def d(die):
    """
rolls a specified die

args: die: max number to roll

returns: integer
"""
    return(r.randint(1,die))

def roll(dice):
    """
"""
    total = 0
    num = int(
        dice[0:dice.find('d')]
        )
    
    if '+' in dice:
        die = int(
            dice[(dice.find('d')+1):dice.find('+')]
            )
        plus = int(
            dice[(dice.find('+')+1):]
            )
    else:
        die = int(
            dice[(dice.find('d')+1):]
            )
        plus = 0
        
    for _ in range(num):
        total += d(die)
    return(total+plus)

def ability_check(dc, prof=0):
    """
runs an ability check with specified DC

args: dc: difficulty to ocheck against
    (optional) prof: profficiency bonus

returns: boolean
"""
    return((d(20)+int(prof))>=int(dc))

def stat_modifier(stat):
    """
returns modifier based on stat

args: stat: the statistic, ex. cha, str, wis

returns: integer
"""
    return(round(stat/2)-5)

def attack(character,weapon,enemy_ac,bonus=0):
    """
determines the amount of damage delt during an attack

args: character: the character attacking, dict
    weapon: the weapon used to attck, must be defined in character sheet, str
    enemy_ac: enemy armor class, int
    bonus: bunus to hit, int
    
returns: damage delt as integer
"""
    if ability_check(enemy_ac,bonus) == True:
        damage = character[str(weapon)]
        return(roll(damage))
    else:
        return(0)
    

def read_character(file_name):
    """
reads a text file of a character sheet and stores it as a dictionary

args: file: .txt file (needs to be in correct format, see write_character)

retutrns: dictionary of character attributes
"""
    ch = {}
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip('\n')
            ch[
                line[0:(line.find(":"))]
                ] = line[line.find(":")+1:]
    return(ch)

def write_character(character):
    """
saves a character sheet that can be read in later

args: character: a dictionary with all character stats

returns: none
"""
    keys = []
    values = []
    file_name = str(character['name']+".txt")
    file = open(file_name,"w")
    
    for key in character.keys():
        keys.append(key)
    for value in character.values():
        values.append(value)
        
    for i in range(len(character)):
        file.write(keys[i]+':'+values[i]+'\n')
            
            
            
            
def create_character():
    """
prompts the user to create a chatacter sheet and writes the character sheet as a .txt file

args: none

returns: ch: dictionary of chatacter stats
"""
    ch = {}
    print("name?")
    name = input()
    ch['name'] = name
    print("hit points?")
    ch['hp'] = input()
    print("armor class?")
    ch['ac'] = input()
    print("stats: \nstregnth?")
    ch['str'] = input()
    print("dexterity?")
    ch['dex'] = input()
    print("constitution?")
    ch['con'] = input()
    print("intelligence?")
    ch['int'] = input()
    print("wisdom?")
    ch['wis'] = input()
    adding_attacks = True
    while adding_attacks == True:
        print("does your character have an attack?")
        if input() == 'yes':
            print("what weapon or spell does " + name + " use?")
            weapon = input()
            print("how much damage does " + weapon + " do? \n(please format damage as ex. 2d4+1)")
            ch[weapon] = input()
            print("does " + name + " have another attack?")
        else:
            adding_attacks = False
    write_character(ch)
    print(name + " is ready!")
    return(ch)

def goblin_attack():
    """
starts a goblin encounter

args: none

returns: none
"""
    goblin_stats = read_character('goblin.txt')
    print("A goblin blocks your path!")
    while int(goblin_stats['hp'])>0 and int(new_character['hp'])>0:
        new_character['hp'] = int(new_character['hp']) - attack(
            goblin_stats, 'scimitar', int(new_character['ac'])
            )
        print(str(new_character['hp']) + " hp remaining, \nwhat attack you you use?")
        damage = attack(new_character, str(input()), int(goblin_stats['ac']))
        goblin_stats['hp'] = int(goblin_stats['hp']) - damage
        print("you did " + str(damage) + " damage!")
        if goblin_stats['hp']>0:
            print("The goblin attacks you!")
    if goblin_stats['hp']<0:
        print("you have defeated the goblin!")
    elif new_character['hp']<0:
        print("the goblin has defeated you!")

new_character = create_character()
goblin_attack()

