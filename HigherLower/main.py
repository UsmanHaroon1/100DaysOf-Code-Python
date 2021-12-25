import art
import data
import random

print(art.logo)
IsEndGame = False

current_score = 0
while IsEndGame is False:

    dict1 = random.choice(data.data)
    random.shuffle(data.data)
    dict2 = random.choice(data.data)

    print(f"Compare A:{dict1['name']}, a {dict1['description']} from {dict1['country']}")

    print(art.vs)

    print(f"Against B:{dict2['name']}, a {dict2['description']} from {dict2['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B':").lower()

    if dict1['follower_count'] > dict2['follower_count']:
        true_answer = 'A'.lower()
    else:
        true_answer = 'B'.lower()

    if user_choice == true_answer:
        current_score+=1
        print(f'You are Right!Current score is {current_score}')
    else:
        IsEndGame = True
        print(f'You are wrong!Final score is: {current_score}')