#difine the menu of cafe
menu = {
    'pizza':100,
    'pasta':90,
    'noodles':120,
    'Burger': 60,
    'sandwich':40,
    'coffee':40,
    'milkshake':50,
    }
#print(menu)

#Greet
print("welcome to python cafe")
print("pizza: Rs100\npasta: Rs90\nnoodles : RS120\nBurger: Rs60\nsandwich : Rs40\ncoffee : Rs40\nmilkshake :Rs50")


order_total = 0
#60 + 40 = 100

item_1 = input("enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 50
    print(f"your item {item_1} has been added to your order")

else:
    print(f"ordered item {item_1} is not available yet")

another_order = input("do you want to Add another item? (YES/NO) ")
if another_order == "YES":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
            print(f"ordered item {item_2} is not available")

print(f"the total amount of items to pay is {order_total}")
