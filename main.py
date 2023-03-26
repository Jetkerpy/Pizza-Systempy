"""
--- Display header ---
-- START LOOP
    - display pizza
    - get user's choice
    - (L) List of pizza
    - (A) Add a pizza
    - (R) Remove a pizza
    - (E) Edit a pizza
    - (S) Save a pizza to csv
    - (G) Get pizza data from csv
    - (Q) Quit
"""
import os
import time
import pandas as pd
import glob

def display_header():
    print(f"{'-' * 5} Welcome to Pizza Order {'-' * 5}")


def display_goodbye():
    print(f"\t\t{'-' * 5} GoodBye {'-' * 5}")
    time.sleep(2)
    os.system('cls')


def get_user_choice():
    choices = """       \n\t\t Pizza System\n
        - (L) List of pizza
        - (A) Add a pizza
        - (R) Remove a pizza
        - (E) Edit a pizza
        - (S) Save a pizza order
        - (G) Get pizza data from csv
        - (Q) Quit

choice one of them: """
    choice = input(choices).upper()
    return choice


# ADD PIZZA
def add_pizza(pizzas: list):
    os.system("cls")
    size = input("Enter pizza size (S, M, L): ")[0].upper()
    print("Toppings") # Yag'niy pizza nin' ustine qoyilatug'in qismi
    toppings = []
    while True:
        topping = input("Enter a topping or enter to stop (Q, E): ")
        if topping not in ['Q', 'q', 'e', 'E']:
            toppings.append(topping.upper())
            continue
        break
    pizza = {"id": 1 if not pizzas else len(pizzas) + 1, 'size': size, 'toppings': toppings}
    pizzas.append(pizza)
# END ADD PIZZA


# DISPLAY PIZZA LIST
def display_pizzas(pizzas):
    if not pizzas:
        print(f'\n {"-" * 70}\n')
        print("\t\tSorry pizza list empty.")
        print(f'\n {"-" * 70}\n')
    else:
        for pizza in pizzas:
            print(f'{"-" * 70}')
            print(f"---- id: {pizza['id']}, size: {pizza['size']}, toppings: {', '.join(pizza['toppings'])}")
        print(f'{"-" * 70}')
# END DISPLAY PIZZA LIST


#  REMOVE PIZZA
def remove_pizza(pizzas: list):
    """
    This function removed pizza by choosed pizza id from pizzas array :)
    """
    pizza_ids= [_id['id'] for _id in pizzas] #For check pizza id array 
    choose_id = 'Choose pizza by id to remove or to stop (Q, E): '
    while (_id := input(choose_id)) not in ['Q', 'E', 'q', 'e']:
        if _id.isdigit():
            pizza_id = int(_id)
            if pizza_id in pizza_ids:
                pizzas = [pizza for pizza in pizzas if pizza['id'] != pizza_id] #remove pizza
                print("Successfully removed pizza.")

                if not pizzas: #If pizza array pustoy bolsa automatically break (toqtatiw)
                    break
                else:
                    again = input('Do you would like to remove again (y, n): ').lower() #ask again
                    if again == 'y':
                        continue
                    break

            else:
                print("You entered wrong pizza's id.")
        else:
            print("Enter number.")
    return pizzas
#  END REMOVE PIZZA


#  EDIT PIZZA 
def check_id_from_pizza_arr(pizza_id: str, pizzas: list):
    pizza_ids = [pizza['id'] for pizza in pizzas]
    while True:
        if pizza_id.isdigit():
            pizza_id = int(pizza_id)
            if pizza_id in pizza_ids:
                return int(pizza_id)
            else:
                pizza_id = input("You choiced wrong pizza's id so choice again: ")
        else:
            pizza_id = input("You must enter number: ")


# EDIT SIZE OF PIZZA
def choice_size(size):
    while True:
        if size == 'S': # Size is S (Small)
            print("Choice size one of them [Medim (M), Large (L)]")
            size = input("Enter size: ").upper()
            if size in ['M', 'L']:
                return size
            else:
                print("You entered wrong size")
                continue

        elif size == 'M':
            print("Choice size one of them [Small (S), Large (L)]")
            size = input("Enter size: ").upper()
            if size in ['S', 'L']:
                return size
            else:
                print("You entered wrong size")
                continue

        elif size == 'L':
            print("Choice size one of them [Small (S), Medium (M)]")
            size = input("Enter size: ").upper()
            if size in ['S', 'M']:
                return size
            else:
                print("You entered wrong size")
                continue

            

def edit_size_of_pizza(pizza_id, pizzas):
    _id = check_id_from_pizza_arr(pizza_id, pizzas)
    for pizza in pizzas:
        if pizza['id'] == _id:
            size = choice_size(pizza['size'])
            pizza['size'] = size
    return pizzas
# END EDIT SIZE OF PIZZA


# EDIT TOPPING OF PIZZA
def add_new_topping(pizza_id, pizzas: list):
    while True:
        new = input('Enter new topping: ').upper()
        for pizza in pizzas:
            if pizza['id'] == pizza_id:
                pizza['toppings'].append(new)
        print("Successfully added.")
        again = input("Do want to add again (y/n): ").upper()
        if again == 'Y':
            continue
        break
    return pizzas


def change_topping_in_pizza(pizza_id, pizzas: list):
    os.system("cls")
    while True:
        for pizza in pizzas:
            if pizza['id'] == pizza_id:
                print(f"To change toppings: {pizza['toppings']}")
                topping = input("Enter one topping correctly to change: ").upper()
                if topping in pizza['toppings']:
                    topping_id = pizza['toppings'].index(topping)
                    pizza['toppings'][topping_id] = input("Enter new topping instead of old topping: ").upper()
                    print("Successfully changed.")
                    
                else:
                    print("You entered incorrectly.")

        return pizzas


def edit_topping_of_pizza(pizza_id: str, pizzas: list):
    _id = check_id_from_pizza_arr(pizza_id, pizzas)
    question = "Do you want to add new (N) or change (C) to stop (E, Q): "
    while (ques := input(question).upper()) not in ['E', 'Q']:
        if ques == 'N': # ADD NEW TOPPING TO PIZZA
            pizzas = add_new_topping(_id, pizzas)
        
        elif ques == 'C':
            pizzas = change_topping_in_pizza(_id, pizzas)
            
        else:
            print("Choice one them ('Add new (N) or Change (C)').")

    return pizzas
# END EDIT TOPPING OF PIZZA


def edit_pizza(pizzas: list):
    choice_size_or_topping = "To edit choice Size (s) or Topping (t). To stop (e/q): "
    while (choiced := input(choice_size_or_topping).upper()) not in ['E', 'Q']:
        if choiced == 'S': # EDIT SIZE OF PIZZA
            display_pizzas(pizzas)
            _id = input("Choice pizza id for edit pizza's size: ")
            pizzas = edit_size_of_pizza(_id, pizzas)
            print("Successfully edited size.")
        
        elif choiced == 'T': # EDIT TOPPING OF PIZZA
            display_pizzas(pizzas)
            _id = input("Choice pizza id for edit pizza's topping: ")
            pizzas = edit_topping_of_pizza(_id, pizzas)

        else:
            print("Invalid choiced.")
    return pizzas
#  END EDIT PIZZA 


# SAVE PIZZA ARRAY TO CSV FILES
def get_files():
    current_file = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(current_file)
    csv_files = glob.glob(os.path.join(BASE_DIR, '*.csv')) # GLOB IS ALLOW US TO GET ONLY .CSV FILES FROM BASE DIR 
    csv_file_names = [os.path.basename(file) for file in csv_files]
    return csv_file_names



def save_pizza_to_csv_file(pizzas: list):
    file_name = input("Enter new file name: ").lower()
    new_file = f"{file_name}.csv"
    file_names = get_files()
    if new_file not in file_names:
        pf = pd.DataFrame(pizzas)
        pf.to_csv(new_file, index=False)
        print(f"Successfully saved to {new_file}.")

    else:
        print(f"You can't save to that {new_file} because this file exist.\nFiles: {file_names}")
# END SAVE PIZZA ARRAY TO CSV FILES


# GET PIZZA DATA FROM CSV
def get_pizza_data_from_csv():
    files = get_files()
    if files:
        print(f"Choice one them files {files}")
        file_name = input("Enter only file name: ").lower()
        file = f"{file_name}.csv"
        if '.csv' not in file_name and file in files:
            data = pd.read_csv(file)
            os.system("cls")
            print(f'\n {"-" * 70}\n')
            print(data)
            print(f'\n {"-" * 70}\n')
        else:
            print("You must enter only file name like (pizza not as pizza.csv)")
    else:
        print("You don't have csv file.")
# END GET PIZZA DATA FROM CSV


def main():
    display_header()
    pizzas = [] #pizza array
    while True:
        choice = get_user_choice()
        if choice in ['A', 'R', 'E', 'S', 'Q', 'L', 'G']:

            if choice == 'Q': # QUIT FROM PROGRAMM
                display_goodbye()
                break
            
            elif choice == 'A': # ADD PIZZA
                add_pizza(pizzas)
            
            elif choice == 'L': # LIST OF PIZZA
                display_pizzas(pizzas)
            
            elif choice == 'R': # REMOVE PIZZA
                if pizzas:
                    os.system("cls")
                    display_pizzas(pizzas)
                    pizzas = remove_pizza(pizzas)
                else:
                    print(f'\n {"-" * 70}\n')
                    print("\t\tPizza doesn't exist.")
                    print(f'\n {"-" * 70}\n')

            
            elif choice == 'E': # EDIT PIZZA
                if pizzas:
                    os.system("cls")
                    pizzas = edit_pizza(pizzas)
                else:
                    print(f'\n {"-" * 70}\n')
                    print("\t\tPizza doesn't exist.")
                    print(f'\n {"-" * 70}\n')


            elif choice == 'S': # SAVE TO CSV FILE
                if pizzas:
                    os.system("cls")
                    save_pizza_to_csv_file(pizzas)
                else:
                    print(f'\n {"-" * 70}\n')
                    print("\t\tPizza doesn't exist.")
                    print(f'\n {"-" * 70}\n')

            elif choice == 'G': # GET FROM CSV FILES
                get_pizza_data_from_csv()
    

        else:
            print(f'\n {"-" * 70}\n')
            print("\t\tWrong choiced please enter correctly.")
            print(f'\n {"-" * 70}\n')

main()




