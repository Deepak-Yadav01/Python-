student = {
    "name": "Deepak",
    "age": 24,
    "course": "Python"
}

print(student.keys())             #  dict_keys(['name', 'age', 'course'])
print(student.values())           #  dict_values(['Deepak', 24, 'Python'])  
print(student.items())            #  dict_items([('name', 'Deepak'), ('age', 24), ('course', 'Python')])

# Loop में बहुत useful:
for key, values in student.items():
    print(key, values)


print(student.get("name"))    # Deepak
print(student.get("city"))    # None    ,agr key present nhi ho to None aata h

student.update({"city": "Patna"})
print(student)                     # {'name': 'Deepak', 'age': 24, 'course': 'Python', 'city': 'Patna'}

#Existing key हो तो value update हो जाती है:
student.update({"age": 25})
print(student)             #{'name': 'Deepak', 'age': 25, 'course': 'Python', 'city': 'Patna'}

student.pop("age")
print(student)      #{'name': 'Deepak', 'course': 'Python', 'city': 'Patna'},,, key aur values dono remove hoti h

student.popitem()
print(student)   #{'name': 'Deepak', 'course': 'Python'},,last se key value delete hoti h

student.clear()
print(student)

student2 = student.copy()


student = {
    "name": "Deepak",
    "age": 24
}

student.setdefault("city", "Patna")
print(student)                      # {'name': 'Deepak', 'age': 24, 'city': 'Patna'}

# अगर "city" पहले से मौजूद है, तो उसकी value change नहीं होगी।
