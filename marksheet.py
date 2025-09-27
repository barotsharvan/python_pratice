rno=int(input("Enter the Rollno"))
na=(input("Enter the Name"))
s1=int(input("Enter the Marks of c"))
s2=int(input("Enter the Marks of c++"))
s3=int(input("Enter the Marks of php"))
tot=s1+s2+s3
per=tot*100/300
if(s1>=35 and s2>=35 and s3>=35 ):
    res='pass'
else:
    res='fail'
if per>=80:
    gr="disc"
elif per>=60:
    gr="first class"
elif per>=50:
    gr="second class"
else:
    gr="pass class"
print("Rollno:",rno)
print("Name:",na)
print("Marks of c:",s1)
print("Marks of c++:",s2)
print("Marks of php:",s3)
print("Total:",tot)
print("Percentage:",per)
print("Result:",res)
if(res=='pass'):
    print ('grade:',gr)
