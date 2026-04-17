# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} lives in {house}")
import csv

family = []

with open("names.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            family.append({"name": row["name"], "home": row["home"]})
        # name, house = line.rstrip().split(",")
        # member = {}
        # member["name"] = name
        # member["house"] = house
        # member = {"name": name, "house": house}
        # family.append(member)

# def get_name(member):
#     return member["name"]

for member in sorted(family, key = lambda memberName: memberName["name"]):
    print(f"{member['name']} lives in {member['home']}")


