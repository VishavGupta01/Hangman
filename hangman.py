import random as ran


def hang1():
    print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')


def hang2():
    print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')


def hang3():
    print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')


def hang4():
    print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')


def hang5():
    print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')


def hangman():
    words = ['apple', 'above', 'about', 'adore', 'actor']
    word = ran.choice(words)
    lives = 5

    guess = "_" * len(word)

    while lives != 0:
        print(guess)
        userinput = input("Guess a Letter :").lower()
        if userinput in word:
            for index in range(len(word)):
                if word[index] == userinput:
                    guess = guess[:index] + userinput + guess[index + 1:]
            if guess == word:
                print("Congrats!! You won the Game!!")
                break
        else:
            lives -= 1
            print("Incorrect!!")
            print("Remaining Chances", lives)
            if lives == 4:
                hang1()
            elif lives == 3:
                hang2()
            elif lives == 2:
                hang3()
            elif lives == 1:
                hang4()
            elif lives == 0:
                hang5()
    else:
        print("Game Over!")
        print("The Correct Word was", word)


play = input("Enter 'yes' to start the game or 'no' to exit : ").lower()
if play == "yes" or play == "y":
    hangman()
elif play == "no":
    print("OK, See you Next Time!")
