import os
import random
import graphics
import hard_words
"""Imports the external files for the graphics and the list of words"""

# hangman game that works with boolean values and functions

word = random.choice(hard_words.game_words)
word = word.upper()
reveal = list(len(word)*'_')
lives = 7
gameOver = False


def check_letters(letter, word):
    """
    Checks what letters have been put in by the user and reveals letter
    if correct.
    """
    global reveal
    for i in range(0, len(word)):
        letter = word[i]
        if attempt == letter:
            reveal[i] = attempt
    if '_' not in reveal:
        return True
    else:
        return False


def monitor():
    """Monitors your progress and lives left"""
    os.system('cls')
    print(graphics.hangman[7-lives])
    print(' '.join([str(e) for e in reveal]))
    print('You have', lives, 'shots left at this.')


while gameOver and lives > 0:
    """Prompts for user input"""
    monitor()
    attempt = input('Guess the entire word or a single letter: /n')
    attempt = attempt.upper()

    if attempt == word:
        gameOver = True
        reveal = word
    elif len(attempt) == 1 and attempt in word:
        gameOver = check_letters(attempt, word)
    else:
        lives -= 1
    monitor()


if gameOver:
    print('Well done on not letting an innocent man hang')
else:
    print('The innocent man has been hung. The word in question was: ', word)