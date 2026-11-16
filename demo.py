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

class student:
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