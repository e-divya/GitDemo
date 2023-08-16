# SYNTAX for Print statement in Python
print("hello")

# Declare variable and Print in Python
a = 5
print(a)

Str = "Hello Python"
print(Str)

b, c, d = 5, 1.12, "Hai"
print(b, c, d)

#Concatenating different data types in Python
print("{} {}".format("Printing integer", b))
print("{} {}".format("Printing decimal", c))
print("{} {}".format("Printing string", d))

#To display what type of datatype is being used by a variable
print(type(b))
print(type(c))
print(type(d))

#List or Array Data Types in Python
values = [1, 2, "hello", 4, 5]
# List is a datatype that allows multiple values with different datatypes
print(values[2]) #hello
print(values[-1]) #-1 prints last value in the list
print(values[2:4]) # ['hello', 4]

#To insert new element in a List
values.insert(3, "Hai")
print(values) #[1, 2, "hello", 'Hai', 4, 5]

#To add new values to the end of a List, use 'append'
values.append("End")
print(values) #[1, 2, 'hello', 'Hai', 4, 5, 'End']

#To update existing values in the List
values[2] = "Hello!" #Updating
print(values) #[1, 2, 'Hello!', 'Hai', 4, 5, 'End']

#Delete existing values in the List
del values[5]
print(values) #[1, 2, 'Hello!', 'Hai', 4, 'End']

# Tuple datatype is same as list but it is immutable (Cannot change the value of parameter)
values = (1, 2, "Hai Tuple")
n = values
print(values[2])

#Dictionary datatype is key-value pair enclosed by flower braces
dic_values = {1: "Hai", 2: 3, "id": 000, "First": "Divya", "Last": "E", "Age": 36}
print(dic_values["Age"]) #36

#Build a new dictionary from an empty dictionary
dict = {}

dict["First"] = "Divya"
dict["Last"] = "Elangovan"
dict["Qualification"] = "B. E. Computer Science"
dict["Age"] = 38
print(dict)

#Conditional Statements:

# IF ELSE CONDITION Syntax in Python:
greeting = "Good Morning"
print("IF ELSE Condition Starts")
if greeting == "Morning":
    print("Condition matches")
else:
    print("Condition fails")
print("IF ELSE Condition Ends")

#Loop Statements:

# FOR Loop Syntax in Python:
obj = [1, 2, 3, 4, 5, 6]
for i in obj:
    print(i)
print("-------------Type multiples of 2------------------")
#Type multiples of 2
obj = [1, 2, 3, 4, 5, 6]
for j in obj:
    j = j * 2
    print(j)
print("-------------Print Sum of First 5 Natural Numbers------------------")
# Print Sum of First 5 Natural Numbers
summation = 0
for k in range(1, 6):
    summation = summation + k
print(summation)

print("-------------To increment an Iteration------------------")
# To increment an Iteration
for o in range(1, 10, 5):
    print(o)

print("-------------Skipping First Index in For loop------------------")
# To increment an Iteration
for p in range(10):
    print(p)

#WHILE Loop in Python
print("-------------WHILE Loop in Python------------------")

it = 4
while it>1:
    print(it)
    it = it-1

print("While loop execution is completed")

print("-------------WHILE Loop in Python with condition------------------")

it = 4
while it>1:
    if(it != 3):
        print(it)
    it = it-1

print("While loop execution is completed")

print("-------------Break Statements in Python with condition------------------")

it = 10
while it>1:
    if(it == 3):
        break
    print(it)
    it = it - 1

print("While loop execution is completed")

print("-------------Continue Statements in Python with condition------------------")

it = 10
while it>1:
    if(it == 9):
        it = it - 1
        continue
    if (it == 3):
        break
    print(it)
    it = it - 1

print("While loop execution is completed")


print("-------------Functions in Python with condition------------------")
def GreetMe(name):
    print("Good Morning " +name+ "!")

GreetMe("Divya")

def AddIntegers(a,b):
    return a+b

print(AddIntegers(5, 6))

print("-------------Object Oriented Principles in Python with condition------------------")
# CLASS - It is a blueprint or Prototype. It has Methods, Variables, Instance Variable, Constructors etc...)
# self keyword is mandatory for calling variable names into method
# instance and class variable have whole different purpose
# constructor name should start and end with double underscore __init__
# new keyword is not required when you create object

class Calculator:
    num = 100 # num is Class variables

    #default constructor
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")
    def input(self):
        print("Executing as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber

    def SummationConst(self):
        return self.firstNumber + self.secondNumber + Calculator.num


#SYNTAX to create object in python
obj = Calculator(2,3) #obj is instance variable
obj.input()
print(obj.Summation())

obj1 = Calculator(4,5) #obj1 is instance variable
obj1.input()
print(obj1.SummationConst())

str ="RahulShettyAcadamey.com"
str1 = "Consulting firm"
str2 = " great "
str3 = " great"
str4 = "great "
searchkey = "RahulShetty"
print(str[1]) #a

print(str[0:5]) #Rahul

print(str+str1) #concatenation

print(searchkey in str)

var = str.split(".")
print(var)
print(var[0])
print(str2.strip())
print(str3.lstrip())
print(str4.rstrip())

print("-------------File Handling in Python with condition------------------")
#Read a file in Python

file = open('test.txt')
#Read by characters
#print(file.read(11))

#Read one single line at a time readLine()
#print(file.readline())
#print(file.readline())

#Line by Line Reading
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()
for line in file.readlines():
    print(line)
file.close()

