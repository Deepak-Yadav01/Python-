# Types of Function Arguments

# 1. Positional Arguments
def student(name, age):
    print(name)
    print(age)

student("Deepak", 25)   # note:  yha Order change krne pe  output bhi bdl jayega

# 2. Keyword Arguments
def student(name, age):
    print(name)
    print(age)

student(age=25, name="Deepak") # यहाँ position बदलने पर भी सही output मिलेगा।

# 3. Default Arguments
def greet(name="Guest"):
    print("Welcome", name)

greet()
greet("Deepak")

# 4. Variable-Length Arguments
# जब हमें पहले से पता नहीं होता कि कितने arguments pass होंगे।  2 types

# A. *args    ---- Multiple positional arguments accept krta h.
def addition(*numbers):

    total = 0

    for num in numbers:
        total += num

    return total

print(addition(10, 20))
print(addition(10, 20, 30))
print(addition(10, 20, 30, 40))
# यहाँ *numbers सभी positional arguments को एक tuple में collect करता है।


# B. **kwargs
# Multiple keyword arguments accept करता है।
def student(**details):

    for key, value in details.items():
        print(key, ":", value)

student(name="Deepak", age=25, course="Python")
# यहाँ **details सभी keyword arguments को dictionary में collect करता है।