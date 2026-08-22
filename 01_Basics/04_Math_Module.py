import math

print(math.sqrt(25)) # result अक्सर float होता है।
print(math.pow(2, 3))
print(math.factorial(5))
print(math.pi)

# area of circle
import math
r = 5
area = math.pi * r ** 2
print(area)

# math.e — Euler's Number
print(math.e)

# ceil() number को ऊपर की तरफ nearest integer पर ले जाता है।
print(math.ceil(4.2))
print(math.ceil(4.9))
print(math.ceil(-4.7))

#floor() number को नीचे की तरफ nearest integer पर ले जाता है।
print(math.floor(4.2))
print(math.floor(4.9))
print(math.floor(-4.2))

#math.trunc() — Decimal हटाना
print(math.trunc(4.9))
print(math.trunc(-4.9))

# math.fabs() — Absolute Value
print(math.fabs(-25.5))

# math.gcd() — Greatest Common Divisor
print(math.gcd(12, 18))

# math.lcm() — Least Common Multiple
print(math.lcm(4, 6))