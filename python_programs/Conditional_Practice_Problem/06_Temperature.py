Temperature = int(input("Enter Temperature: "))
if Temperature>=40:
    print("temperature very hot")
elif Temperature>=30 and Temperature<=39:
    print("Temperature is HOT")
elif Temperature>=20 and Temperature <=29:
    print("Normal")
else:
    print("Cold")