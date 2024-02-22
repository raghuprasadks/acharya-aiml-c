def isEvenOrOdd(num):
    if(num%2==0):
        print(num," is even")
    else:
        print(num, " is odd")

#isEvenOrOdd(100)

def shopping(purchase_amt):
    discount=0
    net_amt=0
    rate=0
    if (purchase_amt<=10000):
        rate=.1
    elif (purchase_amt > 10000 and purchase_amt<=20000):
        rate = .2
    else:
        rate = .25
    discount = purchase_amt*rate
    net_amt=purchase_amt-discount
    print("net amount to pay",net_amt)
    print("discount on this bill",discount)

#shopping(10000)
"""
print("list assignment")
num = int(input("enter number of students"))
marks=[]
for i in range(1,num+1):
    print("enter marks for student ",i)
    mark = int(input())
    marks.append(mark)
print("students marks list")
print(marks)
print("loop")
for mark in marks:
    print(mark)
print("marks < 15 and count")
count=0
for mark in marks:
    if (mark<15):
        print(mark)
        count = count+1
print("count of less than 15",count)
marks[4]=25

topeconomies={
    "country":["USA","CHINA","GERMANY","JAPAN","INDIA"],
    "GDP":[27,18,4.7,4.2,4.1],
    "RANK":[1,2,3,4,5]
}
print("topeconomies")
print(topeconomies)
print("data type ",type(topeconomies))
print("keys ",topeconomies.keys())
print("values ",topeconomies.values())
for k,v in topeconomies.items():
    print(k,v)
print("value of country key")
print(topeconomies["country"])

print("class and object")
"""
class Product():
    def __init__(self,code,name,supplier,price):
        self.code = code
        self.name = name
        self.supplier = supplier
        self.price = price
    def info(self):
        print(f" code : {self.code} name : {self.name}")

laptop= Product(1,"hp 11 gen","hp",70000)
laptop.info()
mobile = Product(2,"Samsung 200px ","Samsung",45000)
mobile.info()



