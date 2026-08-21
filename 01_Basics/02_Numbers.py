# 1. Python में Numbers के Types mainly
# 3 built-in numeric types

# 1. int → Integer numbers
a = 10
b = 25
c = -50
d = 0

print(a)
print(b)
print(c)
print(d)

# 2. float → Decimal numbers
price = 99.50
percentage = 85.75
temperature = -2.5

print(price)
print(percentage)
print(temperature)

# 3. complex → Complex number
x = 3 + 4j  #Real part + Imaginary part

print(x)
print(x.real)
print(x.imag)

# 4. Number का Type कैसे Check करें?
x = 10
print(type(x))

x = 10.5
print(type(x))

x = 10 + 5j
print(type(x))

#5. Addition +
a = 10
b = 20
print(a + b)

#6. Subtraction -
a = 20
b = 10
print(a - b)

#8. Multiplication *
a = 10
b = 5
print(a * b)

# 9. Floor Division //
print(10 // 3)
print(-10 // 3)

# 10. Modulus %
print(10 % 3)

# 11. Power Operator **
print(2 ** 3)

# 12. Arithmetic Operators 
    # Operator	                Meaning                  	Example	Result
    # +                     Addition	                    10 + 3	13
    # -	                    Subtraction	                        10 - 3	7
    # *	                    Multiplication	                    10 * 3	30
    # /	                    Division	                        10 / 3	3.333...
    # //                    Floor Division	                10 // 3	3
    # %	                    Remainder	                        10 % 3	1
    # **                    Power	                        10 ** 3	1000

 # Comparison
a = 10
b = 20

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)