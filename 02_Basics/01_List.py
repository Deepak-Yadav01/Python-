# List Python ka ek collection/data structure hai jisme hum multiple values ko ek hi variable mein store kar sakte hain.
fruits = ["Apple", "Mango", "Banana", "Orange"]
print(fruits)

print(fruits[0])   # Apple
print(fruits[1])   # Mango
print(fruits[2])   # Banana
print(fruits[-1])  # Orange
print(fruits[-2])  # Banana

# Python list mutable hoti hai, yani value change kar sakte hain.
fruits = ["Apple", "Mango", "Banana"]

fruits[1] = "Grapes"
print(fruits)

# append() — last mein value add
fruits = ["Apple", "Mango"]
fruits.append("Banana")
print(fruits)

# insert() — specific position par add
fruits = ["Apple", "Banana"]
fruits.insert(1, "Mango")
print(fruits)

# remove() — value delete
fruits = ["Apple", "Mango", "Banana"]
fruits.remove("Mango")
print(fruits)

# pop() — index se delete
fruits = ["Apple", "Mango", "Banana"]
fruits.pop(1)
print(fruits)
# Agar index nahi doge: to last element remove hoga.
fruits = ["Apple", "Mango", "Banana"]
fruits.pop()
print(fruits)

# len() — list ki length
numbers = [10, 20, 30, 40, 50]
print(len(numbers))

# Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]
for fruit in fruits:
    print(fruit)
    print(fruit, end="-")

if "Guava" in fruits:
    print(f"I Have Guava in fruits baskets")

fruits.append("Guava")
print(fruits)

if "Guava" in fruits:
    print(f"I Have Guava in fruits baskets")
