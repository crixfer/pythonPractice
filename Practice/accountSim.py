# saldo = 1000
amount = 1000
# mientras True:
#     mostrar menú:
#         1. Ver saldo
#         2. Depositar
#         3. Retirar
#         4. Salir
while True:
#     pedir opción
    option = int(input("\nChoose an option from the menu: \n\n 1. Current Amount \n 2. Deposit \n 3. Withdraw \n 4. Exit \n\nOption: "))
#     si opción == 1:
    if option == 1:
#         mostrar saldo
        print("-------------------------------------")
        print(f"Your current amount is: ${amount}.00")
        print("-------------------------------------")
    
#     si opción == 2:
    if option == 2:
#         pedir monto
        deposit = int(input("How much are you going to deposit? \n\nInsert the desired amount: "))
        print(f"\nYou have deposited ${deposit}.00")
        print("-------------------------------------")
#         saldo = saldo + monto
        amount = amount + deposit
        print(f"Your new amount is: ${amount}.00")
        print("-------------------------------------")


#     si opción == 3:
    if option == 3:
#         pedir monto
        withdraw = int(input("\nHow much do you need? \n\nInsert the desired amount: "))
#         si monto > saldo:
        if withdraw > amount:
#             mostrar "fondos insuficientes"
            print("\n-------------------------------------")
            print("You have insuficient funds for this transaction!")
            print("-------------------------------------")
#         sino:
        else:
#             saldo = saldo - monto
            amount = amount - withdraw
            print("\n-------------------------------------")
            print(f"After this transaction, you have ${amount}.00 remaining.")
            print("-------------------------------------")

#     si opción == 4:
    if option == 4:
#         salir del programa
        print("\n Thanks for using our services. Come back soon!\n")
        break