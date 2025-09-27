no1=list((10,20,30,40))
print(no1)
print(type(no1),'   Size      ',len(no1))

a=tuple((100,200,300,100))
print(a,'    ',type(a))

b=tuple(no1)
print(b,'    ',type(b),'       Size  ',len(b))
c=(10,20,30,40)
print(c)
print("100 is how many times present",a.count(100))
print("100 is position ",a.index(100))
