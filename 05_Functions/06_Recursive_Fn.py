# Definition: A recursive function is a function that calls itself until a specific condition is met.
# Recursive function में दो चीजें बहुत जरूरी हैं:
# 1. Base Case – Recursion को रोकने की condition.
# 2. Recursive Case – Function का खुद को call करना.

def numbers(n):

    if n == 6: #Base case
        return

    print(n)

    numbers(n + 1)  # recursive case


numbers(1) # initial function call




# FACTORIAL USING  RECURSION
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))


# Sum of Natural Numbers Using Recursion
def Natural_Sum(n):
    if n == 0:
        return 0
    return n + Natural_Sum(n - 1)
print(Natural_Sum(25))


# Fibonacci Series Using Recursion
#0, 1, 1, 2, 3, 5, 8, 13, 21...

def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(10):
    print(fibonacci(i), end=" ")   # end=" " का मतलब है कि सभी numbers एक ही line में print होंगे।