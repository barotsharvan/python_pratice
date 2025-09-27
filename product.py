pcode=int(input("enter the product code:"))
pname=(input("enter the product Name:"))
pr=int(input("enter the product price:"))
qty=int(input("enter the product quantity:"))

amo=pr*qty
disc=amo*40/100
tax=amo*10/100
tamo=amo-disc+tax

print ("Product code:",pcode)
print ("product name ",pname)
print("product price",pr)
print ("produc quantity",qty)
print ("Amount",amo)
print ("Discount",disc)
print ("Tax",tax)
print ("Total amount",tamo)


