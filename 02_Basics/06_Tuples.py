# a tuple is an ordered collection of values. It’s similar to a list, but a tuple is immutable, meaning you cannot change its elements after creation.
numbers = (10, 20, 30)
print(numbers)              # (10, 20, 30)

person = ("John", 25, True)  # Tuples can contain different data types:

# For a single-element tuple, the comma is required:
x = (5,)   # tuple
print(type(x))
y = (5)    # integer
print(type(y))


fruits = ("apple", "banana", "mango")

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # mango

numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])  # (20, 30, 40)
print(numbers)   # (10, 20, 30, 40, 50)


# numbers = (10, 20, 30)
# numbers[0] = 100       # # TypeError,,, qki  tuples immutable hoti h.


# Tuple unpacking
# Python lets you assign tuple elements to multiple variables:

person = ("Alice", 22, "London")

name, age, city = person

print(name)  # Alice
print(age)   # 22
print(city)  # London

# A common example is swapping variables:
a = 10
b = 20

a, b = b, a

print(a)  # 20
print(b)  # 10