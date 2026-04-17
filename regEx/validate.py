import re

email = input("What's your email? ").strip()


if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.do$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")



# username, domain = email.split("@") # split() separates the variables with whatever is inside the parenthesis

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")