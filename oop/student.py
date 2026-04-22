#OOP

#   simple option
# name = input("Name ")
# house = input("House ")


#   functions option 1
# def main():
#     name = input("What's your name? ")
#     house = input("What's your house name? ")
#     print(f"{name} from {house}.")


#   functions option 2
# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}.")

# def get_name():
#     return input("What's your name? ")

# def get_house():
#     return input("What's your house's name?")


#   functions option 3
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}.")

def get_student():
    # student = {}
    # student["name"] = input("name: ")
    # student["house"] = input("House: ")
    # return student
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

# (name, house) cannot be change when adding information if declared in a specific way.
# [name, house] can be changed.

if __name__ == "__main__":
    main()