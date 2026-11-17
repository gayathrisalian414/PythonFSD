'''print("Hello World");

a=23;
b=45;
c=6.77;
d=(2,3,4,"s");
e=[1,2,3,4];
f={"name":"G"};
print(type(a));
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
age=int (input("enter age:"))
if age>=18:
    print("Eligeable")
else:
    print("Not eligeble")'''

'''a=10.0
b=int(a)
print(b)'''

'''def greet():
    print("hello")
greet()

def show():
    return 100
print(show())

def add(a,b):
 print(a+b)
result=add(10,20)'''

'''f=["apple","mango"]
print("mango" in f)
print("mango" not in f)

a={1,2,3,4,5,5}
print(a)

a.add(6)
a.remove(2)
a.discard(7)'''

'''class student:
    def __init__(self,name,age,subject):
        self.name=name
        self.age=age
        self.subject=subject

    def display(self):
        print(f'name:{self.name},age:{self.age},subject:{self.subject}')

    def study(self,subject):
        print(f'{self.name} is studying {subject}')
s1=student("ravi",11,"C")
s2=student("raju",12,"Python")
s1.display()
s1.study()

class Gayathri:
    def display(self):
        print("hi Gayathri Welcome to Python")
s1=Gayathri()
s1.display()

class student:
    def display():
        print("Name:Gayathri")
        print("Age:19")
        print("Course:python")
s1=student.display()

class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def display(self):
        print("name",self.name)
        print("age",self.age)
        print("course",self.course)

s1=student("hello",11,"python")
s2=student("hello",11,"python")
s3=student("hello",11,"python")
s4=student("hello",11,"python")
s1.display()

class Employee:
    def __init__(self,name,salary,experiance):
        self.name=name
        self.salary=salary
        self.experiance=experiance

    def display(self):
        print("name",self.name)
        print("salary",self.salary)
        print("experiance",self.experiance)

s1=Employee("ridhi",1200,"4 yrs")
s2=Employee("hello",11,"python")
s3=Employee("hello",11,"python")
s4=Employee("hello",11,"python")
s1.display()

class bankaccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance +=amount

    def get_balance(self):
        return self.__balance

account=bankaccount(5000)
account.deposit(2000)
print(account.get_balance())

class vehical:
    def start(self):
        print("vehical")

class car(vehical):
    def end(self):
        print("car")

c1=car()

c1.start()
c1.end()

class animal:
    def sound(self):
        print("animal make sound")
class dog(animal):
    def sound(self):
        print("dog barks")
class cat(animal):
    def sound(self):
        print("meow")
d=dog()
c=cat()
d.sound()
c.sound()'''

from abc import ABC,abstractmethod

class payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass
class upi(payment):
    def pay(self,amount):
        print("Paid using upi:",amount)
class card(payment):
    def pay(self,amount):
        print("Paid using card",amount)
u=upi()
c=card()
u.pay(800)
c.pay(100)

