import random

x = random.random()
print(x)

x = random.randint(1, 10) # 1st and last value included
print(x)


names = ["Rahul", "Amit", "Deepak", "Ravi"]
print(random.choice(names))


# shuffle() list ke elements ka order randomly change karta hai.

print(random.shuffle(names)) # None, Kyunki shuffle() list ko directly modify karta hai, lekin modified list ko return nahi karta.
random.shuffle(names)
print(names)


# random.randrange()
# random.randrange(start, stop, step)

print(random.randrange(1, 20, 2))

# 1 → 3 → 5 → 7 → 9 → 11 → 13 → 15 → 17 → 19
#                   ↑
#             # random selection

#  inhi selection me se hi random number dega


# -----------------------------------------------------------------------------
print(2+2+2)                    # 6
print(2.2 + 2.2 + 2.2)           # 6.6000000000000005
print(2.2 + 2.2 + 2.2 - 6.6)     # 8.881784197001252e-16  but ye to nhi aana chahiye tha,,,,,,,,,,Computer decimal numbers ko internally binary (0 aur 1) mein store karta hai. 2.2 ko binary mein exactly represent nahi kiya ja sakta. Isliye Python ek bahut close value store karta hai.

from decimal import Decimal
print(Decimal('2.2') + Decimal('2.2') + Decimal('2.2') - Decimal("6.60"))

# ----------------------------------------------------------------------------
from fractions import Fraction
print(Fraction(2, 3))