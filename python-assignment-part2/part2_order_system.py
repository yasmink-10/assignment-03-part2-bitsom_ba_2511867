# Task 1 — Explore the Menu

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# 1. Menu grouped by category

categories = ["Starters", "Mains", "Desserts"]

for ctg in categories:
    print(f"\n===== {ctg} =====")

    for item in menu:
        if menu[item]["category"] == ctg:
            price = menu[item]["price"]
            available = menu[item]["available"]

            if available:
                status = "Available"
            else:
                status = "Unavailable"
            print(f"{item:<15} ₹{price:.2f} [{status}]")

# Total items
total_items = len(menu)

# Available items
available_count = 0

# Most expensive item
max_price = 0
max_item = ""

# Items under 150
budget_items = []

for item in menu:
    price = menu[item]["price"]
    available = menu[item]["available"]

    # count available
    if available:
        available_count += 1

    # most expensive
    if price > max_price:
        max_price = price
        max_item = item
    
    # items under 150
    if price < 150:
        budget_items.append((item, price))

print("\nTotal items:", total_items)
print("Available items:", available_count)

print("Most expensive item:", max_item, "-", max_price)

print("\nItems under ₹150:")
for item, price in budget_items:
    print(item, "-", price)

print("\n")

#Task 2 — Cart Operations

cart = []

# Add item
def add_item(name, qty):
    # check if item exists
    if name not in menu:
         print(name, "not found in menu")
         return
    # check availablitity
    if not menu[name]["available"]:
        print(name, "is unavailable")
        return
    price = menu[name]["price"]
    # if already in cart
    for item in cart:
        if item["item"] == name:
            item["quantity"] += qty
            print(name, "quantity updated")
            return
    # add item
    cart.append({"item": name, "quantity": qty, "price": price})
    print(name, "added to cart")

# Remove item
def remove_item(name):
    for item in cart:
        if item["item"] == name:
            cart.remove(item)
            print(name, "removed from cart")
            return
    print(name, "not in cart")

# Print cart
def show_cart():
    print("\nCurrent Cart:")
    for item in cart:
        print(item)
    print()

# Simulation

add_item("Paneer Tikka", 2)
show_cart()

add_item("Gulab Jamun", 1)
show_cart()

add_item("Paneer Tikka", 1)
show_cart()

add_item("Mystery Burger", 1)
show_cart()

add_item("Chicken Wings", 1)
show_cart()

remove_item("Gulab Jamun")
show_cart()

# Final order
print("========== Order Summary ==========")
subtotal = 0

for item in cart:
    total_price = item["quantity"] * item["price"]
    subtotal += total_price

    print(f"{item['item']:<18} x{item['quantity']}   ₹{total_price:.2f}")

print("------------------------------------")

gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal:                ₹{subtotal:.2f}")
print(f"GST (5%):                ₹{gst:.2f}")
print(f"Total Payable:           ₹{total:.2f}")
print("====================================")

#Task 3 — Inventory Tracker with Deep Copy

import copy

# 1. Deep Copy
inventory_backup = copy.deepcopy(inventory)

# Value to test
inventory["Paneer Tikka"]["stock"] = 5

print("Modified Inventory:")
print(inventory["Paneer Tikka"])

print("\nBackup Inventory (should be unchanged):")
print(inventory_backup["Paneer Tikka"])

inventory = copy.deepcopy(inventory_backup)

# 2. Deduct stock
print("\nUpdating inventory from cart...")

for item in cart:
    name = item["item"]
    qty = item["quantity"]

    stock = inventory[name]["stock"]

    if stock >= qty:
        inventory[name]["stock"] -= qty
    else:
        print(f"Warning: Only {stock} {name} available!")
        inventory[name]["stock"] = 0

# 3. Reorder alert
print("\nReorder Alerts:")

for name in inventory:
    stock = inventory[name]["stock"]
    reorder = inventory[name]["reorder_level"]

    if stock <= reorder:
        print(f"⚠ Reorder Alert: {name} - Only {stock} unit(s) left (reorder level: {reorder})")

# 4. Final check
print("\nFinal Inventory (changed):")
print(inventory)

print("\nBackup Inventory (original):")
print(inventory_backup)

# Task 4 - Daily Sales Log Analysis

# 1. Revenue / day
print("Revenue per day:")

daily_rev = {}

for date in sales_log:
    total = 0

    for order in sales_log[date]:
        total += order["total"]

    daily_rev[date] = total
    print(date, ":", total)

# 2. Best-selling day
best_day = ""
max_rev = 0

for date in daily_rev:
    if daily_rev[date] > max_rev:
        max_rev = daily_rev[date]
        best_day = date

print("\nBest-selling day:", best_day, "-", max_rev)

# 3. most ordered
item_count = {}

for date in sales_log:
    for order in sales_log[date]:
        for item in order["items"]:

            if item in item_count:
                item_count[item] += 1
            else: 
                item_count[item] = 1
most_item = ""
max_count = 0

for item in item_count:
    if item_count[item] > max_count:
        max_count = item_count[item]
        most_item = item

print("\nMost ordered item:", most_item, "-", max_count, "times")

# 4. new day

sales_log["2025-01-05"]= [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

print("\nUpdated Revenue per day: ")

daily_rev = {}
for date in sales_log:
    total = 0
    for order in sales_log[date]:
        total += order["total"]
    daily_rev[date] = total
    print(date, ":", total)

best_day = ""
max_rev = 0

for date in daily_rev:
    if daily_rev[date] > max_rev:
        max_rev = daily_rev[date]
        best_day = date

print("\nUpdated Best selling day:", best_day, "-", max_rev)

# 5. Numbered order
print("\nAll Orders: ")
all_orders = []

for date in sales_log:
    for order in sales_log[date]:
        all_orders.append((date, order))

for i, data in enumerate(all_orders, start=1):
    date = data[0]
    order = data[1]

    items = ", ".join(order["items"])
    print(f"{i}. [{date}] order #{order['order_id']} - ₹{order['total']} - Items: {items}")