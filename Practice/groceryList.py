#Grocery List

products = []

while True:
    menu = int(input("Choose an option from the menu:\n \n  1. Add Items \n  2. See List \n  3. Change Status \n  4. Remove Item \n  5. Exit App \n\nOption: "))
    
    if menu == 1:
        #ask for items
        add_item = input("Add items to your grocery list: \nItem Name: ")
        add_qty = int(input("Specify the amount: \nAmount: "))

        if add_qty == 0:
            continue
        #dictionary to add the items
        new_items = {
            "item_name": add_item,
            "quantity": add_qty,
            "bought": False,
        }
        
        products.append(new_items)

    #option 2 see the list
    elif menu == 2:
        #iterate the product list
        if not products:
            print("NO ITEMS")
            
        else:
            for i, item in enumerate(products):
                if item["bought"] == True:
                    status = "Bought"
                else:
                    status = "Need"
                print(i + 1, "-", item["item_name"], "- Quantity: ", item["quantity"], status)

    #option 3 change status
    elif menu == 3:
        #asking for item to change status to
        item_id = int(input("What item number what to change to bought? \nOption: ")) -1

        if item_id >= 0 and item_id < len(products):
            if products[item_id]["bought"] == False:
                products[item_id]["bought"] = True
                print("\nStatus changed!\n")


     #option 4 remove items
    elif menu == 4:
        item_rmv = int(input("What item to remove? \nOption: ")) -1
        if item_rmv >= 0 and item_rmv < len(products):

            products.pop(item_rmv)
            print("Item removed!")

     #option 5 exit app
    elif menu == 5:    
        print("Thanks for using this app!")
    break 




