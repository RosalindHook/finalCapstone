# imports tabulate and Shoe class from separate file
from tabulate import tabulate
from shoe_class import Shoe

# Empty list that will be used to store a list of objects of shoes
shoe_list = []


# creates functions outside the class
# print table function by calling the to_table() class method
def print_table():
    data_list = []
    # headings for table
    top_row = ["Country of manufacture", "Barcode", "Name of product", "Cost of product", "Quantity in stock"]
    # puts data into 2d list - can be used to create table
    for shoe_object in shoe_list:
        data_list.append(shoe_object.to_table())
    print(tabulate(data_list, top_row, tablefmt="grid"))


# function to open text file and read data, then create shoes object with the data
# it also appends the object into the shoes list
# error handling for if file does not exist or data for cost and quantity not as float/int
def read_shoes_data():
    try:
        inventory_file = open("inventory.txt", "r")
    except IOError:
        print("The necessary file does not exist - please create it before trying again")

    else:
        # skips reading first line of file (line 0)
        lines = inventory_file.readlines()[1:]
        # for each line splits by ',' and strips the newline break from last object in list
        for line in lines:
            try:
                country, code, product, cost, quantity = line.strip("\n").split(",")
                shoe_object = Shoe(country, code, product, float(cost), int(quantity))

            except IndexError:
                print(f'There is an error in your text file.')

            except ValueError:
                print(f'There is an error in your text file.')

            # proceeds to convert each line into object that is appended to shoe_list
            else:
                shoe_list.append(shoe_object)

        inventory_file.close()


# function to allow a user to input data about a shoe, which is used to create a shoe object
# appended inside the shoe list inventory. Although not required by this task this function
# also asks the user if they want to add the shoe info to their text file, and if so writes
# this into the text file by calling the to_file() class method
def capture_shoes():
    print("Please provide the information requested:")
    country = str(input("Where were these shoes made? "))
    code = str(input("What is the code for these shoes? "))
    product = str(input("What is the product reference? "))
    while True:
        try:
            cost = float(input("How much do these shoes cost? "))
            break
        except ValueError:
            print("Please try again, the cost needs to be a float or an integer, no symbols please!")

    while True:
        try:
            quantity = int(input("How many shoes are in stock? "))
            break
        except ValueError:
            print("Please try again and enter a number: ")

    shoe_object = Shoe(country, code, product, float(cost), int(quantity))
    shoe_list.append(shoe_object)
    add_to_file = input("This item has been added to your temporary inventory. Do you want to permanently "
                        "add it to your text file (y/n)? ").lower()
    if add_to_file == "y":
        file = open("inventory.txt", "a+")
        for shoe_object in shoe_list:
            file.write(f"\n{shoe_object.to_file()}")
        file.close()
        print("\nThis item has been written into your file.")

    elif add_to_file == "n":
        print("No problem, now return to the main menu.")
    else:
        print("I don't know that option - please return to the main menu.")


# function to iterate over shoe list and print details of the shoes returned from the
# class __str__ method. Checks if list is empty (i.e. if read function not yet called)
def view_all():
    if len(shoe_list) == 0:
        print("Your list is empty - you need to read your text file first to get the data.")
    else:
        print_table()


# function to find shoe object with the lowest quantity, and return the name and quantity to the user
# asks user if they want to add more stock, and if so updates this object
# asks user if they want to add the quantity info to their text file, and if so writes
# this into the text file by calling the to_file() class method
def re_stock():
    if len(shoe_list) == 0:
        print("Your list is empty - you need to read your text file first to get the data.")
    else:
        lowest_quant = min(shoe_list, key=lambda shoes: shoes.quantity)
        print(f"{lowest_quant.product} has the smallest quantity in stock: {lowest_quant.quantity} items")
        restock = input("Would you like to add more stock for this product (enter y or n): ").lower()
        if restock == "n":
            print("No worries, return to the main menu")
        elif restock == "y":
            while True:
                try:
                    new_quant = int(input("Enter the amount of additional stock for this product: "))
                    lowest_quant.quantity += new_quant
                    break
                except ValueError:
                    print("Please try again and enter a number: ")

            add_to_file = input("This item has been added to your temporary inventory. Do you want to permanently "
                                "add it to your text file (y/n)? ").lower()
            if add_to_file == "y":
                file = open("inventory.txt", "w")
                file.write(f"Country,Code,Product,Cost,Quantity")
                for shoe_object in shoe_list:
                    file.write(f"\n{shoe_object.to_file()}")
                file.close()
                print("\nThis item has been written into your file.")

            elif add_to_file == "n":
                print("No problem, now return to the main menu.")
            else:
                print("I don't know that option - please return to the main menu.")
        else:
            print("You have selected an invalid option.")


# asks user to input whether they want to search by code or product name
# calls user_code function or product_name function based on input.
# checks if list is empty (i.e. if read function not yet called)
def search_shoe():
    if len(shoe_list) == 0:
        print("Your list is empty - you need to read your text file first to get the data.")
    else:
        retrieve_item = input("Do you want to search by code reference or product name? Please enter the letter 'c' "
                              "for code or 'p' for product name: ").lower()
        if retrieve_item == "c":
            code_search(input("What is the code reference for this item (please note this reference must be entered "
                              "precisely and is case sensitive)?: "))
        elif retrieve_item == "p":
            prod_search(input("What is the product name for this item? "))
        else:
            print("You have selected an invalid option.")


# searches for shoe from list using shoe code entered by user, returns object as print using # class __str__ method
def code_search(user_code):
    shoe_pos = -1
    for index, shoe_object in enumerate(shoe_list):
        if shoe_object.code == user_code:
            shoe_pos = index
    if shoe_pos == -1:
        print(f"No product with code {user_code} found.")
    else:
        print("\nYour item was found:")
        print(shoe_list[shoe_pos])


# searches for shoe from list using product code entered by user, returns object as print using # class __str__ method
def prod_search(user_prod):
    shoe_pos = -1
    for index, shoe_object in enumerate(shoe_list):
        if shoe_object.product == user_prod:
            shoe_pos = index
    if shoe_pos == -1:
        print(f"No product by the name of {user_prod} found.")
    else:
        print("\nYour item was found:")
        print(shoe_list[shoe_pos])


# calculates total value for each item (value = cost * quantity) and prints info for all shoes
def value_per_item():
    if len(shoe_list) == 0:
        print("Your list is empty - you need to read your text file first to get the data.")
    else:
        print("\nHere are all your shoes and their value:")
        for shoe_object in shoe_list:
            value = shoe_object.cost * shoe_object.quantity
            print(f"{shoe_object.product} value: {value}")


# function to determine product with the highest quantity in stock.
# Asks user to put this on sale and provide a new value that is less than the current one -
# if this is the same or greater than current value asks for a new value, or updates object
# asks user if they want to add the new cost to their text file, and if so writes
# this into the text file by calling the to_file() class method
def highest_qty():
    if len(shoe_list) == 0:
        print("Your list is empty - you need to read your text file first to get the data.")
    else:
        highest_quant = max(shoe_list, key=lambda shoes: shoes.quantity)
        print(f"{highest_quant.product} has the highest amount of stock: {highest_quant.quantity} items in total.")
        print("This shoe needs to go on sale!")

        try:
            while True:
                sale = int(input(f"The price is currently {highest_quant.cost}. Please enter a sale value: "))
                if sale >= highest_quant.cost:
                    print(f"Please enter a sale value that is less than the current price - {highest_quant.cost}: ")
                else:
                    highest_quant.cost = sale
                    break

        except ValueError:
            print("Please try again and enter a number: ")

        add_to_file = input("This sale price has been added to your temporary inventory. Do you want to permanently "
                            "add it to your text file (y/n)? ").lower()
        if add_to_file == "y":
            file = open("inventory.txt", "w")
            file.write(f"Country,Code,Product,Cost,Quantity")
            for shoe_object in shoe_list:
                file.write(f"\n{shoe_object.to_file()}")
            file.close()
            print("\nThis item has been written into your file.")

        elif add_to_file == "n":
            print("No problem, now return to the main menu.")
        else:
            print("I don't know that option - please return to the main menu.")


# main menu
# functions (outside the Shoe Class) that will be called based on user input
# while loop while user_choice is not equal to quit, keeps offering main menu choices
user_choice = ""

while user_choice != "quit":
    user_choice = input("""\nWhat would you like to do now with your inventory? 
    Enter the command on the left to select an option:\n 
Read \t\t\t\t- allows you to read data from a file
Add \t\t\t\t- allows you to add new data about a shoe
View all \t\t\t- allows you to see the information in your shoe inventory
Restock \t\t\t- lets you see and restock the shoes with the lowest quantity
Search \t\t\t\t- lets you search for information about a shoe by code or product name 
Value \t\t\t\t- allows you to find out the total value for each item
Highest \t\t\t- lets you see the shoes with the highest quantity and asks you to put these on sale
Quit \t\t\t\t- quit this programme\n\n""").lower()
    if user_choice == "read":
        read_shoes_data()
    elif user_choice == "add":
        capture_shoes()
    elif user_choice == "view all":
        view_all()
    elif user_choice == "restock":
        re_stock()
    elif user_choice == "search":
        search_shoe()
    elif user_choice == "value":
        value_per_item()
    elif user_choice == "highest":
        highest_qty()
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input, please try again!")
