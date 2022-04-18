import random
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(word)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # get user input
    while len(word_letters) > 0:
        # letters used
        print('Letters used:', ' '.join(used_letters))
        # current word state
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('current word:', ' '.join(word_list))

        user_letters = input("guess a letter: ").upper()
        if user_letters in alphabet:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)

        elif user_letters in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("Please enter a valid letter.")


user_input = input("Guess a letter: ")
print(user_input)
