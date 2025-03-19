# Restaurant Menu Ordering System

# Dictionary for the restaurant menu items and their prices.
menu = {
    'Dosa': 180.00,
    'Pongal': 150.00,
    'Idly': 25.00,
    'Dal Roti': 120.00,
    'Idiyappam': 100.00,
    'Medhu Vadai': 20.00
}
# :.2f will format the value of price to show exactly two decimal places.
def show_menu():
    print("\n!! Welcome to the Lucky Restaurant !!")
    print("\nHere is our menu:")
    for item, price in menu.items():
        print(f"{item}: ₹{price:.2f}")

def place_order():
    order = {}
    while True:
        item = input("\nEnter the item you want to order (or type 'none' if no more'): ").title()
        if item.title() == "None":
            break
        elif item in menu:
            quantity = int(input(f"How many {item}s would you like to order? "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
            print(f"{quantity} {item}(s) added to your order")
        else:
            print("Sorry, we don't have that item on the menu.")
    return order

def total_bill(order):
    total = 0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total

def main():
    show_menu()
    order = place_order()
    
    if order:
        print("\nYour order summary:")
        for item, quantity in order.items():
            print(f"{item}: {quantity} x ₹{menu[item]:.2f} = ₹{menu[item] * quantity:.2f}")
        
        total = total_bill(order)
        print(f"\nThank you for your order! Your total bill is: ₹{total:.2f}")
    else:
        print("No items were ordered.")
    
    print("\nWe hope to see you again soon!")

if __name__ == "__main__":
    main()



