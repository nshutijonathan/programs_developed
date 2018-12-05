class Person():
    def __init__(self,fname,lname,email,age):
        self.fname=fname
        self.lname=lname
        self.email=email
        self.age=age
Person.fname=input("please enter your first name")
Person.lname=input("please enter your last name")
Person.email=input("please enter your email")
Person.age=input("please enter your age")
p1=Person(Person.fname,Person.lname,Person.email,Person.age)
print(p1.fname)
print(p1.lname)
print(p1.email)
print(p1.age)
        
