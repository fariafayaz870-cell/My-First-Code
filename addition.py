(</>)Python
#Addition
a=2
b=4
print(a+b)
#subtraction
a=6
b=5
print(a-b)
#division
a=8
b=2
print(a/b)
#multiplication
a=7
b=4
print(a*b)
#area of rectangle
length=20
breadth=4
area=(length*breadth)
print(area)
#height of a person
name="fiza"
height=170
print(name)
print(height)
#brand and colour of bag
brand="puma"
colour="black"
print=(brand,colour)
#salary of a person
name="raj"
month="april"
salary=20000
print(name,month,salary)
#simple intrest
principal=1000
rate=5
time=2
si=principal*rate*time
print(si)
#circumfrence of a circle
radius=20
circumfrence=2*3.14*radius
print(radius,circumfrence)
#equal to
a=5
b=5
print(a==b)
#name of a person
name=input("what is your name?")
print(name)
#integers
a=int(input("the first number is"))
b=int(input("the second number is"))
sum=a+b
print("the sum is",sum)
#equal to
a=3
b=5
if(a==b):
  print("a is equal to b")
else:
  print("a is not equal to b")
#aprox value
a=30
b=40
s=a//b
print(s)
#percentage
a=9
b=6
r=a%b
print(r)
#remainder
a=5
power=a**3
print(power)
matrix=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(matrix[1][1])
# list
number=[10,20,30,40,50]
total_sum=sum(number)
print(total_sum)
avg=total_sum/len(number)
print(avg)
#number list
number=[10,20,30,40,50]
print(number)
print(number[-1])
print(number[1])
print(number[-2])
number.append(60)
print("after append",number)
number.extend([70,80,90])
print("after extend",number)
number.pop()
print("after pop",number)
number.pop(2)
print("after pop",number)
del number[0]
print("after number[0]",number)
number.clear()
print("cleared list",number)
#-ive numbers
num= int(input("enter a number:"))
factorial =1
if num < 0:
  print("factorial is does not exist for negative numbera")
elif num == 0:
  print("factorial is 1")
else:
  for i in range (1,num +1):
    factorial = factorial*i
    print("factorial of", num,"is", factorial)
    #sum
a=int(input("enter the number"))
b=int(input("enter the number"))
sum=a+b
print(sum)
#def
print("hello python")
#test2()

def  test2():
    a=int(input("enter the first number"))
    b=int(input("enter the 2nd number"))
    sum=a+b
    print(sum)

test2()
#tuple & list
tu=("a","b","c")
print(type(tu))
#tu.append("d")
print(tu)
tu_li=list(tu)
print(type(tu_li))
tu_li.append("d")
print(tu_li)
# dictionary (key, values & items)
dog = {
  "colour":"brown",
  "breed":"labrador",
  "gender":"male"
}
for key, value in dog.items():
  print(key,"=" , value)
bag = {
  "colour":"blue",
  "brand":"puma"
}
for key, value in bag.items():
  print(key,"=" , value)
girls = {
  "personality":"awesome",
  "brain":"well developed",
  "emotions": "regulated"  
}
key = "brain"
print(key, "=" , girls [key])
district = {
  "location":"anatnag",
  "area":"rural"
}
key = "location"
print(key,"=", district [key])
district["time"]="12pm"
print(district)
for key,value in district.items():
  print(key,"=",value)
  key="area"
  print("for given key",key,"=",district[key])
  district["area"]="urban"
  print(district)
  for key,value in district.items():
    if value =="urban":
      print(key,"=",value)
      district.update({"location":"hazratbal","tehsil":"noth"})
      print(district)
     # frozenset (subset $supset), unions
s={1,2,3,4,5}
print(s)
print(type(type(s)))
s.add(5)
print(s)
s.remove(4)
print(s)
li=["a","b","c","d",]
print(li)
print(type(li))
li_s=set(li)
print(li_s)
print("li_set",type(li_s))
fs=frozenset(["f","r", "o"])
print(type(fs))
print(fs)

print(fs)
u=s.union(fs)
print("union",u)
print("union|",s|fs)
print("sort",sorted(li_s))
if fs<=u:
   print("fs is subset")  
if u>=fs:
   print("u is supset")  
print(u)
a={11,12,13,14}
b={10,20,30,40}
print("a-",a-b)
print("b-",b-a)
# make 2 diff files like python.py,dyd.py,firstfile.txt then write this code on dyd.py
try:
  f=open("LB/firstfilee.txt")
except FileNotFoundError:
  print("File found")
finally:
  print("program executed")
  


      
      


      
      


























  

  










         















      



















