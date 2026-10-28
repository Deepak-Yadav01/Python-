numbers = [1, -2, 0, 4, -25, 16, -12, -45, 4, -0, 5]

Positive_Count_Number = 0

for num in numbers:
    if num > 0:
        Positive_Count_Number += 1

print("Total Positive Numbers:", Positive_Count_Number)