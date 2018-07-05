import random

words3 = ['ram', 'fag', 'pot', 'old', 'mad', 'wed']
words4 = ['cord' 'word', 'node', 'help', 'four']
words5 = ['power', 'grown', 'money', 'mouse']
words6 = ['laptop', 'travel', 'answer']
words7 = ['desktop', 'product', 'strange']
i = 0
k = 0
bulls = 0
cows = 0
word_len = 4
turn = 0
max_turn = 5

def start_menu():
    global difficulty
    global word_len
    global max_turn
    global word

    difficulty = input('''Select difficulty :
    0 - easy (default)
        3 letter words
        6 guesses

    1 - normal
        4 letter words
        5 guessess

    2 - intermediate
        5 letter words
        5 guesses

    3 - hard
        6 letter words
        7 guesses

    4 - advanced
        7 letter words
        5 guesses
>''')

    if (difficulty == 0):
        max_turn = 6
        word_len = 3
        word = random.choice(words3)
    elif (difficulty == 1):
        max_turn = 5
        word_len = 4
        word = words4
    elif (difficulty == 2):
        max_turn = 5
        word_len = 5
        word = random.choice(words5)
    elif (difficulty == 3):
        max_turn = 5
        word_len = 6
        word = random.choice(words6)
    elif (difficulty == 4):
        max_turn = 5
        word_len = 7
        word = random.choice(words7)
    else:
        print ("\nInvalid selection. Choose a number between 0 and 4\n")
        start_menu()
    get_input()

def menu_input():
    global usr_input

    usr_input = raw_input("To return to the main menu press 'q'\n> ")
    if (usr_input == 'q'):
        print_start()
    else:
        print_instructions()
        menu_input()


def print_start():
    global instructions

    print('''
 ____                                 ___                                      .
|    |    |       |   |       |      /   \                                     .
|    /    |       |   |       |     |     |                                    .
|---      |       |   |       |      \ __                                      .
|    \    |       |   |       |           \                                    .
|    |    |       |   |       |     |      |                                   .
|____|     \ ___ /    |____   |____  \____/                                    .
      ___                                                                      .
    /     \                                                                    .
    \     /                                                                    .
     \   /                                                                     .
      \ /                                                                      .
      / \                                                                      .
     /   \                                                                     .
    /     \  /                                                                 .
    \_____/\/                                                                  .
  _____     _____                            ___                               .
 /        /       \   |        |        |   /   \                              .
|        |         |  |        |        |  |     |                             .
|        |         |   \      / \      /    \ __                               .
|        |         |    \    /   \    /          \                             .
|        |         |     \  /     \  /     |      |                            .
 \_____   \ _____ /       \/       \/       \____/                             .
 ''')
    instructions = raw_input('''To learn how to play type 'help'
If you already know how to play type 'start'\n> ''')
    if (instructions == 'help'):
        print_instructions()
        menu_input()
    elif (instructions == 'start'):
        start_menu()

def lose_msg():
    print ('''
   _____      ____                            ______                           .
 /           /    \        /\       /\       |                                 .
|           |      |      /  \     /  \      |                                 .
|    ____   |______|     /    \   /    \     |____                             .
|       |   |      |    /      \ /      \    |                                 .
|       |   |      |   |        |        |   |                                 .
 \______/   |      |   |        |        |   |______                           .
                                                                               .
   _____                       ______     ______                               .
 /       \    \          /    |          |      |                              .
|         |    \        /     |          |      |                              .
|         |     \      /      |____      |____ /                               .
|         |      \    /       |          |     \                               .
|         |       \  /        |          |      |                              .
 \_______/         \/         |______    |      |                              .
''')

def win_msg():
    print ('''
             _____
\     /    /       \    |         |
 \   /    |         |   |         |
  \ /     |         |   |         |
   |      |         |   |         |
   |      |         |    \       /
   |       \_______/      \_____/

                       _________
|        |        |        |        |\     |
|        |        |        |        | \    |
 \      / \      /         |        |  \   |
  \    /   \    /          |        |   \  |
   \  /     \  /           |        |    \ |
    \/       \/        _________    |     \|
''')

def print_instructions():
    print ("Welcome to the game of Bulls and Cows\n")
    print ("An isogram (a word without any repeating letters) will be chosen at random\n".format(word_len))
    print ("Your goal is to guess the word in as few tries as possible\n")
    print ("After making a guess you will be shown the number of 'bulls' and 'cows' you have")
    print ("You will also be shown the number of turns taken and remaining\n")
    print ("A 'bull' means that one of the letters is correct and in the correct location")
    print ("A 'cow' means that one of the letters is correct but it is not in the correct location")
    print ("\nex: if the word is\n  'word'\nif you were to guess\n  'node'")
    print ("you would have 1 bull from the 'o' and one cow from the 'd')\n")


def get_input():
    global guess
    global max_turn
    global turn
    global bulls
    global restart

    print ("\nThe word is {} letters long\nMake a guess!\n".format(word_len))
    while (turn < max_turn):
        guess = raw_input("> ")
        if (len(guess) == word_len):
            guess_word()
            turn += 1
        else:
            print ("\nPlease enter a {} letter word\n".format(word_len))
        if (bulls == word_len):
            win_msg()
            break
    if (turn == max_turn):
        lose_msg()
        restart = raw_input("Would you like to play again?\ny/n > ")
        if (restart == "y"):
            start_menu()
        else:
            return


def guess_word():
    global guess
    global i
    global k
    global bulls
    global cows
    global word_len

    bulls = 0
    cows = 0
    k = 0
    while (k < word_len):
        i = 0
        while (i < word_len):
            if (guess[i] == word[k]):
                if (i == k):
                    bulls += 1
                elif (i != k):
                    cows += 1
            i += 1
        k += 1
    print ("\nYour guess : {}".format(guess))
    print ("\nBulls : {}".format(bulls))
    print ("\nCows : {}".format(cows))
    print ("\nTurn : {}\nTurns remaining : {}\n".format(turn, max_turn - turn))

print_start()
