#Practicing python
def questions():
    name = input("What's your name? ").title().strip()
    greet(name)


def greet(to):
    print("Hi,", to, "Welcome to Wednesday!")

questions()