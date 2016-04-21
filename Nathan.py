from rit_object import *
from random import *

class Nathan(rit_object):
    __slots__ = ('HP', 'Strength', 'Defense', 'Stomabucks')
    _types = (    int,    int,   int,     int)

def createNathan(Str, Def):
    return Nathan(750, Str, Def, 0)

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

class Connor(rit_object):
    __slots__ = ('HP')
    _types = (int)

def createConnor(HP):
    return Connor(HP)

def simhelp1(Nathan, Joe):
    while Joe.HP > 0:
        print('Actions')
        print('(1): Ginger Hair Whip')
        print('(2): Sonic Guitar Chord')
        print('(3): Flee')
        action = input('Choose your action: ')
        print('')
        if not action.isdigit():
            print('You have to enter a number')
            print('')
            simhelp1(Nathan, Joe)
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
                    Nathan.HP -= damage - Nathan.Defense
                    tdamage = damage - Nathan.Defense
                    if Nathan.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Joe uses 'being himself' and does", tdamage, 'damage. Your HP is now', Nathan.HP)
                        input()
                    else:
                        print("Joe uses his 'strange music taste' which does", tdamage, 'damage. Your HP is now',
                              Nathan.HP)
                        input()
            elif zeus == 13:
                Joe.HP = 0
                print("HIDDEN ATTACK! Zeus's lightning took out all of Joe's HP!")
            else:
                if int(action) == 1:
                    ginger = randint(-10, 15)
                    Joe.HP -= ginger + Nathan.Strength
                    tginger = ginger + Nathan.Strength
                    print("Nathan uses 'Ginger Hair Whip' which does", tginger, 'damage to Joe. His HP is now', Joe.HP)
                    input()
                    damage = randint(35, 55)
                    Nathan.HP -= damage - Nathan.Defense
                    tdamage = damage - Nathan.Defense
                    if Nathan.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Joe uses 'being himself' and does", tdamage, 'damage. Your HP is now', Nathan.HP)
                        input()
                    else:
                        print("Joe uses his 'strange music taste' which does", tdamage, 'damage. Your HP is now',
                              Nathan.HP)
                        input()
                else:
                    guitar = randint(-5, 10)
                    Joe.HP -= guitar + Nathan.Strength
                    tguitar = guitar + Nathan.Strength
                    print("Nathan uses 'Sonic Guitar Chord' which does", tguitar, 'damage to Joe. His HP is now', Joe.HP)
                    input()
                    damage = randint(40, 55)
                    Nathan.HP -= damage - Nathan.Defense
                    tdamage = damage - Nathan.Defense
                    if Nathan.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Joe uses 'being himself' and does", tdamage, 'damage. Your HP is now', Nathan.HP)
                        input()
                    else:
                        print("Joe uses his 'strange music taste' which does", tdamage, 'damage. Your HP is now',
                              Nathan.HP)
                        input()
    
def steps1(Nathan):
    steps = input('Enter number of steps to take: ')
    print('')
    if not steps.isdigit():
        print('You have to enter a number for steps!')
        print('')
        steps1(Nathan)
    else:
        if int(steps) == 0:
            print('Steps must be more that 0!')
            print('')
            steps1(Nathan)
        else:
            if int(steps) % 7 == 0:
                stoma = randint(50, 100)
                Nathan.Stomabucks += stoma
                print("Congrats! You didn't get attacked and received", stoma, "Stomabucks!")
            else:
                print("Oh no! You are attacked by a wild Joe! (Apparently that's a thing)")
                input()
                health = randint(90, 125)
                Joe = createJoe(health)
                simhelp1(Nathan, Joe)

def sim1(Nathan):
    print('You enter a dark hallway... Probably at NCA.')
    input()
    steps1(Nathan)
    pass
        
def steps2(Nathan):
    steps = input('Enter number of steps to take: ')
    print('')
    if not steps.isdigit():
        print('You have to enter a number for steps!')
        print('')
        steps2(Nathan)
    else:
        if int(steps) == 0:
            print('Steps must be more that 0!')
            print('')
            steps2(Nathan)
        else:
            if int(steps) % 6 == 0:
                stoma = randint(50, 100)
                Nathan.Stomabucks += stoma
                print("Congrats! You didn't get attacked and received", stoma, "Stomabucks!")
                pass
            else:
                print("Oh no! You are attacked by a wild Joe! (Apparently that's a thing)")
                input()
                health = randint(90, 125)
                Joe = createJoe(health)
                simhelp1(Nathan, Joe)


def sim2(Nathan):
    print('You enter a dark hallway... Probably at NCA.')
    input()
    steps2(Nathan)
 

def simhelp2(Nathan, Joe):
    while Joe.HP > 0:
        print('Actions')
        print('(1): Ginger Hair Whip')
        print('(2): Sonic Guitar Chord')
        print('(3): Flee')
        action = input('Choose your action: ')
        print('')
        zeus = randint(1,20)
        if not action.isdigit():
            print('You must enter a number')
            print('')
            simhelp2(Nathan, Joe)
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
                    Nathan.HP -= damage - Nathan.Defense
                    tdamage = damage - Nathan.Defense
                    if Nathan.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Joemageddon says 'I got it with Stuff' and does", tdamage, 'damage. Your HP is now', Nathan.HP)
                        input()
                    else:
                        print("Joemageddon uses its 'Joeness' which does", tdamage, 'damage. Your HP is now',
                              Nathan.HP)
                        input()
            elif zeus == 13:
                Joe.HP = 0
                print("HIDDEN ATTACK! Zeus's lightning took out all of Joe's HP!")
            else:
                if int(action) == 1:
                    ginger = randint(-10, 15)
                    Joe.HP -= ginger + Nathan.Strength
                    tginger = ginger + Nathan.Strength
                    print("Nathan uses 'Ginger Hair Whip' which does", tginger, 'damage to Joe. His HP is now', Joe.HP)
                    input()
                    damage = randint(50, 70)
                    Nathan.HP -= damage - Nathan.Defense
                    tdamage = damage - Nathan.Defense
                    if Nathan.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Joemageddon says 'I got it with Stuff' which does", tdamage, 'damage. Your HP is now', Nathan.HP)
                        input()
                    else:
                        print("Joemageddon uses its 'Joeness' which does", tdamage, 'damage. Your HP is now',
                              Nathan.HP)
                        input()
                else:
                    guitar = randint(-5, 10)
                    Joe.HP -= guitar + Nathan.Strength
                    tguitar = guitar + Nathan.Strength
                    print("Nathan uses 'Sonic Guitar Chord' which does", tguitar, 'damage to Joe. His HP is now', Joe.HP)
                    input()
                    damage = randint(50, 60)
                    Nathan.HP -= damage - Nathan.Defense
                    tdamage = damage - Nathan.Defense
                    if Nathan.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Joemageddon says 'I got it with stuff' and does", tdamage, 'damage. Your HP is now', Nathan.HP)
                        input()
                    else:
                        print("Joemageddon uses its 'Joeness' which does", tdamage, 'damage. Your HP is now',
                              Nathan.HP)
                        input()


def steps3(Nathan):
    steps = input('Enter number of steps to take: ')
    print('')
    if not steps.isdigit():
        print('You have to enter a number for steps!')
        print('')
        steps3(Nathan)
    else:
        if int(steps) == 0:
            print('Steps must be more that 0!')
            print('')
            steps3(Nathan)
        else:
            if int(steps) % 5 == 0:
                stoma = randint(50, 100)
                Nathan.Stomabucks += stoma
                print("Congrats! You didn't get attacked and received", stoma, "Stomabucks!")
                pass
            else:
                print("Oh no! You are attacked by a Joemageddon!")
                input()
                health = randint(125, 150)
                Joe = createJoe(health)
                simhelp2(Nathan, Joe)


def sim3(Nathan):
    print('You enter a dark hallway... Probably at NCA.')
    input()
    steps3(Nathan)
    pass
    

def steps4(Nathan):
    steps = input('Enter number of steps to take: ')
    print('')
    if not steps.isdigit():
        print('You have to enter a number for steps!')
        print('')
        steps4(Nathan)       
    else:
        if int(steps) == 0:
            print('Steps must be more that 0!')
            print('')
            steps4(Nathan)
        else:
            if int(steps) % 9 == 0:
                stoma = randint(50, 100)
                Nathan.Stomabucks += stoma
                print("Congrats! You didn't get attacked and received", stoma, "Stomabucks!")
                pass
            else:
                print("Oh no! You are attacked by a Joemageddon!")
                input()
                health = randint(125, 150)
                Joe = createJoe(health)
                simhelp2(Nathan, Joe)


def sim4(Nathan):
    print('You enter a dark hallway... Probably at NCA.')
    input()
    steps4(Nathan)

def beckhelp(Nathan, beck):
    while beck.HP > 0:
        print('Actions')
        print('(1): Get a Sticker')
        print('(2): Write Awesome Paper')
        print('(3): Flee')
        action = input('Choose your action: ')
        print('')
        zeus = randint(1,20) 
        if not action.isdigit():
            print('You have no enter a number')
            print('')
            beckhelp(Nathan, beck)       
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
                    Nathan.HP -= damage - Nathan.Defense
                    tdamage = damage - Nathan.Defense
                    if Nathan.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Mrs. Beck uses 'Watching YouTube' and does", tdamage, 'damage. Your HP is now', Nathan.HP)
                        input()
                    else:
                        print("Mrs. Beck uses 'Draw AP students' which does", tdamage, 'damage. Your HP is now',
                              Nathan.HP)
                        input()
            elif zeus == 13:
                beck.HP -= 200
                print("HIDDEN ATTACK! Zeus's lightning did 200 damage!")
            else:
                if int(action) == 1:
                    ginger = randint(-10, 15)
                    beck.HP -= ginger + Nathan.Strength
                    tginger = ginger + Nathan.Strength
                    print("Nathan gets a sticker which does", tginger, 'damage to Mrs. Beck. Her HP is now', beck.HP)
                    input()
                    damage = randint(50, 75)
                    Nathan.HP -= damage - Nathan.Defense
                    if Nathan.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    tdamage = damage - Nathan.Defense
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Mrs. Beck uses 'Watching YouTube' and does", tdamage, 'damage. Your HP is now', Nathan.HP)
                        input()
                    else:
                        print("Mrs. Beck uses 'Draw AP students' which does", tdamage, 'damage. Your HP is now',
                              Nathan.HP)
                        input()
                else:
                    guitar = randint(-5, 10)
                    beck.HP -= guitar + Nathan.Strength
                    tguitar = guitar + Nathan.Strength
                    print("Nathan writes a paper and does", tguitar, 'damage to Mrs. Beck. Her HP is now', beck.HP)
                    input()
                    damage = randint(50, 75)
                    Nathan.HP -= damage - Nathan.Defense
                    if Nathan.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    tdamage = damage - Nathan.Defense
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Mrs. Beck uses 'Watching YouTube' and does", tdamage, 'damage. Your HP is now', Nathan.HP)
                        input()
                    else:
                        print("Mrs. Beck uses 'Draw AP students' which does", tdamage, 'damage. Your HP is now',
                              Nathan.HP)
                        input()


def beck(Nathan):
    print('You enter into a room...')
    print('You are confronted by Mrs. Beck')
    input()
    beck = createBeck(500)
    beckhelp(Nathan, beck)


def connorhelp(Nathan, connor):
    while connor.HP > 0:
        print('Actions')
        print('(1): General Argument')
        print('(2): Be THE COMMUNIST')
        print('(3): Flee')
        action = input('Choose your action: ')
        print('')
        zeus = randint(1,20)
        if not action.isdigit():
            print('You have to enter a number')
            print('')
            connorhelp(Nathan, connor)
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
                    Nathan.HP -= damage - Nathan.Defense
                    tdamage = damage - Nathan.Defense
                    if Nathan.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Connor talks about gun control and does", tdamage, 'damage. Your HP is now', Nathan.HP)
                        input()
                    else:
                        print("Connor is THE REPUBLICAN and does", tdamage, 'damage. Your HP is now',
                              Nathan.HP)
                        input()
            elif zeus == 13:
                connor.HP -= 200
                print("HIDDEN ATTACK! Zeus's lightning did 200 damage!")
            else:
                if int(action) == 1:
                    ginger = randint(-10, 15)
                    connor.HP -= ginger + Nathan.Strength
                    tginger = ginger + Nathan.Strength
                    print("Nathan's argument", tginger, 'damage to Connor. His HP is now', connor.HP)
                    input()
                    damage = randint(50, 75)
                    Nathan.HP -= damage - Nathan.Defense
                    if Nathan.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    tdamage = damage - Nathan.Defense
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Connor talks about gun control and does", tdamage, 'damage. Your HP is now', Nathan.HP)
                        input()
                    else:
                        print("Connor is THE REPUBLICAN and does", tdamage, 'damage. Your HP is now',
                              Nathan.HP)
                        input()
                else:
                    guitar = randint(-5, 10)
                    connor.HP -= guitar + Nathan.Strength
                    tguitar = guitar + Nathan.Strength
                    print("Nathan is THE COMMUNIST", tguitar, 'damage to Connor. His HP is now', connor.HP)
                    input()
                    damage = randint(50, 75)
                    Nathan.HP -= damage - Nathan.Defense
                    if Nathan.HP < 0:
                        print("Oh no you've reached 0 HP... Looks like you've been defeated")
                        exit()
                    tdamage = damage - Nathan.Defense
                    scenario = randint(1,2)
                    if scenario == 1:
                        print("Connor talks about gun control and does", tdamage, 'damage. Your HP is now', Nathan.HP)
                        input()
                    else:
                        print("Connor is THE REPUBLICAN and does", tdamage, 'damage. Your HP is now',
                              Nathan.HP)
                        input()

    
def connor(Nathan):
    print('You enter into a room...')
    print('You are confronted by Connor')
    input()
    connor = createConnor(750)
    connorhelp(Nathan, connor)


def storehelp3(Nathan):
    print('')
    print("(1): I can purchase Stuff! Heck yeah!")
    print('(2): Murica')
    answer2 = input('Enter response: ')
    print('')
    if not answer2.isdigit():
        print('You have to enter a number')
        print('')
        storehelp3(Nathan)
    else:
        if int(answer2) == 1:
            print("Not that stuff... Here's a list of things you can buy and their prices")
            store2(Nathan)
        else:
            print("You know it! Here's a list of things you can buy and their prices")
            store3(Nathan)

def storehelp2(Nathan):
    print('(1): Heck yeah!')
    print('(2): Murica')
    input('Enter response: ')
    print('')
    print('You are about to go into your a boss battle. This is where you can purchase stuff with your '
          'Stomabucks')
    storehelp3(Nathan)

def storehelp1(Nathan):
    print('')
    print("(1): Yeah Jimmy. What's it to ya?")
    print('(2): Murica')
    answer = input("Enter response: ")
    print('')
    if not answer.isdigit():
        print('You have to enter a number')
        print('')
        storehelp1(Nathan)
    else:
        if int(answer) == 1:
            print('I was just saying... Welcome to the Hipster Stoma Store!')
        else:
            print("Nice! You're in the Hipster Stoma Store!")
        storehelp2(Nathan)


def store(Nathan):
    print("You made it!")
    storehelp1(Nathan)



def store2(Nathan):
    print('')
    print('(1): Full Heal: 200 Stomabucks')
    print('(2): Pringles with Reeses (strength +10): 250 Stomabucks')
    print("(3): Krony's pizza (defense +10): 250 Stomabucks")
    print("(4): I don't wanna buy anything")
    while Nathan.Stomabucks > 199:
        print('You have', Nathan.Stomabucks, 'Stomabucks')
        item = input('Enter what you would like to buy: ')
        print('')
        if not item.isdigit():
            print('You must enter a number')
            print('')
            store2(Nathan)
        else:
            if int(item )== 1:
                if Nathan.Stomabucks < 200:
                    print("You don't have enough Stomabucks!")
                    store2(Nathan)
                else:
                    Nathan.HP = 750
                    Nathan.Stomabucks -= 200
                    print('Your HP has been restored!')
                    input()
            elif int(item) == 2:
                if Nathan.Stomabucks < 250:
                    print("You don't have enough Stomabucks!")
                    store2(Nathan)
                else:
                    Nathan.Strength += 10
                    Nathan.Stomabucks -= 250
                    print('Your Strength increased by 10!')
                    input()
            elif int(item) == 4:
                break
            else:
                if Nathan.Stomabucks < 250:
                    print("You don't have enough Stomabucks!")
                    store2(Nathan)
                else:
                    Nathan.Defense += 10
                    Nathan.Stomabucks -= 250
                    print('Your Defense increased by 10!')
                    input()
            print('These are now your stats: HP =', Nathan.HP, 'Strength =', Nathan.Strength, 'Defense =',
                  Nathan.Defense, 'Stomabucks', Nathan.Stomabucks)
            input()



def store3(Nathan):
    print('(1): Full Heal: 200 Stomabucks')
    print('(2): Pringles with Reeses (strength +5): 250 Stomabucks')
    print("(3): Krony's pizza (defense +5): 250 Stomabucks")
    print("(4): I don't wanna buy anything")
    while Nathan.Stomabucks > 199:
        print('You have', Nathan.Stomabucks, 'Stomabucks')
        item = input('Enter what you would like to buy: ')
        print('')
        if not item.isdigit():
            print('You must enter a number')
            print('')
            store2(Nathan)
        else:
            if int(item )== 1:
                if Nathan.Stomabucks < 200:
                    print("You don't have enough Stomabucks!")
                    store2(Nathan)
                else:
                    Nathan.HP = 750
                    Nathan.Stomabucks -= 200
                    print('Your HP has been restored!')
                    input()
            elif int(item) == 2:
                if Nathan.Stomabucks < 250:
                    print("You don't have enough Stomabucks!")
                    store2(Nathan)
                else:
                    Nathan.Strength += 5
                    Nathan.Stomabucks -= 250
                    print('Your Strength increased by 5!')
                    input()
            elif int(item) == 4:
                break
            else:
                if Nathan.Stomabucks < 250:
                    print("You don't have enough Stomabucks!")
                    store2(Nathan)
                else:
                    Nathan.Defense += 5
                    Nathan.Stomabucks -= 250
                    print('Your Defense increased by 5!')
                    input()
        print('These are now your stats: HP =', Nathan.HP, ', Strength =', Nathan.Strength, ', Defense =',
              Nathan.Defense, ', Stomabucks', Nathan.Stomabucks)
        input()

def store4help(Nathan):
    print('(1): Yeah Jimmy... That was a piece of cake')
    print('(2): Murica')
    response = input('Enter response: ')
    print('')
    if not response.isdigit():
        print('You have to enter a number')
        print('')
        store4help(Nathan)
    else:
        if int(response) == 1:
            print("Well welcome back to Hipster Stoma Store. Inventory has been restocked.")
            store3(Nathan)
        else:
            print("Well welcome back to Hipster Stoma Store. Inventory has been restocked.")
            store2(Nathan)

def store4(Nathan):
    print("Ahh you're returned")
    store4help(Nathan)


def prizestore(Nathan):
    print('')
    print('(1): Snotchy Petch: '+ str(Nathan.Stomabucks))
    print('(2): All the mustard: ' + str(Nathan.Stomabucks))
    prize = input('Choose a prize: ')
    print('')
    if not prize.isdigit():
        print('You have to enter a number')
        print('')
        prizestore(Nathan)
    else:
        if int(prize)== 1:
            print('Enjoy your Snotchy Petch!')
        else:
            print('Enjoy all that mustard!')

def store5(Nathan):
    print('Nathan! You defeated Connor!')
    print('')
    print("(1): All in a day's work Jimmy")
    print('(2): Murica')
    input('Enter Response: ')
    print('')
    print('Well nice job!')
    print('As your reward for defeating the final boss of THE GAME you get to chose one of these awesome prizes!')
    prizestore(Nathan)


def main2():
    print("(1): Lugia's large")
    print('(2): Five Guys with extra bacon')
    thing = input("Choose one: ")
    print('')
    if not thing.isdigit():
        print('you have to enter a number')
        print('')
        main2()
    else:
        if int(thing) == 1:
            print("Lugia's large. Very good choice!")
            Nathan = createNathan(20, 25)
            input()
            print('Nathan has', Nathan.HP, 'HP,', Nathan.Strength, 'Strength,', Nathan.Defense, 'Defense, and',
                  Nathan.Stomabucks, 'Stomabucks!')
        else:
            print('Five Guys with extra bacon. Nice choice!')
            Nathan = createNathan(25, 20)
            input()
            print('Nathan has', Nathan.HP, 'HP,', Nathan.Strength, 'Strength,', Nathan.Defense, 'Defense, and',
                  Nathan.Stomabucks, 'Stomabucks!')
        input()
        print("Just so you know Nathan has 2 attacks. 'ginger hair whip' and 'sonic guitar chord'")
        print('Nathan gets other attacks in boss battles.')
        input()
        print('Alright I think you are all set now. Have a good time!')
        input()
        sim1(Nathan)
        stoma = randint(50, 100)
        Nathan.Stomabucks += stoma
        print('')
        print('Congratulations! You have defeated the Wild Joe. You also received', stoma, 'Stomabucks!')
        sim2(Nathan)
        stoma = randint(50, 100)
        Nathan.Stomabucks += stoma
        print('')
        print('Congratulations! You have defeated the Wild Joe. You also received', stoma, 'Stomabucks!')
        sim1(Nathan)
        stoma = randint(50, 100)
        Nathan.Stomabucks += stoma
        print('')
        print('Congratulations! You have defeated the Wild Joe. You also received', stoma, 'Stomabucks!')
        sim2(Nathan)
        stoma = randint(50, 100)
        Nathan.Stomabucks += stoma
        print('')
        print('Congratulations! You have defeated the Wild Joe. You also received', stoma, 'Stomabucks!')
        sim2(Nathan)
        stoma = randint(50, 100)
        Nathan.Stomabucks += stoma
        print('')
        print('Congratulations! You have defeated the Wild Joe. You also received', stoma, 'Stomabucks!')
        sim1(Nathan)
        stoma = randint(50, 100)
        Nathan.Stomabucks += stoma
        print('')
        print('Congratulations! You have defeated the Wild Joe. You also received', stoma, 'Stomabucks!')
        store(Nathan)
        print("You don't have enough Stomabucks for anything else.")
        input()
        beck(Nathan)
        stoma = randint(350, 500)
        Nathan.Stomabucks += stoma
        print('Congratulations! You have defeated Mrs. Beck! You also received', stoma, 'Stomabucks!')
        input()
        store4(Nathan)
        print("You don't have enough Stomabucks for anything else.")
        input()
        sim3(Nathan)
        stoma = randint(70, 120)
        Nathan.Stomabucks += stoma
        print('')
        print('Congratulations! You have defeated the Joemageddon. You also received', stoma, 'Stomabucks!')
        sim3(Nathan)
        stoma = randint(70, 120)
        Nathan.Stomabucks += stoma
        print('')
        print('Congratulations! You have defeated the Joemageddon. You also received', stoma, 'Stomabucks!')
        sim4(Nathan)
        stoma = randint(70, 120)
        Nathan.Stomabucks += stoma
        print('')
        print('Congratulations! You have defeated the Joemageddon. You also received', stoma, 'Stomabucks!')
        sim4(Nathan)
        stoma = randint(70, 120)
        Nathan.Stomabucks += stoma
        print('')
        print('Congratulations! You have defeated the Joemageddon. You also received', stoma, 'Stomabucks!')
        sim4(Nathan)
        stoma = randint(70, 120)
        Nathan.Stomabucks += stoma
        print('')
        print('Congratulations! You have defeated the Joemageddon. You also received', stoma, 'Stomabucks!')
        sim3(Nathan)
        stoma = randint(70, 120)
        Nathan.Stomabucks += stoma
        print('')
        print('Congratulations! You have defeated the Joemageddon. You also received', stoma, 'Stomabucks!')
        store(Nathan)
        print("You don't have enough Stomabucks for anything else.")
        input()
        connor(Nathan)
        stoma = randint(1000, 2000)
        Nathan.Stomabucks += stoma
        print('Congratulations! You have defeated Connor! You also received', stoma, 'Stomabucks!')
        input()
        store5(Nathan)
        print('Congratulations! You won THE GAME!')
        print('')

def main():
    print('So you chose Nathan huh? Cool choice!')
    input()
    print("Now before we send you off on your journey you're gonna have to make some choices.")
    input()
    main2()



if __name__ == '__main__':
    main()
