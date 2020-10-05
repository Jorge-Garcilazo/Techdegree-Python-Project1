import random


def playAgain():
    checkPlayAgain = True
    while checkPlayAgain:
        playAgain = input('Would you be intrested to play again? Please type "Yes" or "No"\n')
        playAgain = playAgain.lower()
        if playAgain == 'yes':
            print('The highscore is {}, can you beat it?'.format(highscore))
            startGame()
        elif playAgain == 'no':
            print('Thanks for playing!')
            quit()
        else:
            print('Sorry my programer made it so I can only understand "Yes" or "No" please type you answer again :)')
            continue


def startGame():
    answer = random.randint(1, 10)
    attempts = 1
    game = True

    while game == True:
        guess = input('Guess a number between 1-10\n')
        
        try:
            guess = int(guess)
        except ValueError:
            print('Sorry, please type in a numerical number!')
            continue
        
        guess = int(guess)
        if guess < 1 or guess > 10:
            print('Sorry, your guess must be with in the number range of 1-10.')
            continue
        
        
        if guess == answer:
            print('Hey good job! You guessed it right! :D')
            print('The game has ended and you did it in {} trie(s)!'.format(attempts))
            if attempts < highscore[0]:
                highscore.pop()
                highscore.append(attempts)
            playAgain()
        elif guess < answer:
            print('Sorry, its actually higher!')
            attempts += 1
        else:
            print('Sorry, its actually lower!')
            attempts += 1


highscore = [100]
print('-=-=-=-Welcome the the Guessing Game!-=-=-=-')
      
startGame()