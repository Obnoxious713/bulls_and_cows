words4 = ['word']#, 'node', 'help', 'four']
done = 0
i = 0
j = 0
k = 0
bulls = 0
cows = 0

def print_menu():
    print('''
 ____                               ___
|    |	|       |   |       |      /   \                                       .
|    /	|       |   |       |     |     |
|---	|       |   |       |      \ __
|    \	|       |   |       |           \                                      .
|____|	 \ ___ /    |____   |____  \____/
     _____
   /       \                                                                   .
   \       /
    \     /
      \  /
     /   \                                                                     .
    /     \   /
    \_____/ \/
  _____     _____                        ___
 /        / 	  \   |      |      |   /   \                                  .
|        |         |  |      |      |  |     |
|        |         |   \    / \    /    \ __
|        |         |    \  /   \  /          \                                 .
 \_____	  \ _____ /      \/     \/      \____/
 ''')

def print_instructions():
    print ("Welcome to the game of Bulls and Cows\n")
    print ("A ___ letter word will be chosen at random")
    print ("Your goal is to guess the word in as few tries as possible")
    print ("The word will not contain more than one of the same letter\n")
    print ("After making a guess you will be shown the number of 'bulls' and 'cows' you have\n")
    print ("A 'bull' means that one of the letters is correct and in the correct location")
    print ("A 'cow' means that one of the letters is correct but it is not in the correct location")
    print ("\nex: if the word is\n  'word'\nif you were to guess\n  'node'\nyou would have 1 bull (o) and one cow (d)")


def get_input():
    global done

    guess = input("Guess a ___ letter word\n>")
    guess_word()

def guess_word():
    global guess
    global i
    

    while (guess[i] != '\0'):
        while (words4[j][k] != '\0'):
            if (guess[i] == words4[j][k] & i == k):
                bulls += 1
            elif (guess[i] == words4[j][k] & i != k):
                cows += 1
            k += 1
        i += 1
    print ("Bulls : " + bulls)
    print ("Cows : " + cows)

print_menu()
print_instructions()
get_input()
