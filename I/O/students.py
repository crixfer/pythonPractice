import csv

name = input("What's your name? ")
home = input("What's your home? ")

#option 1

# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

#option 2 helps maintain the order of the rows based on the key values.

with open("students.csv", "a") as file:
    writer = csv.DicWriter(file, fieldname=["name", "home"])
    writer.writerow({"name": name, "home": home})