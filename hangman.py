# import random
# import hangman_stages
#
# fruits = ['apple', 'banana', 'mango', 'pineapple', 'orange', 'strawberry', 'grapes', 'guava', 'watermelon', 'papaya']
# fruit = random.choice(fruits)
# count = len(fruit)
# lives = 6
#
# display = []
# for letter in fruit:
#     display += '_'
# print(display)
# game_over = False
# while not game_over:
#     guessed_letter = input('Guess a letter: ').lower()
#     for position in range(len(fruit)):
#         letter = fruit[position]
#         if letter == guessed_letter:
#             display[position] = guessed_letter
#     print(display)
#     if guessed_letter not in fruit:
#         lives -= 1
#
#         if lives == 0:
#             game_over = True
#             print('You lose!')
#     if '_' not in display:
#         game_over = True
#         print('You win!')



import random
import hangman_stages
fruits = ['apple', 'banana', 'mango', 'pineapple', 'orange', 'strawberry', 'grapes', 'guava', 'watermelon', 'papaya']
chosen_fruit=random.choice(fruits)
count=len(chosen_fruit)
display=[]
chances=6
for i in chosen_fruit:
    display+="_"
print(display)

out_of_moves=False
while not out_of_moves:
    guessed_letter=input(f"Enter a letter(you have {chances} chances):").lower()

    for j in range(count):
        letter=chosen_fruit[j]
        if letter==guessed_letter:
            display[j]=guessed_letter
    print(display)
    print(hangman_stages.stages[chances])
    if guessed_letter  not in chosen_fruit:
        chances-=1

        if chances==0:
            out_of_moves=True
            print("you lost")
    if '_' not in display:
        out_of_moves = True
        print("you won")
