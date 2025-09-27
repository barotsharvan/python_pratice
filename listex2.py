no=[]
n=int(input("How many no u want"))
for i in range(n):
    data=input("Enter value")
    no.append(data)


print(no)
po=int(input("Which pos. u w to enter data "))
data=input("New data ")
no.insert(po-1,data)
print("After insert : ",no)


po=int(input("Which pos data u w to show "))
print(no[po-1])
data=input("Which data u want to remove")
no.remove(data)
print("After Delete : ",no)
