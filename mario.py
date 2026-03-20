#iteration and functions

def main():
    square_size(3)

#option 1

# def square_size(size):
#     #for each row in square
#     for i in range(size):

#         #for each brick in row
#         for j in range(size):

#             #prints brick
#             print("#", end="")
#         print()

#option 2

# def square_size(size):
#     #for each row in square
#     for i in range(size):

#         #for each brick in row
#         for j in range(size):

#             #prints brick
#             print("#", end="")
#         print()

#option 3

# def square_size(size):
#     for i in range(size):
#         print_row(size)

# def print_row(width):
#     print("#" * width)


# main()

# Matrix

number = 0

def matrix():
    counter(3)

def counter(n):
    for i in range(n):
        n += 1
        each_number(n)

def each_number(num):
    print(num * num)

matrix()


