import random
from stages import stages, banner
from words import word_list
import os
os.system('cls||clear') # clears the previous terminal text

game_over = False
lives = 6
chosen_word = random.choice(word_list)

print(banner)

# print(chosen_word)

display = []

for _ in chosen_word:
    display.append("_")

print(' '.join(display) + "\n")

def add_to_word(guessed_letter):
    if guessed_letter in chosen_word:
        if guessed_letter not in ''.join(display):
            print("\nCorrect, the letter has been added!\n")
        else:
            print("\nYou have already guessed this letter before\n")

    for pos in range(len(chosen_word)):
        if guessed_letter == chosen_word[pos]:
            display[pos] = guessed_letter

def add_to_hangman(guessed_letter,nr_lives):
    if guessed_letter not in chosen_word:
        nr_lives -= 1
        print("\nWrong, you have lost a life!\n")   
    return nr_lives

def check_game_over():
    if ''.join(display) == chosen_word:
        print("You win!")
        return True

    elif lives == 0:
        print("You lose!\n")
        print(f"The correct word was {chosen_word}")
        return True
    else:
        return False

def clear():
     os.system('cls' if os.name=='nt' else 'clear')
     return("   ")

while game_over is False:
    guess = input("Guess a letter from the word:\n").lower()
    clear()
    add_to_word(guess)
    lives = add_to_hangman(guess,lives)
    
    print(' '.join(display))
    print(stages[lives])

    game_over = check_game_over()