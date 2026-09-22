# Python में join() method का use multiple strings को जोड़कर एक single string बनाने के लिए होता है।

words = ["Deepak", "is", "learning", "Python"]
result = " ".join(words)
print(result)

words = ["2026", "09", "20"]
print("-".join(words))

names = ["Deepak", "Rahul", "Amit"]
print(", ".join(names))

# Important: join() में list के elements generally strings होने चाहिए।
numbers = [1, 2, 3]
# print("-".join(numbers))  # ❌ Error
print("-".join(map(str, numbers)))


chai = "masala chai"
print(chai)

for letters in chai:
    print(letters)  # indentetion ka dhyan yha dena hota h

print(chai)
chai = "Masala\nChai"   # \n string ka next line me leke jata h
print(chai)

chai = r"Masala\nChai"  # Yahan r ka matlab raw string hai. #\n → new line ka escape sequence hai.
print(chai)             ## r"..." → Python ko bolta hai backslash (\) ko special character mat samjho

# path = r"c:\user\pwd\"
path = r"c:\\user\pwd\\"
print(path)

