item = "Notebook"
quantity = 5
price = 20.0

bill = "Item: {item}\nQuantity: {qty}\nPrice per item: ₹{price:.2f}\nTotal: ₹{total:.2f}".format(
    item=item,
    qty=quantity,
    price=price,
    total=quantity * price
)

print("--- Bill ---")
print(bill)
