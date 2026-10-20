age = int(input("Enter your age: "))

base_fare = 500

if age <= 0:
    print("Invalid Age")

elif age < 5:
    final_fare = 0

elif age <= 12:
    final_fare = base_fare * 50 / 100

elif age <= 59:
    final_fare = base_fare

else:
    final_fare = base_fare * 60 / 100

if age > 0:
    print("Base Fare: ₹", base_fare)
    print("Final Fare: ₹", final_fare)
