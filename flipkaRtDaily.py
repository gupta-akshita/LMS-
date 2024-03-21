from enum import Enum

class PricingOption(Enum):
    FLAT_DISCOUNT = 1
    PERCENTAGE_INCREASE = 2

class Item:
    def __init__(self, category: str, brand: str, mrp: float, price: float):
        self.category = category
        self.brand = brand
        self.mrp = mrp
        self.price = price

class InventoryItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

class User:
    def __init__(self, name, email, wallet_amount):
        self.name = name
        self.email = email
        self.wallet_amount = wallet_amount
        self.cart = {}

class Inventory:
    def __init__(self, system):
        self.inventory = {}
        self.system = system

    def add_inventory(self, category, brand, quantity):
        if quantity <= 0:
            print("Error: Quantity must be a positive integer.")
            return
        
        if category not in self.inventory or brand not in self.inventory.get(category, {}):
            print(f"New brand {brand} and category {category} detected.")
            # Ask for MRP and price since it's a new item
            try:
                mrp = float(input("Enter MRP for the new item: "))
                price = float(input("Enter price for the new item: "))
                if mrp <= 0 or price <= 0:
                    print("Error: Invalid MRP or price.")
                    return
                self.system.add_item(category, brand, mrp, price)
            except ValueError:
                print("Error: Please enter a valid number for MRP and price.")
                return
        
        if category not in self.inventory:
            self.inventory[category] = {}
        if brand not in self.inventory[category]:
            self.inventory[category][brand] = 0
        
        self.inventory[category][brand] += quantity
        print(f"Inventory updated: Category - {category}, Brand - {brand}, Quantity added - {quantity}")

    def update_inventory(self, category, brand, quantity):
        if category in self.inventory and brand in self.inventory[category]:
            self.inventory[category][brand] += quantity
            print(f"Inventory updated: Category - {category}, Brand - {brand}, Quantity updated - {quantity}")
        else:
            print(f"Error: Inventory item not found - Category: {category}, Brand: {brand}")

    def search_inventory(self, filters):
        results = []
        for category, brands in self.inventory.items():
            for brand, quantity in brands.items():
                if all(filter_func(category, brand, quantity) for filter_func in filters):
                    results.append((category, brand, quantity))
        return results
    
    def show_inventory(self):
        print("Curent Inventory Details :")
        if not self.inventory:
            print("The inventory is currently empty.")
            return
        
        for category, brands in self.inventory.items():
            print(f"Category: {category}")
            for brand, quantity in brands.items():
                print(f"  Brand: {brand}, Quantity: {quantity}")
            print("")  # Extra newline for better readability

class ShoppingCart:
    def __init__(self):
        self.carts = {}

    def add_to_cart(self, user, item, brand, quantity):
        if quantity <= 0:
            print("Error: Quantity must be a positive integer.")
            return
        if user not in self.carts:
            self.carts[user] = {}
        if brand not in self.carts[user]:
            self.carts[user][brand] = {}
        if item not in self.carts[user][brand]:
            self.carts[user][brand][item] = 0
           
        self.carts[user][brand][item] += quantity
        print(f"Item added to cart: User - {user.name}, Brand - {brand}, Item - {item}, Quantity - {quantity}")
        print()

    def remove_from_cart(self, user, item, brand, quantity):
        if quantity <= 0:
            print("Error: Quantity must be a positive integer.")
            return
        if user in self.carts and brand in self.carts[user] and item in self.carts[user][brand]:
            self.carts[user][brand][item] -= quantity
            if self.carts[user][brand][item] <= 0:
                del self.carts[user][brand][item]
                if not self.carts[user][brand]:
                    del self.carts[user][brand]
                    if not self.carts[user]:
                        del self.carts[user]
            print(f"Item removed from cart: User - {user.name}, Brand - {brand}, Item - {item}, Quantity - {quantity}")
        else:
            print(f"Error: Item not found in cart - User: {user.name}, Brand: {brand}, Item: {item}")

    def get_cart_info(self, user):

        if user in self.carts:
            return self.carts[user]
        else:
            print(f"Error: Cart not found for user - {user.name}")
            return {}

class FlipkartGrocerySystem:
    def __init__(self):
        self.items = []
        self.inventory = Inventory(self)
        self.shopping_cart = ShoppingCart()

    def add_item(self, brand, category, mrp, price):
        if mrp <= 0 or price <= 0:
            print("Error: MRP and price must be positive numbers.")
            return
        
        existing_item = next((item for item in self.items if item.brand == brand and item.category == category), None)
        if existing_item:
            # Ask the user if they want to update the price
            user_choice = input(f"Item with Brand - {brand} and Category - {category} already exists. Do you want to update the price? (yes/no): ").strip().lower()
            if user_choice == "yes" or user_choice == "y":
                existing_item.price = price
                existing_item.mrp = mrp
                print(f"Price updated for Brand - {brand}, Category - {category}. New Price - {price} with MRP - {mrp}")
            else:
                new_category_name = input("Enter a new category name to add this item as a new category: ").strip()
                if new_category_name:
                    self.items.append(Item(new_category_name, brand, mrp, price))
                    print(f"New category '{new_category_name}' added with item: Brand - {brand}, MRP - {mrp}, Price - {price}")
                else:
                    print("Operation cancelled. Item was not added or updated.")
        else:
            self.items.append(Item(category, brand, mrp, price))
            print("Items added successfully in an Inventory!")
            # self.update_inventory(category, brand, 0)

    def update_item(self, category, brand, price):
        for item in self.items:
            if item.category == category and item.brand == brand:
                if price <= 0:
                    print("Error: Price must be a positive number.")
                    return
                if price > item.mrp:
                    print("Error: Price can not be greater than MRP.")
                    return 
                item.price = price
                print(f"Item price updated: Category - {category}, Brand - {brand}, New price - {price}")
                return
        print(f"Error: Item not found - Category: {category}, Brand: {brand}")

    def add_user(self, name, email, wallet_amount):
        if wallet_amount <= 0:
            print("Error: Wallet amount must be a positive number.")
            return None
        user = User(name, email, wallet_amount)
        print(f"User added successfully: Name - {name}, Email - {email}, Wallet Amount - {wallet_amount}")
        return user

    def update_items(self, category, brand, pricing_option):
        for item in self.items:
            if item.category == category and item.brand == brand:
                if pricing_option == PricingOption.FLAT_DISCOUNT:
                    item.price -= item.price * 0.1
                    print(f"Item price updated with flat discount: Category - {category}, Brand - {brand}, New price - {item.price}")
                elif pricing_option == PricingOption.PERCENTAGE_INCREASE:
                    item.price += item.price * 0.1
                    print(f"Item price updated with percentage increase: Category - {category}, Brand - {brand}, New price - {item.price}")
                return
        print(f"Error: Item not found - Category: {category}, Brand: {brand}")

    def search_items(self, filters):
        return self.inventory.search_inventory(filters)

    def show_added_items(self):
        print("Added items : ")
        for item in self.items:
            print(f"Category - {item.category}, Brand - {item.brand}, MRP - {item.mrp}, Price - {item.price}")

    def execute_commands(self):
        # Example usage of methods
        self.add_item("Amul", "Milk", 120, 100)
        self.add_item("Amul", "Curd", 60, 50)
        self.add_item("Nestle", "Milk", 70, 60)
        self.add_item("Nestle", "Curd", 100, 90)
        self.show_added_items()
        
        self.add_item("Nestle", "Curd", 120, 100)

        print(" Show Items --------- ")
        self.show_added_items()
        # print("Add inventory ***********")

        self.inventory.add_inventory("Amul", "Milk", 10)
        # self.inventory.add_inventory("Nestle", "Milk", 5)
        # self.inventory.add_inventory("Nestle", "Curd", 10)
        # self.inventory.add_inventory("Nestle", "Milk", 30)
        # self.inventory.add_inventory("Amul", "Curd", 5)

        print(" Show inventory ----------- ")
        self.inventory.show_inventory()
        # self.inventory.add_inventory("MDH", "Red Chilli", 5)
        # self.inventory.show_inventory()

        print("Add new users *********")

        user1 = self.add_user("Jhonny", "jhonny@gmail.com", 600)
        user2 = self.add_user("Naruto", "naruto@gmail.com", 500)
        user3 = self.add_user("Goku", "goku@gmail.com", 3000)

        print()

        self.shopping_cart.add_to_cart(user1, "Milk", "Nestle", 40)
        self.shopping_cart.add_to_cart(user2, "Milk", "Nestle", 12)
        
        self.show_added_items()
        # self.update_item("Milk", "Amul", 60)
        # self.show_added_items()

        self.shopping_cart.add_to_cart(user3, "Milk", "Nestle", 10)
        
        print("Update items")

        # print(self.shopping_cart.get_cart_info(user3))
        # print()
        # print(self.shopping_cart.get_cart_info(user1))
        # print()
        # print(self.shopping_cart.get_cart_info(user2))
        # print()

        self.update_items("Nestle", "Curd", PricingOption.FLAT_DISCOUNT)
        print("------------------")
        
        print(self.search_items([lambda category, brand, quantity: category == "Nestle"]))
        print()
        print(self.search_items([lambda category, brand, quantity: category in ["Nestle", "Amul"]]))
        print()

        self.show_added_items()

if __name__ == "__main__":
    system = FlipkartGrocerySystem()
    system.execute_commands()


    # client interaction   --> 

    # strategy 

    # decouple 

