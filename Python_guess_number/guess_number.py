import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess number between 1 and {x}: "))
        if guess < random_number:
            print("Too low")
        elif guess > random_number:
            print("Too high")

    print("You got it!!!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        guess = random.randint(low, high)
        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print("Computer guessed your number!!!")
