# Function with Parameters
def greet(name):  #name :- parameter
    print("Hello", name)

greet("Deepak") #Deepak :- arguments
greet("Rahul")
greet("Amit")


# Function with Multiple Parameters
def addition(a, b):
    result = a + b
    print("Addition:", result)

addition(10, 20)
addition(50, 30)



def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student("Deepak", 25, "Python")

# --------------------------------------------------------------------------------------------------

# Return keyword:
def addition(a, b):
    print(a + b)  # ye 30 print krega 

result = addition(10, 20)

print(result) # ye none aayega qki result me koi bhi value nhi aayi h,,result me value lane ke liye hme return keyword likhna prega.

def addition(a, b):
    return a + b

result = addition(10, 20)

print(result + 50)