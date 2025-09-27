class Info:
    def setdata(self):
        self.sno=int(input("Enter S.no"))
        self.na=input("Enter Name")
        self.age=int(input("Enter Age"))
    def show(self):
        print('S.no:',self.sno)
        print('Name:',self.na)
        print('Age:',self.age)
x=Info()
x.setdata()
x.show()
