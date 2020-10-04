import random

print('-=-=-=-Welcome the the Guessing Game!-=-=-=-')

answer = random.randint(1, 10)
attempts = 1

while True:
    guess = input('Guess a number between 1-10\n')
    
    try:
        guess = int(guess)
    except ValueError:
        print('Sorry, please type in a numerical number!')
        continue
    
    guess = int(guess)
    
    if guess == answer:
        print('Hey good job! You guess right! :D')
        print('You did it in {} trie(s)!'.format(attempts))
        print('The game has now ended thanks for playing!')
        break
    elif guess < answer:
        print('Sorry, its actually higher!')
        attempts += 1
    else:
        print('Sorry, its actually lower!')
        attempts += 1
            

