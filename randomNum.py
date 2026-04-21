import random

randomNumber = random.randint(1,10)

userNumber = int(input("What's the number? "))

if userNumber == randomNumber:
    print("You win!")
else:
    print("Keep trying.")