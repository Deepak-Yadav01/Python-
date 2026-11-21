# Definition: A generator function is a function that uses the yield keyword to return values one at a time while maintaining its state between calls.

# Normal Function Example
def my_function():
    return 10
    return 20
    return 30

result = my_function()

print(result) # bs 10 milega qki ek return milne pe fuction bahar aa jata h


# Generator Function Example
def my_generator():
    yield 10
    yield 20
    yield 30

result = my_generator()

print(result)  #इसकी values प्राप्त करने के लिए next() इस्तेमाल करेंगे।
print(next(result))
print(next(result))
print(next(result))
# print(next(result))


# yield keyword का काम function से एक value देना और function की execution को temporarily pause करना है।

# Example 1: Even Number Generator
def even_numbers():

    for num in range(1, 21):

        if num % 2 == 0:
            yield num


for number in even_numbers():
    print(number)



# ye dono same h bs alg alg tarike se likha gya h,
def even_numbers():

        for num in range(1, 21):

            if num % 2 == 0:
             yield num


gen = even_numbers()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))