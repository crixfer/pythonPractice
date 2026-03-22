#iteration and functions

# def main():
#     square_size(3)

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

# Matrix - Con números (no strings)

count = 1
for i in range(3):
    for j in range(3):
        print(count, end=" ")
        count += 1
    print()  # Nueva línea después de cada fila


