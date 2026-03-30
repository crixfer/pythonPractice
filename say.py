# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1]) #prints a cow that greets the user.

def main():
    hello()
    goodbye()

def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"Goodbye, {name}")


if __name__ == "__main__":
    main()