# a dictionary (dict) stores data as key–value pairs.
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

print(student)

# Access a value
print(student["name"])      # John

# Safe access
print(student.get("age"))   # 20

# Add a new key-value pair
student["city"] = "London"
print(student)

# Change a value
student["age"] = 21

# Remove an item
del student["city"]
print(student)


# Loop through a dictionary
for key in student:
    print(key, student[key])

# ya

for key, value in student.items():
    print(key, value)
    