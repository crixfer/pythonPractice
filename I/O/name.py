# name = input("What's your name? ")

# file = open("names.txt", "a") #w for write, a for append
# file.write(f"{name}\n")
# file.close()

#open and automatically close the file
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

with open("names.txt", "r") as file: #r for reading files
    for line in sorted(file, reverse = True):
        print("hello,", line.rstrip())




# names = []

# for _ in range(3):
#     name = input("What's your name? ")
#     names.append(name)
    
# print(name)

# for _ in range(3):
#     names.append(input("What's your name? "))

# #sorting alphabethically
# for name in sorted(names):
#     print(f"hello, {name}")