import random
easy_level_attempts=10
hard_level_attempts=5
def choose_level(level):
    if level == "easy":
        return easy_level_attempts
    elif level == "hard":
        return hard_level_attempts
    else:
        print("Invalid level")
def compare(number,guessed_number,attempts):
    if guessed_number > number:
        attempts=attempts - 1
        print("You guessed too high")
        if attempts ==-1:
            print("you lost")
    elif guessed_number < number:
        attempts=attempts - 1
        print("You guessed too low")
        if attempts ==-1:
            print("you lost")
    elif guessed_number == guessed_number:
        print("You guessed the number correctly!")

print("let me think a number between 1 and 50.")
number=random.randint(1,50)
# print(number)
level=input("Choose level of difficulty.... Type 'easy' or 'hard': ").lower()
attempts=choose_level(level)
guessed_number=0
while guessed_number!=number and attempts>0:

    print(f"You have {attempts} attempts remaining to guess the number.")
    attempts = attempts - 1
    guessed_number=int(input("Make a guess..."))
    compare(number,guessed_number,attempts)