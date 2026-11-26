# Scope ka mtlb hai ki kisi variable को Python program में कहाँ access  kr skte h
# 4 types of scopesare:

# L = Local Scope
# E = Enclosing Scope
# G = Global Scope
# B = Built-in Scope

def my_function():
    name = "Deepak"   # local variable, ye keval is function ke andr hi use ho skta h
    print(name)

my_function()

# print(name)    #NameError: name 'name' is not defined


# 2. Enclosing Scope (E),     जब एक function के अंदर दूसरा function होता है, तो Inner Function अपने Outer Function के variables को access कर सकता है।
def outer_function():

    name = "Deepak"

    def inner_function():
        print(f'inner_function: {name}')

    inner_function()
    print(f'outer_fun: {name}')
outer_function()


# 3. Global Scope (G)
name = "Deepak"

def my_function():
    print(name)

my_function()

print(name)
# Global variable को पूरे program में access कर सकते हैं।


# 4. Built-in Scope (B)
print("Hello")

len("Deepak")

max(10, 20, 30)

min(10, 20, 30)

sum([10, 20, 30])



#  LEGB Rule in Python
# Python किसी variable को खोजने के लिए एक निश्चित क्रम follow करता है।

# Local → Enclosing → Global → Built-in
