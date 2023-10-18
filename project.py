import sys
import fileinput
from tabulate import tabulate


def main():
    inventory_file = 'Inventory.data'
    while True:
        display_options()
        try:
            user_choice = int(input("Enter the Option number: "))
        except ValueError:
            print("Invalid input. Please enter a valid option number.")
            continue
        choice(user_choice, inventory_file)


def display_options():
    """Display a menu of available options"""
    header = ["Inventory Management System"]
    options = [
        (1, "Add a New Item"),
        (2, "Remove an Item"),
        (3, "Update Item Details"),
        (4, "Search for an Item"),
        (5, "View All Items"),
        (6, "Clear Inventory"),
        (7, "Exit the System")
    ]
    print(tabulate(options, headers=header, tablefmt="pretty"))


def choice(option, inventory_file):
    """Process user's choice"""
    if option == 1:
        header = [["Add to Inventory"]]
        print(tabulate(header, tablefmt="fancy_grid"))
        item_name = input("Enter the item you want to add to the inventory: ")

        while True:
            try:
                item_qty = int(input("Enter the quantity of the item (in units): "))
                print("Item added successfully.")
                break
            except ValueError:
                print("Invalid input. Please enter a valid quantity.")

        add_item(inventory_file, item_name, item_qty)


    elif option == 2:
        header = [["Delete from Inventory"]]
        print(tabulate(header, tablefmt="fancy_grid"))

        item_name = input("Enter the item you want to delete from the inventory: ")
        delete_item(inventory_file, item_name)


    elif option == 3:
        header = [["Update Inventory"]]
        print(tabulate(header, tablefmt="fancy_grid"))

        item_name = input("Enter the item you want to update: ")
        update_item(inventory_file, item_name)


    elif option == 4:
        header = [["Search Inventory"]]
        print(tabulate(header, tablefmt="fancy_grid"))

        item_name = input("Enter the item you want to search: ")
        search_item(inventory_file, item_name)


    elif option == 5:
        header = [["Inventory Overview"]]
        print(tabulate(header, tablefmt="fancy_grid"))

        display_items(inventory_file)


    elif option == 6:
        header = [["Clear Inventory"]]
        print(tabulate(header, tablefmt="fancy_grid"))

        clear_inventory(inventory_file)


    elif option == 7:
        print("You have exited the Inventory Management System.")
        sys.exit()


def add_item(file_path, item_name, item_qty):
    """Add items to the inventory"""
    inv_file = open(file_path, 'a')
    inv_file.write(item_name + '\n')
    inv_file.write(str(item_qty) + '\n')
    inv_file.close()


def delete_item(file_path, item_name):
    """Remove items from the inventory"""
    file = fileinput.input(file_path, inplace=True)

    found = False
    updated_inventory = []

    for line in file:
        if item_name in line:
            found = True
            for i in range(1):
                next(file, None)
        else:
            updated_inventory.append(line.strip('\n'))

    if found:
        print("Item '{}' deleted successfully.".format(item_name))
    else:
        print("Item not found in the inventory.")

    with open(file_path, 'w') as inv_file:
        for item in updated_inventory:
            inv_file.write(item + '\n')


def update_item(file_path, item_name):
    """Update item details in the inventory"""
    with open(file_path, 'r') as f:
        filedata = f.readlines()

    found = False
    for i, line in enumerate(filedata):
        if item_name in line:
            found = True

            while True:
                try:
                    item_qty = int(input("Enter the new quantity: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid quantity.")

            for i, line in enumerate(filedata):
                if item_name in line:
                    filedata[i + 1] = str(item_qty) + '\n'

            with open(file_path, 'w') as f:
                f.writelines(filedata)
            print("Item updated successfully.")
            break

    if not found:
        print("Item not found in the inventory.")


def search_item(file_path, item_name):
    """Search for an item in the inventory"""
    f = open(file_path, 'r')
    search = f.readlines()
    f.close()

    found = False
    search_results = []

    for i, line in enumerate(search):
        if item_name in line:
            found = True
            item = line.strip()
            quantity = search[i + 1].strip()
            search_results.append(["Item", item])
            search_results.append(["Quantity", quantity])

    if found:
        print(tabulate(search_results, tablefmt="fancy_grid"))
    else:
        print("Item not found in the inventory.")


def display_items(file_path):
    """Display all the items in the inventory"""
    inv_file = open(file_path, 'r')
    item_name = inv_file.readline()
    header = ["Items", "Quantity"]
    data = []

    while item_name != '':
        item_qty = inv_file.readline()
        item_name = item_name.rstrip('\n')
        item_qty = item_qty.rstrip('\n')
        data.append([item_name, item_qty])
        item_name = inv_file.readline()

    if data:
        print(tabulate(data, headers=header, tablefmt="fancy_grid"))
    else:
        print("No items found in the inventory.")


def clear_inventory(file_path):
    """Clear all items from the inventory"""
    try:
        with open(file_path, 'w') as inv_file:
            pass
        print("All items have been deleted from the inventory.")
    except Exception as e:
        print("An error occurred while deleting items:", str(e))


if __name__ == "__main__":
    main()
