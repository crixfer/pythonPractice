name = input("What's your name? ")
level = input("What's your English level? ")

with open("registry.csv", "a") as file:
    file.write(f"{name}, {level}\n")