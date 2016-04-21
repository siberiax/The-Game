#import Alex
import Nathan
import Lyndsey

def main3():
    print('(1): Lyndsey')
    print('(2): Nathan')
    name = input('Select your character: ')
    print('')
    if not name.isdigit():
        print('You have to enter a number')
        print('')
        main3()
    else:
        if int(name) == 1:
            Lyndsey.main()
        else:
            Nathan.main()

def main2():
    print('(1): Yes')
    print('(2): No')
    response = input('Enter response: ')
    print('')
    if not response.isdigit():
        print('You must enter a number.')
        print('')
        main2()
    else:
        if int(response) == 1:
            print('Good!')
        else:
            print('I think you do get it.')
        print('Okay I think we are ready to start.')
        input()
        main3()


def main():
    print('')
    print("Welcome to THE GAME (hope you didn't lose it)")
    print('This program will pause between each set of text. Just hit ENTER to continue!')
    input()
    print("There you go! I'm your narrator Jimmy, and I will be taking you through THE GAME.")
    input()
    print("Because this is a text based game the course of the game will be based on user input")
    input()
    print('All decisions must be made by inputing a number')
    input()
    print("For example if the game says '(1): Yes/(2): No' that means you would type in 1 to select yes.")
    input()
    print('Got it?')
    main2()

main()
