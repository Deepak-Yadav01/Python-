# Python में input() का use user से keyboard के through data लेने के लिए किया जाता hai.
name = input("Enter your name: ")
print("Hello", name)

# Important: input() हमेशा String देता है
age = input("Enter your age: ")

print(age)
print(type(age))

# Integer input
age = int(input("Enter your age: "))

print(age)
print(type(age))

# Float input
price = float(input("Enter price: "))

print(price)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)