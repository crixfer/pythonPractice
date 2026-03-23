#Login System

users = []

while True:
    menu = print("\nSelect an option.\n \n  1. Register \n  2. Login \n  3. See Users \n  4. Remove User \n  5. Exit App")
    option = int(input(" \nOption: "))

#   option 1 REGISTER
    if option == 1:

        username = input("\nWrite username: ")
        pssw = input("\nWrite password: ")

        registry = {
            "username": username,
            "password": pssw,
        }

        users.append(registry)

        print("\n  Registered successfully!\n")

#   option 2 LOGIN
    if option == 2:

        if not users:
            print("There is no registry.")

        else:
            login = input("Write your existing username: ")
            loginPssw = input("Write your existing password: ")

            if login == registry["username"] and loginPssw == registry["password"]:
                print(f"\n Welcome to the system! {registry["username"]}\n")

            else:
                print("\n  Incorrect username or password!\n")

#   option 3 SEE USERS
    if option == 3:

        if not users:
            print("\nEmpty list.")

        else:
            for i, user in enumerate(users):
                print("\n", i + 1, "- User: ", user["username"])
   
#   option 4 Remove Users
    if option == 4:

        user2remove = int(input("\n Select user to be removed \nOption: "))-1

        if not users:
            print("\n User does not exist!")

        else:
            if user2remove >= 0 and user2remove < len(users):
                if users[user2remove]["username"]:

                    users.pop(user2remove)
                    print("\nUser deleted successfully!")



#   option 5 Exit app
    if option == 5:

        print("'Thanks for using our Login System'")
        break







