
Number_N = int(input("Enter the Number: "))

even_sum = 0

for n in range(1, Number_N + 1):

    if n % 2 == 0:
        print(n)
        even_sum = even_sum + n

print("Sum of Even Numbers:", even_sum)
