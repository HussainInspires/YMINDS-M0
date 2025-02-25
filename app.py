import json

# File to store inventory data
FILENAME = "inventory.json"

# Load inventory from file
def load_inventory():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save inventory to file
def save_inventory(inventory):
    with open(FILENAME, "w") as file:
        json.dump(inventory, file, indent=4)

# Add a new item
def add_item(inventory):
    item_id = input("Enter item ID: ")
    if item_id in inventory:
        print("Item already exists!")
        return

    name = input("Enter item name: ")
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
    except ValueError:
        print("Invalid input! Quantity must be a number, and price must be a decimal.")
        return

    inventory[item_id] = {"name": name, "quantity": quantity, "price": price}
    print("Item added successfully!")
    save_inventory(inventory)

# Update an existing item
def update_item(inventory):
    item_id = input("Enter item ID to update: ")
    if item_id not in inventory:
        print("Item not found!")
        return

    try:
        quantity = int(input("Enter new quantity: "))
        price = float(input("Enter new price: "))
    except ValueError:
        print("Invalid input!")
        return

    inventory[item_id]["quantity"] = quantity
    inventory[item_id]["price"] = price
    print("Item updated successfully!")
    save_inventory(inventory)

# View all items
def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty!")
    else:
        print("\nInventory List:")
        for item_id, item in inventory.items():
            print(f"ID: {item_id}, Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")

# Search for an item
def search_item(inventory):
    search_term = input("Enter item name or ID to search: ").lower()
    found = False

    for item_id, item in inventory.items():
        if search_term in item_id.lower() or search_term in item["name"].lower():
            print(f"ID: {item_id}, Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")
            found = True

    if not found:
        print("Item not found!")

# Main function
def main():
    inventory = load_inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Search Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            update_item(inventory)
        elif choice == "3":
            view_inventory(inventory)
        elif choice == "4":
            search_item(inventory)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if _name_ == "_main_":
    main()