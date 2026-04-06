#Practicing python
# def questions():
#     name = input("What's your name? ").title().strip()
#     greet(name)


# def greet(to):
#     print("Hi,", to, "Welcome to Wednesday!")

# questions()

# from random import randint

# randomNumber = randint(1,10)
# print(randomNumber)

import random

cards = ["queen", "king", "jack", "joker"]

random.shuffle(cards)
print(cards)

for card in cards:
    print(card)

