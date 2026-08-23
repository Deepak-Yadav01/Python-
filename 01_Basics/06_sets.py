numbers = {10, 20, 30, 40}
print(numbers)

# Set में order fixed नहीं होता
names = {"Rahul", "Amit", "Deepak", "Ravi"}
print(names)


a = {} # यह empty set नहीं, बल्कि empty dictionary है।

#  empty set banane ke liye 
a = set()
print(a)

# to convert list into set
numbers = [10, 20, 10, 30, 20, 40]
unique_numbers = set(numbers)
print(unique_numbers)

# important methods of sets
numbers = {10, 20, 30}
numbers.add(40) # add()
print(numbers) # {40, 10, 20, 30}

numbers.remove(30)  # agr element available nhi hoga to error dega
print(numbers) # {40, 10, 20}

numbers.discard(50)
print(numbers) # koi error nhi dega

numbers = {10, 20, 30, 40}
numbers.pop()
print(numbers)


numbers.clear()  # agr pure set ko empty krna ho
print(numbers)

#----------------------------------------------------------------------------------------
# sets Operations

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 1. Union |    ,, unique elements deta h
print(A | B)  # {1, 2, 3, 4, 5, 6}

# 2. Intersection & ,,, dono me common 
print(A & B) # {3, 4}

# 3. Difference -  
print(A - B) # {1, 2}  ,, A me h lekin B me nhi
print(B - A) # {5, 6}  ,, B me h lekin A me nhi

# 4. Symmetric Difference ^   ,, जो elements केवल A या केवल B में हैं, लेकिन दोनों में common नहीं:
print(A ^ B)  # {1, 2, 5, 6}

# 5. isdisjoint()  ,, Check करता है कि दोनों sets में कोई common element है या नहीं।

A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B)) # agr common element nhi hoga to true

A = {1, 2, 3}
B = {3, 4, 5}

print(A.isdisjoint(B)) # agr common element hoga to false

# 6. issubset()  ,, Check करता है कि एक Set दूसरे Set के अंदर पूरी तरह मौजूद है या नहीं।
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B)) # true

# 7. issuperset()  ,, Check करता है कि पहला Set दूसरे Set के सभी elements रखता है या नहीं।
A = {1, 2, 3, 4}
B = {1, 2}

print(A.issuperset(B)) # true

