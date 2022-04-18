import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    # get user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('Letters used:', ' '.join(used_letters))
        # current word state
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1  # wrong guess - 1 live
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("Please enter a valid letter.")

    if lives == 0:
        print("You lost. The word was", word)
    else:
        print("You won! The word was", word)


if __name__ == '__main__':
    hangman()
