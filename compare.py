#conditionals

a = int(input("What's a? "))
b = int(input("What's b? "))

if a > b:
    print("The value of 'a' is greater than 'b'")

elif a < b:
    print("The value of 'a' is lower than 'b'")

else:
    print("Both have the same value")

#***********************

if a < b or a > b:
    print("'a' is not equals to 'b'")

if a != b:
    print("They are different")

else:
    print("'a' is iquals to 'b'")