no=[10,20]
no1=[]
print("No : ",no)
print(type(no))
no1.append(20)
no1.append(200)
no1.append(100)
no1.append(200)
print("No1 : ",no1)
x=no1.copy()
print("X : ",x)
x.clear()
print("After Clear X : ",x)
print("200 is present in no1 ",no1.count(200)," times")
no1.extend(no)
print("After (no1+no) No1 : ",no1)
print("No : ",no)
print("index position of 200 in no1 ",no1.index(200))
no1.insert(2,2000)
print("After Insert 2000 No1 : ",no1)
print("pop in no1 :- ",no1.pop())

print("No1 : ",no1)
no1.remove(200)
print("remove 200 in No1 : ",no1)
no1.reverse()

print("After Revers No1 : ",no1)
no1.sort()

print("Sorting No1 : ",no1)
no1.reverse()

print("Desc. Sorting No1 : ",no1)
