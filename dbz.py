#MATCH = Switch for python

type = input("Who is it? ").title()

match type:
    case "Goku" | "Vegeta" | "Gohan" | "Trunks" | "Goten":
        print("Sayan")
    case "Krillin" | "Bulma" | "Roshi" | "Yamcha" | "Tenchinhan":
        print("Human")
    case "Picoro":
        print("Namekian")
    case _:
        print("Not a dbz character!")
