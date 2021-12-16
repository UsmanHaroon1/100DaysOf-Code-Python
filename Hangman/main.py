# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import words
import art
import random

print(art.logo)
word = random.choice(words.word_list)
word_char_list = []
for char in word:
    word_char_list.append(char)

print(f"Selected word is:{word}")
display=[]

for i in range(len(word)):
    display.append('_')
end_of_game = False
life=6
while not end_of_game:
    user_input = input("Guess a letter:").lower()
    if user_input=="":
        print("Please make a guess")
        continue
    if user_input in display:
        life -= 1
        print(f"You have already guessed it!!{life} guess left")
        print(art.stages[life])

    elif user_input in word_char_list:
        for pos in range(len(word)):
            if user_input == word_char_list[pos]:
                display[pos]=user_input
    else:
        life-=1
        print(f"You made a wrong guess, Please try again and remember you have {life} guess left")
        print(art.stages[life])
    if not "_" in display:
        end_of_game = True
        print("You have won the game!!")
    if life==0:
        end_of_game=True
        print("You lost")
    print(f"{''.join(display)}")


