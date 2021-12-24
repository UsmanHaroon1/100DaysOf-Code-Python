import random
import art


print(art.logo)
print('Welcome to the number guessing game')

level_choice = input("Choose Level:Easy or Hard").lower()
print('Guess the number in the range of 0-100')

choosed_number = random.randint(0,100)

if(level_choice == 'easy'):
    life = 10
else:
    life = 3

while not life == 0:
    print(f"You have {life} remaining to guess")
    user_input= int(input("Make a guess:"))
    if(user_input == choosed_number):
        print('Right answer')
        break
    elif(user_input > choosed_number):
        print('Guess is too high')
        life-=1
    else:
        print('Guess is too low')
        life -= 1

print(f"Guessed number is {choosed_number}")