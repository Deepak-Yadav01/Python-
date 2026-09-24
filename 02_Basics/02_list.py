
fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]

fruits2 = fruits.copy()

print(fruits)
print(fruits2)

fruits2.append("Pineapple")

print(fruits)
print(fruits2)

fruits2.reverse() #Important
print(fruits2)

fruits.sort()  # Important,, ye strings ko alphabetical order (A → Z) mein arrange karta hai.
print(fruits)

numbers = [50, 10, 40, 20, 30]
numbers.sort()                    # hmesa Asscending order me krta h
print(numbers)

# decending order ke liye
numbers.sort(reverse=True)
print(numbers)

# clear() — Puri list empty karna
fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]

fruits.clear()
print(fruits)