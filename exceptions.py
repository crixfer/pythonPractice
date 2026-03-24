#Exceptions
# try:
#     x = int(input("What is X? "))
#     print(f"X is {x}")

# except ValueError:
#     print("x is not an integer")

# Function
# def main():
#     x = get_int()
#     print(f"X is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("What is X? ")) #return has also the power to break a loop
#         except ValueError:
#             print("X is not an integer!")


#reusable function
def main():
    x = get_int("What's X? ")
    print(f"x is {x}.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()