#Q21
Products = {
    'pid1': {'Name': 'Shoes', 'Price': 1200},
    'pid2': {'Name': 'Backpack', 'Price': 1500}
}

cart = {}
cart_id = 1
total_bill = 0

for pid, details in Products.items():
    print(f"Product ID: {pid}")
    print(f"Name: {details['Name']}")
    print(f"Price: {details['Price']}")
    choice = input("Do you want to add this product to cart? (yes/no): ").lower()
    
    if choice == 'yes':
        qty = int(input("Enter quantity: "))
        item_amount = details['Price'] * qty
        cart_key = f"cart{cart_id}"
        cart[cart_key] = {
            'prodid': pid,
            'Name': details['Name'],
            'Price': details['Price'],
            'Quantity': qty,
            'ItemAmount': item_amount
        }

        total_bill += item_amount
        cart_id += 1
    print()

print("Invoice:")
for key, item in cart.items():
    print(f"Cart ID: {key}")
    print(f"Product ID: {item['prodid']}")
    print(f"Name: {item['Name']}")
    print(f"Price: {item['Price']}")
    print(f"Quantity: {item['Quantity']}")
    print(f"Item Amount: {item['ItemAmount']}")
    print()

print(f"Total Amount to Pay: {total_bill}")
