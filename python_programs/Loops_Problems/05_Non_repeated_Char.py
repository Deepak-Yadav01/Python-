input_string = "aabbcfcddeeF"

for char in input_string:
    if input_string.count(char) == 1:
        print("First Non-Repeated Character:", char)
        break
else:
    print("No Non-Repeated Character Found")    