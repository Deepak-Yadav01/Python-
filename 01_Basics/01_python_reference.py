# same reference kr rha 
p1 = [3, 6, 9, 12]
p2 = p1

print(p1)
print(p2)


print(p1 == p2)
print(p1 is p2)

p1[0] = 55
print(p1)
print(p2)



l1 = [1,2,3,4,5]
l2 = l1

l2[0]=66
print(l1)
print(l2)
# but yha alag alg objects bnenge
l2 =[1,2,3]
l1 =[1,2,3]
print(l1==l2)
print(l1 is l2)
l2[0]=77
print(l1)
print(l2)

# Agar alag list chahiye
p1 = [3, 6, 9, 12]
p2 = p1.copy()

p1[0] = 50

print(p1)
# [50, 6, 9, 12]

print(p2)
# [3, 6, 9, 12]

# Slicing se — .copy() ke bina
p1 = [3, 6, 9, 12]
p2 = p1[:]

p1[0] = 50

print(p1)
# [50, 6, 9, 12]

print(p2)
# [3, 6, 9, 12]