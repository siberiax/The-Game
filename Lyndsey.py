from rit_object import *
from random import *

class Lyndsey(rit_object):
    __slots__ = ('HP', 'Strength', 'Defense', 'BahamaDuckBucks')
    _types = (    int,    int,   int,     int)

def createLyndsey(Str, Def):
    return Lyndsey(750, Str, Def, 0)

class Joe(rit_object):
    __slots__ = ('HP')
    _types = (int)

def createJoe(HP):
    return Joe(HP)

class Beck(rit_object):
    __slots__ = ('HP')
    _types = (  int)

def createBeck(health):
    return Beck(health)

class Nathan(rit_object):
    __slots__ = ('HP')
    _types = (int)

def createNathan(HP):
    return Nathan(HP)

def simhelp1(Lyndsey, Joe):
    while Joe.HP > 0:
        print('Actions')
        print('(1): Potassium Nitrate Throw')
        print('(2): Squirt the Dirt (trust me it does damage)')
        print('(3): Flee')
        action = input('Choose your action: ')
        print('')
        if not action.isdigit():
            print('You have to enter a number')
            print('')
            simhelp1(Lyndsey, Joe)
        else:
            zeus = randint(1,20)
            if int(action) == 3:
                flee = randint(1,15)
                if flee == 3:
                    print('You successfully fled the fight!')
                    break
                else:
                    print("You were unsuccessful in fleeing")
                    input()
                    damage = randint(30, 50)
                    Lyndsey.HP -= damage - Lyndsey.Defense
                    tdamage = damage - Lyndsey.Defense
                    if Lyndsey.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Lyndsey uses 'sit across from you' and does", tdamage, 'damage. Your HP is now', Lyndsey.HP)
                        input()
                    else:
                        print("Nathan uses 'Jump over to your cabin' which does", tdamage, 'damage. Your HP is now',
                              Lyndsey.HP)
                        input()
            elif zeus == 13:
                Joe.HP = 0
                print("HIDDEN ATTACK! Lyndsey's hotness melts Nathan")
            else:
                if int(action) == 1:
                    ginger = randint(-10, 15)
                    Joe.HP -= ginger + Lyndsey.Strength
                    tginger = ginger + Lyndsey.Strength
                    print("Lyndsey uses 'Potassium Nitrate Throw' which does", tginger, 'damage to Nathan. His HP is now', Joe.HP)
                    input()
                    damage = randint(35, 55)
                    Lyndsey.HP -= damage - Lyndsey.Defense
                    tdamage = damage - Lyndsey.Defense
                    if Lyndsey.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Lyndsey uses 'sit across from you' and does", tdamage, 'damage. Your HP is now', Lyndsey.HP)
                        input()
                    else:
                        print("Nathan uses 'Jump over to your cabin' which does", tdamage, 'damage. Your HP is now',
                              Lyndsey.HP)
                        input()
                else:
                    guitar = randint(-5, 10)
                    Joe.HP -= guitar + Lyndsey.Strength
                    tguitar = guitar + Lyndsey.Strength
                    print("Lyndsey uses 'Squirt the Dirt (trust me it does damage)' which does", tguitar, 'damage to Nathan. His HP is now', Joe.HP)
                    input()
                    damage = randint(40, 55)
                    Lyndsey.HP -= damage - Lyndsey.Defense
                    tdamage = damage - Lyndsey.Defense
                    if Lyndsey.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Nathan uses 'sit across from you' and does", tdamage, 'damage. Your HP is now', Lyndsey.HP)
                        input()
                    else:
                        print("Nathan uses 'Jump over to your cabin' which does", tdamage, 'damage. Your HP is now',
                              Lyndsey.HP)
                        input()
    
def steps1(Lyndsey):
    steps = input('Enter number of steps to take: ')
    print('')
    if not steps.isdigit():
        print('You have to enter a number for steps!')
        print('')
        steps1(Lyndsey)
    else:
        if int(steps) == 0:
            print('Steps must be more that 0!')
            print('')
            steps1(Lyndsey)
        else:
            if int(steps) % 7 == 0:
                stoma = randint(50, 100)
                Lyndsey.BahamaDuckBucks += stoma
                print("Congrats! You didn't get attacked and received", stoma, "BahamaDuckBucks!")
            else:
                print("Oh no! You are attacked by a wild Nathan! (Apparently that's a thing)")
                input()
                health = randint(90, 125)
                Joe = createNathan(health)
                simhelp1(Lyndsey, Joe)

def sim1(Lyndsey):
    print('You enter a dark hallway... Probably at NCA.')
    input()
    steps1(Lyndsey)
    pass
        
def steps2(Lyndsey):
    steps = input('Enter number of steps to take: ')
    print('')
    if not steps.isdigit():
        print('You have to enter a number for steps!')
        print('')
        steps2(Lyndsey)
    else:
        if int(steps) == 0:
            print('Steps must be more that 0!')
            print('')
            steps2(Lyndsey)
        else:
            if int(steps) % 6 == 0:
                stoma = randint(50, 100)
                Lyndsey.BahamaDuckBucks += stoma
                print("Congrats! You didn't get attacked and received", stoma, "BahamaDuckBucks!")
                pass
            else:
                print("Oh no! You are attacked by a wild Nathan! (Apparently that's a thing)")
                input()
                health = randint(90, 125)
                Joe = createNathan(health)
                simhelp1(Lyndsey, Joe)


def sim2(Lyndsey):
    print('You enter a dark hallway... Probably at NCA.')
    input()
    steps2(Lyndsey)
 

def simhelp2(Lyndsey, Joe):
    while Joe.HP > 0:
        print('Actions')
        print('(1): Potassium Nitrate Throw')
        print('(2): Squirt the Dirt (trust me it does damage)')
        print('(3): Flee')
        action = input('Choose your action: ')
        print('')
        zeus = randint(1,20)
        if not action.isdigit():
            print('You must enter a number')
            print('')
            simhelp2(Lyndsey, Joe)
        else:
            if int(action) == 3:
                flee = randint(1, 15)
                if flee == 3:
                    print('You successfully fled the fight!')
                    break
                else:
                    print("You were unsuccessful in fleeing")
                    input()
                    damage = randint(60, 75)
                    Lyndsey.HP -= damage - Lyndsey.Defense
                    tdamage = damage - Lyndsey.Defense
                    if Lyndsey.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Adrian uses 'being himself' and does", tdamage, 'damage. Your HP is now', Lyndsey.HP)
                        input()
                    else:
                        print("Adrian uses 'Adrianess' which does", tdamage, 'damage. Your HP is now',
                              Lyndsey.HP)
                        input()
            elif zeus == 13:
                Joe.HP = 0
                print("HIDDEN ATTACK! Lyndsey's hotness melts Adrian")
            else:
                if int(action) == 1:
                    ginger = randint(-10, 15)
                    Joe.HP -= ginger + Lyndsey.Strength
                    tginger = ginger + Lyndsey.Strength
                    print("Lyndey uses 'Potassium Nitrate Throw' which does", tginger, 'damage to Adrian. His HP is now', Joe.HP)
                    input()
                    damage = randint(50, 70)
                    Lyndsey.HP -= damage - Lyndsey.Defense
                    tdamage = damage - Lyndsey.Defense
                    if Lyndsey.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Adrian uses 'being himself' which does", tdamage, 'damage. Your HP is now', Lyndsey.HP)
                        input()
                    else:
                        print("Adrian uses 'Adrianess' which does", tdamage, 'damage. Your HP is now',
                              Lyndsey.HP)
                        input()
                else:
                    guitar = randint(-5, 10)
                    Joe.HP -= guitar + Lyndsey.Strength
                    tguitar = guitar + Lyndsey.Strength
                    print("Lyndsey uses 'Squirt the Dirt (trust me it does damage)' which does", tguitar, 'damage to Adrian. His HP is now', Joe.HP)
                    input()
                    damage = randint(50, 60)
                    Lyndsey.HP -= damage - Lyndsey.Defense
                    tdamage = damage - Lyndsey.Defense
                    if Lyndsey.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Adrian uses 'being himself' and does", tdamage, 'damage. Your HP is now', Lyndsey.HP)
                        input()
                    else:
                        print("Adrian uses 'Adrianess' which does", tdamage, 'damage. Your HP is now',
                              Lyndsey.HP)
                        input()


def steps3(Lyndsey):
    steps = input('Enter number of steps to take: ')
    print('')
    if not steps.isdigit():
        print('You have to enter a number for steps!')
        print('')
        steps3(Lyndsey)
    else:
        if int(steps) == 0:
            print('Steps must be more that 0!')
            print('')
            steps3(Lyndsey)
        else:
            if int(steps) % 5 == 0:
                stoma = randint(50, 100)
                Lyndsey.BahamaDuckBucks += stoma
                print("Congrats! You didn't get attacked and received", stoma, "BahamaDuckBucks!")
                pass
            else:
                print("Oh no! You are attacked by a Adrian!")
                input()
                health = randint(125, 150)
                Joe = createJoe(health)
                simhelp2(Lyndsey, Joe)


def sim3(Lyndsey):
    print('You enter a dark hallway... Probably at NCA.')
    input()
    steps3(Lyndsey)
    pass
    

def steps4(Lyndsey):
    steps = input('Enter number of steps to take: ')
    print('')
    if not steps.isdigit():
        print('You have to enter a number for steps!')
        print('')
        steps4(Lyndsey)       
    else:
        if int(steps) == 0:
            print('Steps must be more that 0!')
            print('')
            steps4(Lyndsey)
        else:
            if int(steps) % 9 == 0:
                stoma = randint(50, 100)
                Lyndsey.BahamaDuckBucks += stoma
                print("Congrats! You didn't get attacked and received", stoma, "BahamaDuckBucks!")
                pass
            else:
                print("Oh no! You are attacked by a Adrian!")
                input()
                health = randint(125, 150)
                Joe = createJoe(health)
                simhelp2(Lyndsey, Joe)


def sim4(Lyndsey):
    print('You enter a dark hallway... Probably at NCA.')
    input()
    steps4(Lyndsey)

def beckhelp(Lyndsey, beck):
    while beck.HP > 0:
        print('Actions')
        print('(1): Smash Suitcase through their Thick Skulls')
        print("(2): Tell them how _______ annoying they're being (gotta keep the game G rated)")
        print('(3): Flee')
        action = input('Choose your action: ')
        print('')
        zeus = randint(1,20) 
        if not action.isdigit():
            print('You have no enter a number')
            print('')
            beckhelp(Lyndsey, beck)       
        else:
            if int(action) == 3:
                flee = randint(1, 100)
                if flee == 3:
                    print('You successfully fled the fight!')
                    break
                else:
                    print("You were unsuccessful in fleeing")
                    input()
                    damage = randint(60, 80)
                    Lyndsey.HP -= damage - Lyndsey.Defense
                    tdamage = damage - Lyndsey.Defense
                    if Lyndsey.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Girls in the Airport uses 'I have a question' and does", tdamage, 'damage. Your HP is now', Lyndsey.HP)
                        input()
                    else:
                        print("Girls in the Airport uses 'Talk' which does", tdamage, 'damage. Your HP is now',
                              Lyndsey.HP)
                        input()
            elif zeus == 13:
                beck.HP -= 200
                print("HIDDEN ATTACK! Lyndsey's hotness melts the enemy for 200 damage!")
            else:
                if int(action) == 1:
                    ginger = randint(-10, 15)
                    beck.HP -= ginger + Lyndsey.Strength
                    tginger = ginger + Lyndsey.Strength
                    print("Lyndsey smashes her suitcase through their thick skulls and does", tginger, 'damage to them. Her HP is now', beck.HP)
                    input()
                    damage = randint(50, 75)
                    Lyndsey.HP -= damage - Lyndsey.Defense
                    if Lyndsey.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    tdamage = damage - Lyndsey.Defense
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Girls in the Airport uses 'I have a question' and does", tdamage, 'damage. Your HP is now', Lyndsey.HP)
                        input()
                    else:
                        print("Girls in the Airport uses 'Talk' which does", tdamage, 'damage. Your HP is now',
                              Lyndsey.HP)
                        input()
                else:
                    guitar = randint(-5, 10)
                    beck.HP -= guitar + Lyndsey.Strength
                    tguitar = guitar + Lyndsey.Strength
                    print("Lyndsey is explicit which does", tguitar, 'damage to them. Her HP is now', beck.HP)
                    input()
                    damage = randint(50, 75)
                    Lyndsey.HP -= damage - Lyndsey.Defense
                    if Lyndsey.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    tdamage = damage - Lyndsey.Defense
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Girls in the Airport uses 'I have a question' and does", tdamage, 'damage. Your HP is now', Lyndsey.HP)
                        input()
                    else:
                        print("Girls in the Airport uses 'Talk' which does", tdamage, 'damage. Your HP is now',
                              Lyndsey.HP)
                        input()


def beck(Lyndsey):
    print('You enter into a room...')
    print('You are confronted by Girls in the Airport')
    input()
    beck = createBeck(500)
    beckhelp(Lyndsey, beck)


def Joehelp(Lyndsey, Joe):
    while Joe.HP > 0:
        print('Actions')
        print('(1): Use the Syzygy')
        print("(2): Don't Text Back")
        print('(3): Flee')
        action = input('Choose your action: ')
        print('')
        zeus = randint(1,20)
        if not action.isdigit():
            print('You have to enter a number')
            print('')
            Joehelp(Lyndsey, Joe)
        else:
            if int(action) == 3:
                flee = randint(1, 100)
                if flee == 3:
                    print('You successfully fled the fight!')
                    break
                else:
                    print("You were unsuccessful in fleeing")
                    input()
                    damage = randint(85, 100)
                    Lyndsey.HP -= damage - Lyndsey.Defense
                    tdamage = damage - Lyndsey.Defense
                    if Lyndsey.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Joe complains you didn't text back and does", tdamage, 'damage. Your HP is now', Lyndsey.HP)
                        input()
                    else:
                        print("Joe is too Hipster and does", tdamage, 'damage. Your HP is now',
                              Lyndsey.HP)
                        input()
            elif zeus == 13:
                Joe.HP -= 200
                print("HIDDEN ATTACK! Lyndsey's hotness melts the enemy for 200 damage!")
            else:
                if int(action) == 1:
                    ginger = randint(-10, 15)
                    Joe.HP -= ginger + Lyndsey.Strength
                    tginger = ginger + Lyndsey.Strength
                    print("Lyndsey's incredible syzygy", tginger, 'damage to Joe. His HP is now', Joe.HP)
                    input()
                    damage = randint(50, 75)
                    Lyndsey.HP -= damage - Lyndsey.Defense
                    if Lyndsey.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    tdamage = damage - Lyndsey.Defense
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Joe complains you didn't text back and does", tdamage, 'damage. Your HP is now', Lyndsey.HP)
                        input()
                    else:
                        print("Joe is too Hipster and does", tdamage, 'damage. Your HP is now',
                              Lyndsey.HP)
                        input()
                else:
                    guitar = randint(-5, 10)
                    Joe.HP -= guitar + Lyndsey.Strength
                    tguitar = guitar + Lyndsey.Strength
                    print("Lyndsey doesn't text back and does", tguitar, 'damage to Joe. His HP is now', Joe.HP)
                    input()
                    damage = randint(50, 75)
                    Lyndsey.HP -= damage - Lyndsey.Defense
                    if Lyndsey.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    tdamage = damage - Lyndsey.Defense
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Joe complains you didn't text back and does", tdamage, 'damage. Your HP is now', Lyndsey.HP)
                        input()
                    else:
                        print("Joe is too Hipster and does", tdamage, 'damage. Your HP is now',
                              Lyndsey.HP)
                        input()

    
def Reed(Lyndsey):
    print('You enter into a room...')
    print('You are confronted by Joe')
    input()
    Joe = createJoe(750)
    Joehelp(Lyndsey, Joe)


def storehelp3(Lyndsey):
    print('')
    print("(1): Yes I am real man you want to go skateboards?")
    print('(2): Buckwheat!')
    answer2 = input('Enter response: ')
    print('')
    if not answer2.isdigit():
        print('You have to enter a number')
        print('')
        storehelp3(Lyndsey)
    else:
        if int(answer2) == 1:
            print("Not right now...")
            store2(Lyndsey)
        else:
            print("You know it! Here's a list of things you can buy and their prices")
            store3(Lyndsey)

def storehelp2(Lyndsey):
    print('(1): I like trains')
    print('(2): Buckwheat!')
    input('Enter response: ')
    print('')
    print('You are about to go into your a boss battle. This is where you can purchase stuff with your '
          'BahamaDuckBucks')
    storehelp3(Lyndsey)

def storehelp1(Lyndsey):
    print('')
    print("(1): Cailin I think I'm having cronic hic-ups")
    print('(2): Buckwheat!')
    answer = input("Enter response: ")
    print('')
    if not answer.isdigit():
        print('You have to enter a number')
        print('')
        storehelp1(Lyndsey)
    else:
        if int(answer) == 1:
            print("Lyndsey it's not time for that")
        else:
            print("Right back at ya!")
        storehelp2(Lyndsey)


def store(Lyndsey):
    print("You made it!")
    storehelp1(Lyndsey)



def store2(Lyndsey):
    print('')
    print('(1): Full Heal: 200 BahamaDuckBucks')
    print('(2): Pretty Pants Party (strength +10): 250 BahamaDuckBucks')
    print("(3): Hosey Lemonade (defense +10): 250 BahamaDuckBucks")
    print("(4): I don't wanna buy anything")
    while Lyndsey.BahamaDuckBucks > 199:
        print('You have', Lyndsey.BahamaDuckBucks, 'BahamaDuckBucks')
        item = input('Enter what you would like to buy: ')
        print('')
        if not item.isdigit():
            print('You must enter a number')
            print('')
            store2(Lyndsey)
        else:
            if int(item )== 1:
                if Lyndsey.BahamaDuckBucks < 200:
                    print("You don't have enough BahamaDuckBucks!")
                    store2(Lyndsey)
                else:
                    Lyndsey.HP = 750
                    Lyndsey.BahamaDuckBucks -= 200
                    print('Your HP has been restored!')
                    input()
            elif int(item) == 2:
                if Lyndsey.BahamaDuckBucks < 250:
                    print("You don't have enough BahamaDuckBucks!")
                    store2(Lyndsey)
                else:
                    Lyndsey.Strength += 10
                    Lyndsey.BahamaDuckBucks -= 250
                    print('Your Strength increased by 10!')
                    input()
            elif int(item) == 4:
                break
            else:
                if Lyndsey.BahamaDuckBucks < 250:
                    print("You don't have enough BahamaDuckBucks!")
                    store2(Lyndsey)
                else:
                    Lyndsey.Defense += 10
                    Lyndsey.BahamaDuckBucks -= 250
                    print('Your Defense increased by 10!')
                    input()
            print('These are now your stats: HP =', Lyndsey.HP, 'Strength =', Lyndsey.Strength, 'Defense =',
                  Lyndsey.Defense, 'BahamaDuckBucks', Lyndsey.BahamaDuckBucks)
            input()



def store3(Lyndsey):
    print('(1): Full Heal: 200 BahamaDuckBucks')
    print('(2): Pretty Pants Party (strength +5): 250 BahamaDuckBucks')
    print("(3): Hosey Lemonade (defense +5): 250 BahamaDuckBucks")
    print("(4): I don't wanna buy anything")
    while Lyndsey.BahamaDuckBucks > 199:
        print('You have', Lyndsey.BahamaDuckBucks, 'BahamaDuckBucks')
        item = input('Enter what you would like to buy: ')
        print('')
        if not item.isdigit():
            print('You must enter a number')
            print('')
            store2(Lyndsey)
        else:
            if int(item )== 1:
                if Lyndsey.BahamaDuckBucks < 200:
                    print("You don't have enough BahamaDuckBucks!")
                    store2(Lyndsey)
                else:
                    Lyndsey.HP = 750
                    Lyndsey.BahamaDuckBucks -= 200
                    print('Your HP has been restored!')
                    input()
            elif int(item) == 2:
                if Lyndsey.BahamaDuckBucks < 250:
                    print("You don't have enough BahamaDuckBucks!")
                    store2(Lyndsey)
                else:
                    Lyndsey.Strength += 5
                    Lyndsey.BahamaDuckBucks -= 250
                    print('Your Strength increased by 5!')
                    input()
            elif int(item) == 4:
                break
            else:
                if Lyndsey.BahamaDuckBucks < 250:
                    print("You don't have enough BahamaDuckBucks!")
                    store2(Lyndsey)
                else:
                    Lyndsey.Defense += 5
                    Lyndsey.BahamaDuckBucks -= 250
                    print('Your Defense increased by 5!')
                    input()
        print('These are now your stats: HP =', Lyndsey.HP, ', Strength =', Lyndsey.Strength, ', Defense =',
              Lyndsey.Defense, ', BahamaDuckBucks', Lyndsey.BahamaDuckBucks)
        input()

def store4help(Lyndsey):
    print("(1): Yes joe, it's Emerson, shut up Alex, no it's Randy!")
    print('(2): Buckwheat!')
    response = input('Enter response: ')
    print('')
    if not response.isdigit():
        print('You have to enter a number')
        print('')
        store4help(Lyndsey)
    else:
        if int(response) == 1:
            print("Well welcome back to Hipster Stoma Store. Inventory has been restocked.")
            store3(Lyndsey)
        else:
            print("Well welcome back to Hipster Stoma Store. Inventory has been restocked.")
            store2(Lyndsey)

def store4(Lyndsey):
    print("Ahh you're returned")
    store4help(Lyndsey)


def prizestore(Lyndsey):
    print('')
    print('(1): Become a Jedi Now: '+ str(Lyndsey.BahamaDuckBucks))
    print('(2): Salmon with Barbeque Sauce: ' + str(Lyndsey.BahamaDuckBucks))
    prize = input('Choose a prize: ')
    print('')
    if not prize.isdigit():
        print('You have to enter a number')
        print('')
        prizestore(Lyndsey)
    else:
        if int(prize)== 1:
            print('Enjoy Being a Jedi!')
        else:
            print('Really... You chose the fish?')

def store5(Lyndsey):
    print('Lyndsey! You defeated Joe!')
    print('')
    print("(1): You know it Cailin")
    print('(2): Buckwheat!')
    input('Enter Response: ')
    print('')
    print('Well nice job!')
    print('As your reward for defeating the final boss of THE GAME you get to chose one of these awesome prizes!')
    prizestore(Lyndsey)


def main2():
    print("(1): Pretty Pants Party")
    print('(2): Hosey Water')
    thing = input("Choose one: ")
    print('')
    if not thing.isdigit():
        print('you have to enter a number')
        print('')
        main2()
    else:
        if int(thing) == 1:
            print("Pretty Pants Party. Very good choice!")
            Lyndsey = createLyndsey(20, 25)
            input()
            print('Lyndsey has', Lyndsey.HP, 'HP,', Lyndsey.Strength, 'Strength,', Lyndsey.Defense, 'Defense, and',
                  Lyndsey.BahamaDuckBucks, 'BahamaDuckBucks!')
        else:
            print('Hosey Lemonade. Nice choice!')
            Lyndsey = createLyndsey(25, 20)
            input()
            print('Lyndsey has', Lyndsey.HP, 'HP,', Lyndsey.Strength, 'Strength,', Lyndsey.Defense, 'Defense, and',
                  Lyndsey.BahamaDuckBucks, 'BahamaDuckBucks!')
        input()
        print("Just so you know Lyndsey has 2 attacks. 'Potassium Nitrate Throw' and 'Squirt the Dirt' (trust me it does damage)")
        print('Lyndsey gets other attacks in boss battles.')
        input()
        print('Alright I think you are all set now. Have a good time!')
        input()
        sim1(Lyndsey)
        stoma = randint(50, 100)
        Lyndsey.BahamaDuckBucks += stoma
        print('')
        print('Congratulations! You have defeated the wild Nathan. You also received', stoma, 'BahamaDuckBucks!')
        sim2(Lyndsey)
        stoma = randint(50, 100)
        Lyndsey.BahamaDuckBucks += stoma
        print('')
        print('Congratulations! You have defeated the wild Nathan. You also received', stoma, 'BahamaDuckBucks!')
        sim1(Lyndsey)
        stoma = randint(50, 100)
        Lyndsey.BahamaDuckBucks += stoma
        print('')
        print('Congratulations! You have defeated the wild Nathan. You also received', stoma, 'BahamaDuckBucks!')
        sim2(Lyndsey)
        stoma = randint(50, 100)
        Lyndsey.BahamaDuckBucks += stoma
        print('')
        print('Congratulations! You have defeated the wild Nathan. You also received', stoma, 'BahamaDuckBucks!')
        sim2(Lyndsey)
        stoma = randint(50, 100)
        Lyndsey.BahamaDuckBucks += stoma
        print('')
        print('Congratulations! You have defeated the wild Nathan. You also received', stoma, 'BahamaDuckBucks!')
        sim1(Lyndsey)
        stoma = randint(50, 100)
        Lyndsey.BahamaDuckBucks += stoma
        print('')
        print('Congratulations! You have defeated the wild Nathan. You also received', stoma, 'BahamaDuckBucks!')
        store(Lyndsey)
        print("You don't have enough BahamaDuckBucks for anything else.")
        input()
        beck(Lyndsey)
        stoma = randint(350, 500)
        Lyndsey.BahamaDuckBucks += stoma
        print('Congratulations! You have defeated Girls in the Airport! You also received', stoma, 'BahamaDuckBucks!')
        input()
        store4(Lyndsey)
        print("You don't have enough BahamaDuckBucks for anything else.")
        input()
        sim3(Lyndsey)
        stoma = randint(70, 120)
        Lyndsey.BahamaDuckBucks += stoma
        print('')
        print('Congratulations! You have defeated the Adrian. You also received', stoma, 'BahamaDuckBucks!')
        sim3(Lyndsey)
        stoma = randint(70, 120)
        Lyndsey.BahamaDuckBucks += stoma
        print('')
        print('Congratulations! You have defeated the Adrian. You also received', stoma, 'BahamaDuckBucks!')
        sim4(Lyndsey)
        stoma = randint(70, 120)
        Lyndsey.BahamaDuckBucks += stoma
        print('')
        print('Congratulations! You have defeated the Adrian. You also received', stoma, 'BahamaDuckBucks!')
        sim4(Lyndsey)
        stoma = randint(70, 120)
        Lyndsey.BahamaDuckBucks += stoma
        print('')
        print('Congratulations! You have defeated the Adrian. You also received', stoma, 'BahamaDuckBucks!')
        sim4(Lyndsey)
        stoma = randint(70, 120)
        Lyndsey.BahamaDuckBucks += stoma
        print('')
        print('Congratulations! You have defeated the Adrian. You also received', stoma, 'BahamaDuckBucks!')
        sim3(Lyndsey)
        stoma = randint(70, 120)
        Lyndsey.BahamaDuckBucks += stoma
        print('')
        print('Congratulations! You have defeated the Adrian. You also received', stoma, 'BahamaDuckBucks!')
        store(Lyndsey)
        print("You don't have enough BahamaDuckBucks for anything else.")
        input()
        Reed(Lyndsey)
        stoma = randint(1000, 2000)
        Lyndsey.BahamaDuckBucks += stoma
        print('Congratulations! You have defeated Joe! You also received', stoma, 'BahamaDuckBucks!')
        input()
        store5(Lyndsey)
        print('Congratulations! You won THE GAME!')
        print('')

def main():
    print('So you chose Lyndsey huh? Attractive choice!')
    input()
    print("Now before we send you off on your journey you're gonna have to make some choices.")
    input()
    main2()
    print("Would you like to go on a date with Alex sometime?")
    
    i = 3
    while (i >= 0):
        if (i == 0):
            print("That burns more that the salt water did")
            print('')
            break
        answer = input("please say yes: ")
        if (answer == ''):
            print("Well answer something!")
            print('')
            continue
        if (answer == 'yes' or answer == 'Yes'):
            print("GREAT!!!!!!")
            break
        print("That wasn't a yes...")
        print('')
        i -= 1   



if __name__ == '__main__':
    main()






