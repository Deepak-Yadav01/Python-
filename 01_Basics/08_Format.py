# 1. Basic format()
Name = "Deepak Yadav"
Age = 24

print("My name is {} and I am {} years old".format(Name, Age))

# Position ke sath
print("My name is {0} and I am {1} years old".format(Name, Age)) # {0} → Name  {1} → Age

# आजकल format() के बजाय f-string ज्यादा commonly use होती है:
name = "Deepak"
age = 25

print(f"My name is {name} and I am {age} years old")