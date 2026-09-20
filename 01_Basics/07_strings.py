# In Python, a string (str) is a sequence of characters used to store text.
name = "Alice"
message = 'Hello, world!'

# Important: Python strings are immutable. Methods don't change the original string:

text = "Python"

# Length
print(len(text))       # 6

# Access characters
print(text[0])         # P
print(text[-1])        # n

# Slicing    last include nhi hota
print(text[0:3])       # Pyt
print(text[2:])        # thon

# Combine strings
first = "Hello"
second = "World"
print(first + " " + second)   # Hello World

# Strings have many useful methods:
text = "hello python"

print(text.upper())          # HELLO PYTHON
print(text.capitalize())     # Hello python
print(text.replace("python", "world"))
print(text.split())          # ['hello', 'python']


name = "      deepak yadav  jyoti yadav  "
print(name.title())        #  Deepak Yadav  Jyoti Yadav   #  Capitalizes each word
print(name.strip())        # Removes spaces from both ends 
print(name.lstrip())
print(name.rstrip())

#rjust() aur ljust() string ko right/left side align karne ke liye use hote hain.
print(name.rjust(40,"-"))    # -------      deepak yadav  jyoti yadav  
print(name.ljust(40,"-"))    # deepak yadav  jyoti yadav  -------
print(name.center(40,"-"))   # ---      deepak yadav  jyoti yadav  ----

# Finds position of substring
frnd = "deepak yadav jyoti yadav"
print(frnd.find("jyoti")) # 13
print(frnd.find("yadav"))  # 7

print(frnd.count("a"))  # Counts occurrences