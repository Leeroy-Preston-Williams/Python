import random

animals = ['ape', 'baboon', 'crocodile', 'dog', 'elephant', 'frog','girrafe','hippopotamus','iguana']
places = ['argentina', 'barcelona', 'chile', 'denmark', 'ethiopia', 'france', 'germany', 'hungary', 'italy']
cars = ['alpha', 'bently', 'chevrolet', 'datsun', 'ford', 'gumpert', 'hummer', 'infinity']

def playHangman(wordToGuess):
    word = wordToGuess
    wordToDisplay = ''
    guessed = []
    incorrect = 0

    for i in range(0,len(word)):
        wordToDisplay = wordToDisplay + '*'
    wordToDisplay = list(wordToDisplay)

    playing = True

    HANGMAN = (
    """
    _________
    |/      |
    |
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    _________
    |/      |
    |     ('_')
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    _________
    |/      |
    |     ('_')
    |      -+-
    |
    |
    |
    |
    |
    --------
    """,
    """
    _________
    |/      |
    |     ('_')
    |     /-+-
    |
    |
    |
    |
    |
    --------
    """,
    """
    _________
    |/      |
    |     ('_')
    |     /-+-\ 
    |
    |
    |
    |
    |
    --------
    """,
    """
    _________
    |/      |
    |     ('_')
    |     /-+-\ 
    |       | 
    |
    |
    |
    |
    --------
    """,
    """
    _________
    |/      |
    |     ('_')
    |     /-+-\ 
    |       | 
    |       | 
    |
    |
    |
    --------
    """,
    """
    _________
    |/      |
    |     ('_')
    |     /-+-\ 
    |       | 
    |       | 
    |      /
    |     
    |
    --------
    """,
    """
    _________
    |/      |
    |     ('_')
    |     /-+-\ 
    |       | 
    |       | 
    |      /
    |     /
    |
    --------
    """,
    """
    _________
    |/      |
    |     ('_')
    |     /-+-\ 
    |       | 
    |       | 
    |      / \\
    |     /   
    |
    --------
    """,
    """
    _________
    |/      |
    |     ('_')
    |     /-+-\ 
    |       | 
    |       | 
    |      / \\
    |     /   \\
    |
    --------
    """)


    while playing:
        game = (word != ''.join(wordToDisplay))
        if(game):
            print(HANGMAN[incorrect] + "\n")
            attempts = len(HANGMAN) 
            print(''.join(wordToDisplay))
            print("\nAttempts Remaining: " + str(attempts - incorrect))
            guess = input('Enter your guess: \n')
            guessed.append(guess)
            
            if(guess in wordToDisplay):
                print('\nAlready Guessed This Letter!')
            elif(guess in word):
                for x in range(0,len(word)):
                    if guess == word[x]:
                        wordToDisplay[x] = guess
            elif(incorrect+1 == attempts):
                print("\nGame Over!\n\nCorrect Word: " + word)
                game = False
                playing = False
            else:
                incorrect = incorrect + 1
        else:
            print('\nCongratulations! You have guessed correctly!\n')
            playing = False
        

if __name__ == "__main__":
    print(
'''
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                                
                        Y8b d88P                                          
                         "Y88P"          github.com/ibraaheem              
''')
    print('\n\nCategories:\n\n1)Animals\n2)Places\n3)Cars\n')
    
    try:
        selection = int(input("Choose a category(eg. 1): "))
        if selection == 1:
            word = random.choice(animals)
        elif(selection == 2):
            word = random.choice(places)
        else:
            word = random.choice(cars)
        playHangman(word)
    except:
        print("\nplease specify a number!\n")

            



