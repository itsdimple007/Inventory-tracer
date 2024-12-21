inventory = {}

def add_item(item_name, quantity, price_per_unit):
    """
    Add an item to the inventory.
    If the item already exists, update its quantity.
    """
    if item_name in inventory:
        inventory[item_name]['quantity'] += quantity
    else:
        inventory[item_name] = {'quantity': quantity, 'price_per_unit': price_per_unit}
    print(f"{quantity} units of {item_name} added to inventory.")

def remove_item(item_name, quantity):
    """
    Remove a specific quantity of an item from the inventory.
    """
    if item_name in inventory:
        if inventory[item_name]['quantity'] >= quantity:
            inventory[item_name]['quantity'] -= quantity
            print(f"{quantity} units of {item_name} removed from inventory.")
            if inventory[item_name]['quantity'] == 0:
                del inventory[item_name]
                print(f"{item_name} is now out of stock and removed from inventory.")
        else:
            print(f"Insufficient quantity of {item_name} in inventory.")
    else:
        print(f"{item_name} does not exist in the inventory.")

def display_inventory():
    """
    Display the current state of the inventory.
    """
    if inventory:
        print("\nCurrent Inventory:")
        print(f"{'Item Name':<20}{'Quantity':<10}{'Price Per Unit':<15}")
        print("-" * 45)
        for item, details in inventory.items():
            print(f"{item:<20}{details['quantity']:<10}{details['price_per_unit']:<15}")
    else:
        print("\nInventory is empty.")

def calculate_total_value():
    """
    Calculate and display the total value of all items in the inventory.
    """
    total_value = sum(details['quantity'] * details['price_per_unit'] for details in inventory.values())
    print(f"\nTotal value of inventory: ${total_value:.2f}")

# Main menu
def main():
    while True:
        print("\nInventory Tracker")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Inventory")
        print("4. Calculate Total Value")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price_per_unit = float(input("Enter price per unit: "))
            add_item(item_name, quantity, price_per_unit)
        elif choice == '2':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            remove_item(item_name, quantity)
        elif choice == '3':
            display_inventory()
        elif choice == '4':
            calculate_total_value()
        elif choice == '5':
            print("Exiting Inventory Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


    main()