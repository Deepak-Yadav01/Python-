units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = units * 7

elif units <= 300:
    bill = units * 10

else:
    bill = units * 12

print("Total Units:", units)
print("Total Electricity Bill: ₹", bill)
